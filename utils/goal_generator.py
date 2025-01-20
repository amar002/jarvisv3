from utils.gemini_api import get_gpt_response

def generate_improved_goals(theme, user_goal):
    prompt = f"""
    Improve and suggest actionable steps for the following goal in the context of {theme}:
    Goal: {user_goal}
    Provide output in this format:
    - Improved Goal: [Improved Goal]
    - Actionable Steps:
      1. [Step 1]
      2. [Step 2]
      3. [Step 3]
    """
    return get_gpt_response(prompt)

def generate_actionable_steps(goal):
    """
    Use LLM to generate actionable steps for the given goal.
    """
    prompt = f"""
    Break down the following goal into actionable steps that can be tracked for progress:
    Goal: {goal}
    
    Provide the output as a list of steps.
    """
    response = get_gpt_response(prompt)
    return response.split("\n")  # Split the response into steps

