import os
import openai
from dataclasses import dataclass
from typing import List
import unittest

# --------------------------------------------------------------
# Step 1: Set Up OpenAI API Client
# --------------------------------------------------------------

# Ensure you have your OpenAI API key set as an environment variable
# You can set it in your environment or directly in the code (not recommended for security reasons)
# Example: export OPENAI_API_KEY='your-api-key'
openai.api_key = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------------------
# Step 2: Define Data Models
# --------------------------------------------------------------

@dataclass
class Task:
    description: str
    completed: bool = False

@dataclass
class Result:
    success: bool
    message: str

# --------------------------------------------------------------
# Step 3: Implement the Worker
# --------------------------------------------------------------

class Worker:
    def process(self, task: Task) -> Result:
        # Use OpenAI API to analyze the task description
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Analyze the following task and determine if it's actionable:\n\nTask: {task.description}\n",
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.5,
            )
            analysis = response.choices[0].text.strip()
            if "actionable" in analysis.lower():
                task.completed = True
                return Result(success=True, message=f"Task '{task.description}' marked as completed.")
            else:
                return Result(success=False, message=f"Task '{task.description}' is not actionable.")
        except Exception as e:
            return Result(success=False, message=f"Error processing task: {str(e)}")

# --------------------------------------------------------------
# Step 4: Implement the Orchestrator
# --------------------------------------------------------------

class Orchestrator:
    def __init__(self):
        self.worker = Worker()
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        task = Task(description=description)
        self.tasks.append(task)
        return task

    def process_tasks(self) -> List[Result]:
        results = []
        for task in self.tasks:
            if not task.completed:
                result = self.worker.process(task)
                results.append(result)
        return results

# --------------------------------------------------------------
# Step 5: Write Tests Using TDD
# --------------------------------------------------------------

class TestTodoListSystem(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_add_task(self):
        task_description = "Write unit tests for the to-do list system."
        task = self.orchestrator.add_task(task_description)
        self.assertEqual(task.description, task_description)
        self.assertFalse(task.completed)
        self.assertIn(task, self.orchestrator.tasks)

    def test_process_actionable_task(self):
        task_description = "Buy groceries."
        task = self.orchestrator.add_task(task_description)
        results = self.orchestrator.process_tasks()
        self.assertEqual(len(results), 1)
        self.assertTrue(results[0].success)
        self.assertTrue(task.completed)
        self.assertIn("marked as completed", results[0].message)

    def test_process_non_actionable_task(self):
        task_description = "Dream about flying."
        task = self.orchestrator.add_task(task_description)
        results = self.orchestrator.process_tasks()
        self.assertEqual(len(results), 1)
        self.assertFalse(results[0].success)
        self.assertFalse(task.completed)
        self.assertIn("is not actionable", results[0].message)

    def test_process_tasks_with_api_error(self):
        # Temporarily unset the API key to simulate an error
        original_api_key = openai.api_key
        openai.api_key = None
        task_description = "Complete the project report."
        task = self.orchestrator.add_task(task_description)
        results = self.orchestrator.process_tasks()
        self.assertEqual(len(results), 1)
        self.assertFalse(results[0].success)
        self.assertIn("Error processing task", results[0].message)
        # Restore the original API key
        openai.api_key = original_api_key

if __name__ == "__main__":
    unittest.main()
