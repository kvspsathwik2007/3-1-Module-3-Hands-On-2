import numpy as np


def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.

    Formula:

              A · B
    similarity = ─────────────
                 ||A|| ||B||

    Returns a value generally between -1 and 1.
    For normalized semantic embeddings, higher values
    indicate greater semantic similarity.
    """

    vector_a = np.asarray(vector_a, dtype=np.float32)
    vector_b = np.asarray(vector_b, dtype=np.float32)

    # Calculate vector magnitudes
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    # Avoid division by zero
    if norm_a == 0 or norm_b == 0:
        return 0.0

    # Dot product / product of magnitudes
    similarity = np.dot(vector_a, vector_b) / (
            norm_a * norm_b
    )

    return float(similarity)


def calculate_similarities(
        query_embedding,
        document_embeddings
):
    """
    Compare one query embedding against
    all document embeddings.

    Returns:
        [
            {
                "index": 0,
                "similarity": 0.82
            },
            ...
        ]
    """

    similarities = []

    for index, document_embedding in enumerate(
            document_embeddings
    ):

        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        similarities.append(
            {
                "index": index,
                "similarity": score
            }
        )

    return similarities