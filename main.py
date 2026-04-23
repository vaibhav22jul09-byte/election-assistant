import os
from helper import check_eligibility, get_election_steps, ask_gemini

def main():
    print("Welcome to Smart Election Assistant")

    while True:
        print("\n1. Check Voting Eligibility")
        print("2. Election Process")
        print("3. Ask AI")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            age = input("Enter your age: ")
            citizenship = input("Are you an Indian citizen? (yes/no): ")
            print(check_eligibility(age, citizenship))

        elif choice == "2":
            print(get_election_steps())

        elif choice == "3":
            question = input("Ask your question: ")
            print(ask_gemini(question))

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
