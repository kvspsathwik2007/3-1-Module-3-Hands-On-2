from services.document_service import (
    document_service
)

from services.retrieval_service import (
    retrieval_service
)


def main():

    print("=" * 60)
    print("GENERATING DOCUMENT EMBEDDINGS")
    print("=" * 60)

    documents = (
        document_service.get_documents()
    )

    print(
        f"Documents found: {len(documents)}"
    )

    result = (
        retrieval_service.build_index()
    )

    print()
    print("Embedding generation completed.")
    print(
        f"Documents: {result['documents']}"
    )
    print(
        f"Dimensions: {result['embedding_dimensions']}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()