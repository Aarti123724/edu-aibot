from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def split_text(text, chunk_size=1000):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks


def create_embeddings(chunks):

    print("Total Chunks:", len(chunks))

    embeddings = embedding_model.encode(
        chunks
    )

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    print("Embedding Shape:", embeddings.shape)

    return embeddings


def create_faiss_index(embeddings):

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    print("FAISS Input Shape:", embeddings.shape)

    if len(embeddings.shape) != 2:
        raise ValueError(
            f"Invalid embedding shape: {embeddings.shape}"
        )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(embeddings)

    return index

def search_chunks(question, chunks, embeddings, index, top_k=7):

    question_embedding = embedding_model.encode(
        [question]
    )

    distances, indices = index.search(
        np.array(question_embedding, dtype="float32"),
        top_k
    )

    relevant_chunks = []

    for idx in indices[0]:

        relevant_chunks.append(
            chunks[idx]
        )

    return relevant_chunks