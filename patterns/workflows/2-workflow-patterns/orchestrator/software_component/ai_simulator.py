import json

def simulate_ai_response(prompt: str) -> str:
    """
    Simulates an AI response based on the given prompt.

    Args:
        prompt (str): The input prompt to simulate a response for.

    Returns:
        str: A JSON-formatted string representing the simulated AI response.
    """
    if "Analyze the following software requirements" in prompt:
        # Simulated response for the orchestrator's planning phase
        simulated_plan = {
            "system_overview": "This system manages user authentication, including registration, login, and password reset functionalities.",
            "design_patterns": ["Singleton", "Factory Method"],
            "modules": [
                {
                    "module_name": "UserRegistration",
                    "functionality": "Handles new user registrations and stores user data securely.",
                    "interfaces": ["IUserRegistration", "IDataStorage"],
                    "dependencies": ["DatabaseModule", "EmailService"]
                },
                {
                    "module_name": "UserLogin",
                    "functionality": "Manages user login sessions and authentication tokens.",
                    "interfaces": ["IUserLogin", "IAuthentication"],
                    "dependencies": ["DatabaseModule", "TokenService"]
                },
                {
                    "module_name": "PasswordReset",
                    "functionality": "Facilitates secure password reset requests and updates.",
                    "interfaces": ["IPasswordReset", "IEmailService"],
                    "dependencies": ["DatabaseModule", "EmailService"]
                }
            ]
        }
        return json.dumps(simulated_plan)
    
    elif "Develop the following software module" in prompt:
        # Simulated response for a worker's module development phase
        simulated_module = {
            "code": "class UserRegistration:\n    def register_user(self, user_data):\n        # Code to register a new user\n        pass",
            "tests": "def test_register_user():\n    # Unit test for register_user method\n    pass",
            "documentation": "This module handles the registration of new users, ensuring that user data is validated and stored securely."
        }
        return json.dumps(simulated_module)
    
    elif "Review the following software component design" in prompt:
        # Simulated response for the reviewer's cohesion analysis
        simulated_review = {
            "cohesion_score": 0.9,
            "suggested_edits": [
                {
                    "module_name": "UserRegistration",
                    "suggested_edit": "Ensure that the registration process includes email verification to enhance security."
                },
                {
                    "module_name": "UserLogin",
                    "suggested_edit": "Implement account lockout after multiple failed login attempts to prevent brute force attacks."
                }
            ],
            "final_design": "The software component design effectively addresses user authentication needs. Modules are well-structured, and the use of design patterns like Singleton and Factory Method promotes scalability and maintainability."
        }
        return json.dumps(simulated_review)
    
    else:
        # Default response for unrecognized prompts
        return json.dumps({"error": "Unrecognized prompt."})
