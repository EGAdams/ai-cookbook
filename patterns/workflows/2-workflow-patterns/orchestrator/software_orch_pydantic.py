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
    """Task for developing a software module"""
    module_name: str = Field(description="Name of the module to develop")
    functionality: str = Field(description="Description of the module's functionality")
    interfaces: List[str] = Field(description="List of interfaces the module should implement")
    dependencies: List[str] = Field(description="Other modules or services this module depends on")

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
    module_name: str = Field(description="Name of the module")
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
"""

WORKER_PROMPT = """
Develop the following software module based on the provided specifications.

Module Name: {module_name}
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

    def get_plan(self, requirements: str, constraints: str) -> OrchestratorPlan:
        """Get orchestrator's software component structure plan"""
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",  # Ensure the correct model is used
            messages=[
                {
                    "role": "system",
                    "content": ORCHESTRATOR_PROMPT.format(
                        requirements=requirements, constraints=constraints
                    ),
                }
            ],
            response_format=OrchestratorPlan,  # Ensure response is parsed correctly into the Pydantic model
        )
        return completion.choices[0].message.parsed  # Return the structured response


    def develop_module(self, module_task: ModuleTask) -> ModuleImplementation:
        """Worker: Develop a specific software module"""
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": WORKER_PROMPT.format(
                    module_name=module_task.module_name,
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
                f"=== {module.module_name} ===\nFunctionality: {module.functionality}\nInterfaces: {', '.join(module.interfaces)}\nDependencies: {', '.join(module.dependencies)}"
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
            logger.info(f"Developing module: {module_task.module_name}")
            implementation = self.develop_module(module_task)
            self.modules_implementation[module_task.module_name] = implementation

        # Review and polish
        logger.info("Reviewing full software component design")
        review = self.review_design(plan)

        return {"structure": plan, "modules": self.modules_implementation, "review": review}

# --------------------------------------------------------------
# Step 4: Example usage - Building from GitHub Repo
# --------------------------------------------------------------

if __name__ == "__main__":
    orchestrator = SoftwareOrchestrator()

    # Example: Building a project from a GitHub repository
    requirements = (
        "Retrieve the README.md file from the specified GitHub repository and analyze the installation and build instructions."
        "Follow the documented steps to set up the development environment and build the project."
    )
    constraints = (
        "Ensure compatibility with the listed dependencies and required frameworks. "
        "Provide any missing setup instructions if necessary and verify that all build steps are executed correctly."
    )

    result = orchestrator.design_software_component(
        requirements=requirements, constraints=constraints
    )

    print("\nFinal Software Build Plan:")
    print(result["review"].final_design)

    print("\nCohesion Score:", result["review"].cohesion_score)
    if result["review"].suggested_edits:
        for edit in result["review"].suggested_edits:
            print(f"\nModule: {edit.module_name}")
            print(f"Suggested Edit: {edit.suggested_edit}")
# 030125
