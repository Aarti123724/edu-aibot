from rag_utils import (
    create_embeddings,
    create_faiss_index,
    search_chunks
)


class RAGService:

    def build_index(
        self,
        chunks
    ):

        embeddings = create_embeddings(
            chunks
        )

        index = create_faiss_index(
            embeddings
        )

        return embeddings, index

    def search(
        self,
        question,
        chunks,
        metadata,
        embeddings,
        index
    ):

        return search_chunks(
            question,
            chunks,
            metadata,
            embeddings,
            index
        )
