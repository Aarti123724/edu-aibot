def rewrite_question(
    model,
    chat_history,
    question
):
    print("=" * 80)
    print("rewrite_question() CALLED")
    print("Original Question:", question)
    print("=" * 80)

    prompt = f"""
You are an expert query rewriter for a RAG chatbot.

Conversation:

{chat_history}

Latest User Question:

{question}

If the latest question is referring to something mentioned earlier
(using words like "it", "this", "that", "explain more", "continue"),
rewrite it into a complete standalone question.

Example:

Conversation:

User: What is Artificial Intelligence?

Assistant: ...

User: Explain it in simple words.

Output:

Explain Artificial Intelligence in simple words.

Return ONLY the rewritten question.
Do NOT answer the question.
Do NOT explain anything.
"""

    response = model.generate_content(prompt)

    rewritten = response.text.strip()

    print("Rewritten Question:", rewritten)
    print("=" * 80)

    return rewritten