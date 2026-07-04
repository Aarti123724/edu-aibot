from pypdf import PdfReader


def extract_pdf_text(pdf_file):

    try:

        reader = PdfReader(pdf_file)

        pages = []

        for page_number, page in enumerate(reader.pages):

            page_text = page.extract_text()

            if page_text:

                pages.append(
                    {
                        "page": page_number + 1,
                        "text": page_text
                    }
                )

        return pages

    except Exception as e:

        print("PDF Extraction Error:", e)

        return []