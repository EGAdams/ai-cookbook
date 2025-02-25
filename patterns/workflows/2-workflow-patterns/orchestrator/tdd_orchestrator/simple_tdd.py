from dataclasses import dataclass
from typing import List

# --------------------------------------------------------------
# Step 1: Define the Data Models
# --------------------------------------------------------------

@dataclass
class Task:
    description: str

@dataclass
class Result:
    output: str

# --------------------------------------------------------------
# Step 2: Implement the Worker
# --------------------------------------------------------------

class Worker:
    def process(self, task: Task) -> Result:
        # Simulate processing the task
        return Result(output=f"Processed: {task.description}")

# --------------------------------------------------------------
# Step 3: Implement the Orchestrator
# --------------------------------------------------------------

class Orchestrator:
    def __init__(self):
        self.worker = Worker()

    def handle_tasks(self, tasks: List[Task]) -> List[Result]:
        results = []
        for task in tasks:
            result = self.worker.process(task)
            results.append(result)
        return results

# --------------------------------------------------------------
# Step 4: Write Tests Using TDD
# --------------------------------------------------------------

import unittest

class TestOrchestratorWorkerPattern(unittest.TestCase):
    def test_worker_process(self):
        worker = Worker()
        task = Task(description="Test Task")
        result = worker.process(task)
        self.assertEqual(result.output, "Processed: Test Task")

    def test_orchestrator_handle_tasks(self):
        orchestrator = Orchestrator()
        tasks = [Task(description=f"Task {i}") for i in range(3)]
        results = orchestrator.handle_tasks(tasks)
        self.assertEqual(len(results), 3)
        for i, result in enumerate(results):
            self.assertEqual(result.output, f"Processed: Task {i}")

if __name__ == "__main__":
    unittest.main()
