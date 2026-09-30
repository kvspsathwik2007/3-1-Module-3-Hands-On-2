import os
import numpy as np

from config.config import (
    EMBEDDINGS_FILE,
    TOP_K
)

from services.embedding_service import (
    embedding_service
)

from services.document_service import (
    document_service
)

from utils.similarity import (
    calculate_similarities
)


class RetrievalService:

    def __init__(self):
        self.embeddings = None

    def load_embeddings(self):
        """
        Load cached document embeddings.
        """

        if not os.path.exists(EMBEDDINGS_FILE):
            raise FileNotFoundError(
                "Document embeddings not found. "
                "Run generate_embeddings.py first."
            )

        self.embeddings = np.load(
            EMBEDDINGS_FILE
        )

        return self.embeddings

    def build_index(self):
        """
        Generate embeddings for all documents
        and save them to disk.
        """

        documents = (
            document_service.get_documents()
        )

        texts = [
            f"{doc['title']}. {doc['content']}"
            for doc in documents
        ]

        embeddings = (
            embedding_service.generate_embeddings(
                texts
            )
        )

        np.save(
            EMBEDDINGS_FILE,
            embeddings
        )

        self.embeddings = embeddings

        return {
            "documents": len(documents),
            "embedding_dimensions": int(
                embeddings.shape[1]
            )
        }

    def search(self, query):
        """
        Perform embedding-based document retrieval.
        """

        if not query or not query.strip():
            raise ValueError(
                "Query cannot be empty."
            )

        documents = (
            document_service.get_documents()
        )

        if self.embeddings is None:
            self.load_embeddings()

        if len(documents) != len(
                self.embeddings
        ):
            raise ValueError(
                "Document count and embedding count "
                "do not match. Rebuild the index."
            )

        # Generate query embedding
        query_embedding = (
            embedding_service.generate_embedding(
                query
            )
        )

        # Calculate similarity
        similarities = calculate_similarities(
            query_embedding,
            self.embeddings
        )

        # Sort highest similarity first
        similarities.sort(
            key=lambda item: item["similarity"],
            reverse=True
        )

        # Select TOP_K
        top_results = similarities[:TOP_K]

        results = []

        for item in top_results:

            document = documents[
                item["index"]
            ]

            results.append(
                {
                    "id": document["id"],
                    "title": document["title"],
                    "content": document["content"],
                    "similarity": round(
                        item["similarity"],
                        4
                    )
                }
            )

        return results


retrieval_service = RetrievalService()