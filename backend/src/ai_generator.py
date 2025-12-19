import os
import json
from openai import OpenAI
from typing import Any
from .default_return import ai_response_fail_default
import random
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> dict[str, Any]:
    system_prompt = f"""
    You are an expert coding challenge creator. 
    Your task is to generate a **unique** coding question with multiple choice answers.
    The question should match the specified difficulty level: {difficulty}.

    Rules:
    1. For **easy** questions: Use basic syntax, simple operations, or common programming concepts.
    2. For **medium** questions: Include intermediate concepts like data structures, algorithms, or language features.
    3. For **hard** questions: Cover advanced topics such as design patterns, optimization, or complex algorithms.
    4. Always ensure **only one answer is correct**. The other options must be plausible but incorrect.
    5. Avoid repeating topics from previous questions. Make each question scenario or example unique.
    6. Randomize numbers, variable names, and data structures wherever possible to ensure variety.
    7. Shuffle the order of options in a way that the correct answer index matches the correct option.

    Return the challenge strictly in the following JSON format:
    {{
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }}

    Make sure the questions are realistic, clear, and solvable within a short coding exercise. 
    Prioritize uniqueness and variety over common examples.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty coding challenge."}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title","options","correct_answer_id","explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")
        return challenge_data


    except Exception as e:
        print(e)
        return random.choice(ai_response_fail_default)