from dotenv import load_dotenv
import os
import google.generativeai as genai

from classifier import is_education_question

# Load environment variables
load_dotenv()

# Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

print("🎓 EduBot Started")
print("Type 'exit' to quit\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Debugging
    result = is_education_question(question)
    print("Classifier Result:", result)

    # Domain Check
    if not result:
        print("\nBot:")
        print("Sorry, I can only answer educational questions.\n")
        continue

    try:
        response = model.generate_content(question)

        print("\nBot:")
        print(response.text)
        print()

    except Exception as e:
        print("\nError:", e)