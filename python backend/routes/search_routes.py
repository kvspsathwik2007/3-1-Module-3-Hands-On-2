from flask import Blueprint, request, jsonify

from config.config import is_groq_configured

from services.document_service import document_service

from services.retrieval_service import retrieval_service


search_bp = Blueprint(
    "search",
    __name__
)


@search_bp.route("/search", methods=["POST"])
def search():

    try:

        if not request.is_json:
            return jsonify({
                "error": True,
                "message": "Request must contain JSON."
            }), 400

        data = request.get_json()

        if not data:
            return jsonify({
                "error": True,
                "message": "Request body cannot be empty."
            }), 400

        query = data.get("query")

        if query is None:
            return jsonify({
                "error": True,
                "message": "Missing query."
            }), 400

        query = query.strip()

        if not query:
            return jsonify({
                "error": True,
                "message": "Query cannot be empty."
            }), 400

        results = retrieval_service.search(query)

        return jsonify({
            "error": False,
            "query": query,
            "results": results,
            "count": len(results),
            "groq_configured": is_groq_configured()
        }), 200

    except Exception as error:

        print(f"Search error: {error}")

        return jsonify({
            "error": True,
            "message": str(error)
        }), 500


@search_bp.route("/documents", methods=["GET"])
def get_documents():

    try:

        documents = document_service.get_documents()

        return jsonify({
            "error": False,
            "count": len(documents),
            "documents": documents
        }), 200

    except Exception as error:

        return jsonify({
            "error": True,
            "message": str(error)
        }), 500


@search_bp.route("/documents", methods=["POST"])
def add_document():

    try:

        if not request.is_json:
            return jsonify({
                "error": True,
                "message": "Request must contain JSON."
            }), 400

        data = request.get_json()

        document = document_service.add_document(data)

        return jsonify({
            "error": False,
            "message": "Document added successfully.",
            "document": document,
            "note": "Run /rebuild-index before searching."
        }), 201

    except Exception as error:

        return jsonify({
            "error": True,
            "message": str(error)
        }), 400


@search_bp.route("/rebuild-index", methods=["POST"])
def rebuild_index():

    try:

        result = retrieval_service.build_index()

        return jsonify({
            "error": False,
            "message": "Embedding index rebuilt successfully.",
            **result
        }), 200

    except Exception as error:

        return jsonify({
            "error": True,
            "message": str(error)
        }), 500