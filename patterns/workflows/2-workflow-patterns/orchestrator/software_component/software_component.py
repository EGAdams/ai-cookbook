from typing import List, Dict
from pydantic import BaseModel, Field
import os
import logging

from ai_simulator import simulate_ai_response


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

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

Return your response in this format:

# System Overview
[Provide a high-level overview of the system.]

# Design Patterns
- [List of design patterns to be applied]

# Modules
## Module 1
- Name: module_name
- Functionality: description of what this module does
- Interfaces: [List of interfaces]
- Dependencies: [List of dependencies]

[Additional modules as needed...]
"""

WORKER_PROMPT = """
Develop the following software module based on the provided specifications.

Module Name: {module_name}
Functionality: {functionality}
Interfaces: {interfaces}
Dependencies: {dependencies}

Return your response in this format:

# Code
[Provide the complete source code for the module.]

# Tests
[Provide unit tests for the module.]

# Documentation
[Provide documentation for the module.]
"""

REVIEWER_PROMPT = """
Review the following software component design for cohesion and integration.

System Overview: {system_overview}
Modules:
{modules}

Provide a cohesion score between 0.0 and 1.0, suggested edits for each module if needed, and a final polished design of the complete software component.

The cohesion score should reflect how well the modules integrate and work together, with 1.0 being perfect cohesion.
For suggested edits, focus on improving module interactions and maintaining consistent design patterns across modules.
The final design should incorporate your suggested improvements into a cohesive software component.
"""

# --------------------------------------------------------------
# Step 3: Implement orchestrator
# --------------------------------------------------------------

class SoftwareOrchestrator:
    def __init__(self):
        self.modules_implementation = {}

    def get_plan(self, requirements: str, constraints: str) -> BaseModel:
        """Get orchestrator's software component structure plan"""
        response = simulate_ai_response(
            ORCHESTRATOR_PROMPT.format(requirements=requirements, constraints=constraints)
        )
        return OrchestratorPlan.model_validate_json(response)  # Updated for Pydantic v2

    def develop_module(self, module_task: BaseModel) -> BaseModel:
        """Worker: Develop a specific software module"""
        response = simulate_ai_response(
            WORKER_PROMPT.format(
                module_name=module_task.module_name,
                functionality=module_task.functionality,
                interfaces=", ".join(module_task.interfaces),
                dependencies=", ".join(module_task.dependencies),
            )
        )
        return ModuleImplementation.model_validate_json(response)  # Updated for Pydantic v2

    def review_design(self, plan: BaseModel) -> BaseModel:
        """Reviewer: Analyze and improve overall cohesion"""
        modules_text = "\n\n".join(
            [
                f"=== {module.module_name} ===\nFunctionality: {module.functionality}\nInterfaces: {', '.join(module.interfaces)}\nDependencies: {', '.join(module.dependencies)}"
                for module in plan.modules
            ]
        )
        response = simulate_ai_response(
            REVIEWER_PROMPT.format(
                system_overview=plan.system_overview,
                modules=modules_text,
            )
        )
        return ReviewFeedback.model_validate_json(response)  # Updated for Pydantic v2

    def design_software_component(self, requirements: str, constraints: str) -> Dict:
        """Process the entire software component design task"""
        logger.info("Starting software component design process")

        # Get software component structure plan
        plan = self.get_plan(requirements, constraints)
        logger.info(f"Software structure planned: {len(plan.modules)} modules")
        logger.info(f"Software structure planned: {plan.model_dump_json(indent=2)}")  # Updated for Pydantic v2

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
# Step 4: Example usage
# --------------------------------------------------------------

if __name__ == "__main__":
    orchestrator = SoftwareOrchestrator()

    # Example: Designing a user authentication system
    requirements = (
        "The system should allow users to register, log in, and reset passwords securely."
    )
    constraints = "Use RESTful API principles and ensure compatibility with OAuth 2.0."

    result = orchestrator.design_software_component(
        requirements=requirements, constraints=constraints
    )

    print("\nFinal Software Design:")
    print(result["review"].final_design)

    print("\nCohesion Score:", result["review"].cohesion_score)
    if result["review"].suggested_edits:
        for edit in result["review"].suggested_edits:
            print(f"Module: {edit.module_name}")
            print(f"Suggested Edit: {edit.suggested_edit}")