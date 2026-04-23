from flask import Flask, request
from helper import check_eligibility, get_election_steps, ask_gemini

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🗳️ Smart Election Assistant</h1>

    <h3>Check Voting Eligibility</h3>
    <form action="/eligibility">
        Age: <input name="age"><br><br>
        Citizen (yes/no): <input name="citizen"><br><br>
        <input type="submit" value="Check">
    </form>

    <h3>Ask AI Question</h3>
    <form action="/ask">
        Question: <input name="q"><br><br>
        <input type="submit" value="Ask">
    </form>

    <h3>Election Process</h3>
    <a href="/steps">View Election Steps</a>
    """

@app.route("/eligibility")
def eligibility():
    age = request.args.get("age", "")
    citizen = request.args.get("citizen", "")
    return check_eligibility(age, citizen)

@app.route("/steps")
def steps():
    return get_election_steps()

@app.route("/ask")
def ask():
    q = request.args.get("q", "")
    return ask_gemini(q)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
