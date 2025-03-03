import datetime
from typing import List, Dict
from pydantic import BaseModel, Field
from openai import OpenAI
import os
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


model = "gpt-4o-mini"

# --------------------------------------------------------------
# Step 1: Define the data models
# --------------------------------------------------------------

class ModuleTask(BaseModel):
    """Defines an individual module within the orchestrator plan."""
    name: str = Field(description="Module name")
    functionality: str = Field(description="Description of what this module does")
    interfaces: List[str] = Field(description="List of interfaces provided or used by this module")
    dependencies: List[str] = Field(description="List of dependencies required by this module")


class OrchestratorPlan(BaseModel):
    """Orchestrator's software component structure and tasks"""
    system_overview: str = Field(description="High-level overview of the software component")
    design_patterns: List[str] = Field(description="Design patterns to be used")
    modules: List[ModuleTask] = Field(description="List of modules to develop")

class ModuleImplementation(BaseModel):
    """Implementation details of a module"""
    code: str = Field(description="Source code of the module")
    tests: str = Field(description="Unit tests for the module")
    documentation: str = Field(description="Documentation for the module")

class SuggestedEdits(BaseModel):
    """Suggested edits for a module"""
    name: str = Field(description="Name of the module")
    suggested_edit: str = Field(description="Suggested edit")

class ReviewFeedback(BaseModel):
    """Final review and suggestions"""
    cohesion_score: float = Field(description="How well modules integrate together (0-1)")
    suggested_edits: List[SuggestedEdits] = Field(description="Suggested edits by module")
    final_design: str = Field(description="Complete, polished design of the software component")

# --------------------------------------------------------------
# Step 2: Define prompts
# --------------------------------------------------------------

ORCHESTRATOR_PROMPT = """
Analyze the following software requirements and design a component structure.

Requirements: {requirements}
Design Constraints: {constraints}

Return your response in this format:

# System Overview
{system_overview}

# Design Patterns
{design_patterns}

# Modules
{modules}
"""

MODULE_TEMPLATE = """
## {name}
- Functionality: {functionality}
- Interfaces: {interfaces}
- Dependencies: {dependencies}
"""


WORKER_PROMPT = """
Develop the following software module based on the provided specifications.

Module Name: {name}
Functionality: {functionality}
Interfaces: {interfaces}
Dependencies: {dependencies}
"""

REVIEWER_PROMPT = """
Review the following software component design for cohesion and integration.

System Overview: {system_overview}
Modules:
{modules}
"""

# --------------------------------------------------------------
# Step 3: Implement orchestrator using structured output parsing
# --------------------------------------------------------------

class SoftwareOrchestrator:
    def __init__(self):
        self.modules_implementation = {}
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        now = datetime.datetime.now()
        timestamp = now.strftime("%B_%d__%I_%M_%p")
        self.project_directory_name  = f"build_{timestamp}"
        print( f"creating directory { self.project_directory_name }..." )
        os.makedirs( self.project_directory_name , exist_ok=True)
        print( f"directory { self.project_directory_name } created." )

    def get_plan(self, requirements: str, constraints: str) -> OrchestratorPlan:
        """Get orchestrator's software component structure plan."""
        
        # First, make an API call to get structured data
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",  # Ensure correct model usage
            messages=[
                {
                    "role": "system",
                    "content": ORCHESTRATOR_PROMPT.format(
                        requirements=requirements,
                        constraints=constraints,
                        system_overview="{system_overview}",
                        design_patterns="{design_patterns}",
                        modules="{modules}"
                    ),
                }
            ],
            response_format=OrchestratorPlan,  # Ensure response is parsed into Pydantic model
        )

        plan = completion.choices[0].message.parsed  # Extract structured response

        # Format the module list dynamically
        formatted_modules = "\n".join(
            MODULE_TEMPLATE.format(
                name=module.name,
                functionality=module.functionality,
                interfaces=", ".join(module.interfaces),
                dependencies=", ".join(module.dependencies)
            )
            for module in plan.modules
        )

        # Final formatting
        prompt_content = ORCHESTRATOR_PROMPT.format(
            requirements=requirements,
            constraints=constraints,
            system_overview=plan.system_overview,
            design_patterns="\n- ".join(plan.design_patterns),
            modules=formatted_modules
        )

        # return prompt_content  # Return the structured and formatted response
        # put the prompt into a file named plan.md
        with open( f"{ self.project_directory_name }/_plan.md", "w") as f: # "_" puts it on the top
            f.write(prompt_content)

        return plan
 

    def develop_module(self, module_task: ModuleTask) -> ModuleImplementation:
        """Worker: Develop a specific software module"""
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": WORKER_PROMPT.format(
                    name=module_task.name,
                    functionality=module_task.functionality,
                    interfaces=", ".join(module_task.interfaces),
                    dependencies=", ".join(module_task.dependencies),
                )}
            ],
            response_format=ModuleImplementation,
        )
        return response.choices[0].message.parsed

    def review_design(self, plan: OrchestratorPlan) -> ReviewFeedback:
        """Reviewer: Analyze and improve overall cohesion"""
        modules_text = "\n\n".join(
            [
                f"=== {module.name} ===\nFunctionality: {module.functionality}\nInterfaces: {', '.join(module.interfaces)}\nDependencies: {', '.join(module.dependencies)}"
                for module in plan.modules
            ]
        )
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": REVIEWER_PROMPT.format(
                    system_overview=plan.system_overview,
                    modules=modules_text,
                )}
            ],
            response_format=ReviewFeedback,
        )
        return response.choices[0].message.parsed

    def design_software_component(self, requirements: str, constraints: str) -> Dict:
        """Process the entire software component design task"""
        logger.info("Starting software component design process")
        
        # Get software component structure plan
        plan = self.get_plan(requirements, constraints)
        logger.info(f"Software structure planned: {len(plan.modules)} modules")
        logger.info(f"Software structure planned: {plan.model_dump_json(indent=2)}")

        # Develop each module
        for module_task in plan.modules:
            logger.info(f"Developing module: { module_task.name }")
            implementation = self.develop_module(module_task)
            self.modules_implementation[module_task.name] = implementation

            # snake case the module_task.name by lowercasing all names in the class and putting underscores after all of them except for the first one.
            # for example: `ApacheServerManager` becomes `apache_server_manager`
            module_directory_name = "".join(["_" + char.lower() if char.isupper() else char for char in module_task.name])[1:]
            print(f"module_directory_name: {module_directory_name}")
            with open(f"{ self.project_directory_name }/plan.md", "w") as f:
                f.write(plan.model_dump_json(indent=2))
            
            with open(f"{ self.project_directory_name }/{ module_directory_name }/{ module_task.name }.py", "w") as f:
                f.write( implementation.code )
            with open(f"{ self.project_directory_name }/{ module_directory_name }/{ module_task.name }_tests.py", "w") as f:
                f.write( implementation.tests )
            with open(f"{ self.project_directory_name }/{ module_directory_name }/{ module_task.name }_docs.md", "w") as f:
                f.write( implementation.documentation )

        # Review and polish
        logger.info("Reviewing full software component design")
        review = self.review_design(plan)

        return {"structure": plan, "modules": self.modules_implementation, "review": review}

# --------------------------------------------------------------
# Step 4: Example usage - Building from GitHub Repo
# --------------------------------------------------------------

if __name__ == "__main__":
    orchestrator = SoftwareOrchestrator()

    # Example: Building a server manager system
    requirements = (
        "Design and implement a Server Manager system that provides functionality to start, stop, and check the status of servers. "
        "The system should allow for retrieving server error logs. "
        "Create a base ServerManager interface or abstract class that defines these operations. "
        "Implement specific managers for MySQL and Apache servers by extending the base ServerManager. "
        "Ensure that each server manager correctly handles process management and error retrieval."
    )

    constraints = (
        "The system should follow SOLID principles to allow easy extension for other server types in the future. "
        "Implement the system in Python and ensure it is compatible with Linux-based server environments. "
        "Use subprocess or OS-specific commands for starting, stopping, and checking the status of the servers. "
        "Provide unit tests to verify the correct functionality of each component. "
    )

    result = orchestrator.design_software_component(
        requirements=requirements, constraints=constraints
    )

# 030225
