import json
import os

from config.config import DOCUMENTS_FILE


class DocumentService:

    def __init__(self):
        self.documents = []

    def load_documents(self):
        """
        Load documents from documents.json.
        """

        if not os.path.exists(DOCUMENTS_FILE):
            raise FileNotFoundError(
                f"Documents file not found: {DOCUMENTS_FILE}"
            )

        with open(
                DOCUMENTS_FILE,
                "r",
                encoding="utf-8"
        ) as file:

            self.documents = json.load(file)

        if not isinstance(self.documents, list):
            raise ValueError(
                "documents.json must contain a JSON array."
            )

        return self.documents

    def get_documents(self):
        """
        Return all documents.
        """

        if not self.documents:
            self.load_documents()

        return self.documents

    def add_document(self, document):
        """
        Add a new document to documents.json.
        """

        required_fields = [
            "title",
            "content"
        ]

        for field in required_fields:

            if field not in document:
                raise ValueError(
                    f"Missing field: {field}"
                )

        documents = self.get_documents()

        new_id = max(
            [doc.get("id", 0) for doc in documents],
            default=0
        ) + 1

        new_document = {
            "id": new_id,
            "title": document["title"],
            "content": document["content"]
        }

        documents.append(new_document)

        with open(
                DOCUMENTS_FILE,
                "w",
                encoding="utf-8"
        ) as file:

            json.dump(
                documents,
                file,
                indent=4,
                ensure_ascii=False
            )

        self.documents = documents

        return new_document


document_service = DocumentService()