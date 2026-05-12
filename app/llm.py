'''import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_response(prompt):

    response = model.generate_content(prompt)

    return response.text'''

def generate_response(prompt):

    return """
Based on the hiring requirements, these SHL assessments are recommended:

1. Java Programming Assessment
2. Communication Skills Test
3. Cognitive Ability Test

These assessments help evaluate technical and interpersonal skills effectively.
"""