import os

def check_eligibility(age, citizenship):
    if not age.isdigit():
        return "Invalid age input"

    age = int(age)

    if age >= 18 and citizenship.lower() == "yes":
        return "You are eligible to vote in India."
    else:
        return "You are not eligible to vote."

def get_election_steps():
    return """
Election Process in India:

1. Register as a voter (Form 6)
2. Verify your name in voter list
3. Receive Voter ID
4. Go to polling booth
5. Cast your vote using EVM
"""

def ask_gemini(question):
    try:
        import google.generativeai as genai

        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")

        prompt = f"Explain simply: {question} about Indian elections"
        response = model.generate_content(prompt)

        return response.text

    except Exception:
        return "AI service unavailable."
