from sentence_transformers import SentenceTransformer

from config.config import EMBEDDING_MODEL


class EmbeddingService:

    def __init__(self):
        print(
            f"Loading embedding model: {EMBEDDING_MODEL}"
        )

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("Embedding model loaded successfully.")

    def generate_embedding(self, text):
        """
        Generate an embedding for a single text.
        """

        if not text or not text.strip():
            raise ValueError(
                "Text cannot be empty."
            )

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=False
        )

        return embedding

    def generate_embeddings(self, texts):
        """
        Generate embeddings for multiple documents.
        """

        if not texts:
            raise ValueError(
                "Text list cannot be empty."
            )

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=False,
            show_progress_bar=True
        )

        return embeddings


# Singleton service
embedding_service = EmbeddingService()