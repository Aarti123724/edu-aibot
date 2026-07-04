from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def split_text(text, chunk_size=500, overlap=100):

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(text), step):

        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    return chunks


def split_documents(
    documents,
    chunk_size=500,
    overlap=100
):

    chunks = []
    metadata = []

    step = chunk_size - overlap

    for document in documents:

        text = document["text"]
        source = document["source"]
        page = document["page"]


        for i in range(0, len(text), step):

            chunk = text[i:i + chunk_size]

            if not chunk.strip():
                continue

            chunks.append(chunk)

            metadata.append(
                {
                    "source": source,
                    "page": page
                }
            )

    return chunks, metadata


def create_embeddings(chunks):

    print("Total Chunks:", len(chunks))

    embeddings = embedding_model.encode(
        chunks,
        normalize_embeddings=True
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

    # Cosine Similarity
    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(embeddings)

    return index


def search_chunks(
    question,
    chunks,
    metadata,
    embeddings,
    index,
    top_k=8
):

    question_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    )

    distances, indices = index.search(
        np.array(question_embedding, dtype="float32"),
        top_k
    )

    results = []

    for score, idx in zip(distances[0], indices[0]):

        if idx == -1:
            continue

        results.append(
            {
                "text": chunks[idx],
                "source": metadata[idx]["source"],
                "page": metadata[idx]["page"],
                "score": float(score)
            }
        )

    print("\n========== Retrieved Chunks ==========")

    if len(results) == 0:
        print("No relevant chunks found.")

    for r in results:
        print("--------------------------------------")
        print("Source :", r["source"])
        print("Score  :", round(r["score"], 4))
        print("Preview:", r["text"][:150].replace("\n", " "))

    print("======================================\n")

    return results