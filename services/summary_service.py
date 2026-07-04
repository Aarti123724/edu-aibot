def generate_summary(model, pdf_text):

    prompt = f"""
    Summarize the following educational document.

    Give:

    1. Main Topics
    2. Key Concepts
    3. Important Points
    4. Short Summary

    Document:

    {pdf_text[:10000]}
    """

    response = model.generate_content(prompt)

    return response.text
