from pdf2image import convert_from_bytes

def extract_text_with_gemini(pdf_file, model):

    try:

        images = convert_from_bytes(
            pdf_file.read()
        )

        prompt = """
        You are a professional OCR engine.

        Extract ALL text exactly as written.

        The pages may contain:
        - Handwritten notes
        - Printed text
        - Mixed handwriting and printed text
        - Tables
        - Diagrams with labels

        Rules:
        1. Do not summarize.
        2. Do not explain.
        3. Preserve line breaks.
        4. Read difficult handwriting carefully.
        5. Return only extracted text.
        6. Do not add information that is not visible.
        7. Include page headings if present.
        8. Preserve numbered points and bullet points.

        Output only the extracted text.
        """

        content = [prompt]

        for page_num, image in enumerate(images, start=1):

            print(f"Adding Page {page_num}")

            content.append(image)

        response = model.generate_content(
            content
        )

        return response.text

    except Exception as e:

        print("Gemini OCR Error:", e)

        return ""