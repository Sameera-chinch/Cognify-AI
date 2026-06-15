import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(text):

    prompt = f"""
    Summarize the following study material in a clear and concise way:

    {text}
    """

    response = model.generate_content(prompt)

    return response.text