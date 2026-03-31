import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class EduAgent:
    """
    Single AI Agent
    Task: Answer educational questions with structured explanation
    """

    def __init__(self):
        self.client = client

    def run(self, user_input: str) -> str:
        prompt = f"""
        You are an educational AI assistant.

        Explain the following question in a clear and structured way.

        Rules:
        - Keep the answer concise (150-200 words)
        - Use bullet points
        - Use simple language for students
        - Do NOT include unnecessary details

        Question:
        {user_input}
        """

        response = self.client.models.generate_content( # type: ignore
            model="gemini-3-flash-preview",
            contents=prompt,
        )

        return response.text # type: ignore