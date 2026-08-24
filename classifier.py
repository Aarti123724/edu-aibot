print("🔥 NEW CLASSIFIER FILE LOADED")

def is_education_question(question, model):

    prompt = f"""
    Determine whether this question is educational.

    Reply with ONLY:
    EDUCATION
    or
    NON_EDUCATION

    Question:
    {question}
    """

    try:
        print("🔥 Calling Gemini classifier...")
        
        response = model.generate_content(prompt)

        print("🔥 Gemini response received")

        result = response.text.strip().upper()

        print("Classifier:", result)

        return (
            "EDUCATION" in result
            and "NON_EDUCATION" not in result
        )

    except Exception as e:

        print("❌ CLASSIFIER GEMINI ERROR:")
        print(type(e).__name__)
        print(str(e))

        raise