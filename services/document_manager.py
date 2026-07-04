from pdf_utils import extract_pdf_text
from rag_utils import split_documents


class DocumentManager:

    def process_documents(
        self,
        uploaded_files,
        rag
    ):

        pdf_text = ""
        documents = []

        for uploaded_file in uploaded_files:

            pages = extract_pdf_text(uploaded_file)

            if len(pages) == 0:
                continue

            pdf_text += f"\n\n===== {uploaded_file.name} =====\n\n"

            for page in pages:

                pdf_text += page["text"] + "\n"

                documents.append(
                    {
                        "source": uploaded_file.name,
                        "page": page["page"],
                        "text": page["text"]
                    }
                )

        chunks, metadata = split_documents(documents)

        if len(chunks) == 0:

            return None

        embeddings, index = rag.build_index(chunks)

        return {
            "pdf_text": pdf_text,
            "chunks": chunks,
            "metadata": metadata,
            "embeddings": embeddings,
            "index": index
        }