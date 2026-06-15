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
def generate_flashcards(text):

    prompt = f"""
    You are an expert study assistant.

    Create 5 flashcards from the study material below.

    Return them in the format:

    Question: ...
    Answer: ...

    Text:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text

def generate_quiz(text):

    prompt = f"""
    Create 5 multiple choice questions from the following text.

    Format:

    Question: ...
    A) ...
    B) ...
    C) ...
    D) ...
    Answer: ...

    Text:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text
