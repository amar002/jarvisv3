from utils.gemini_api import get_gpt_response

def generate_appreciation_message(goal_name):
    prompt = f"Write a motivational message in less than 5 words for completing the goal: {goal_name}."
    return get_gpt_response(prompt)
