import openai

from config.settings import settings

openai.api_key = settings.openai_api_key


def generate_prompt(language, user_query, policy_data):
    if language == "en":
        prompt = f"Q: {user_query}\nA: Based on Amazon's return policy: {policy_data}"
    elif language == "es":
        prompt = f"Q: {user_query}\nA: Basado en la política de devoluciones de Amazon: {policy_data}"
    else:
        prompt = f"Q: {user_query}\nA: Based on Amazon's return policy: {policy_data}"

    return prompt


def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
