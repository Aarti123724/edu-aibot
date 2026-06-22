print("🔥 NEW CLASSIFIER FILE LOADED")

def is_education_question(question, model):

    prompt = f"""
    You are a classifier.

    Determine whether the following question is educational.

    Educational topics include:
    - School Subjects
    - College Subjects
    - Mathematics
    - Physics
    - Chemistry
    - Biology
    - Computer Science
    - Programming
    - DBMS
    - Operating Systems
    - Computer Networks
    - Software Engineering
    - Engineering
    - Career Guidance
    - Interview Preparation

    Return ONLY one word:

    EDUCATION

    or

    NON_EDUCATION

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    result = response.text.strip().upper()

    print("Classifier:", result)

    return "EDUCATION" in result and "NON_EDUCATION" not in result