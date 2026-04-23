from flask import Flask, request, jsonify
from helper import check_eligibility, get_election_steps, ask_gemini

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart Election Assistant is running!"

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
