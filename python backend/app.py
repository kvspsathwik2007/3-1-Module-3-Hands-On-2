from flask import Flask, jsonify
from flask_cors import CORS

from config.config import (
    is_groq_configured,
    GROQ_MODEL
)

from routes.search_routes import search_bp


app = Flask(__name__)

# Enable CORS
CORS(app)


# Register API routes
app.register_blueprint(
    search_bp
)


@app.route("/", methods=["GET"])
def home():

    return jsonify(
        {
            "status": "running",
            "message": "Document Retrieval API is running",
            "service": "Retrieval System Lab",
            "embedding": "Sentence Transformers",
            "retrieval": "Cosine Similarity",
            "groq_configured": is_groq_configured(),
            "groq_model": GROQ_MODEL
        }
    )


@app.route("/health", methods=["GET"])
def health():

    return jsonify(
        {
            "status": "healthy",
            "backend": "Flask",
            "groq_configured": is_groq_configured()
        }
    )


@app.errorhandler(404)
def not_found(error):

    return jsonify(
        {
            "error": True,
            "message": "Endpoint not found."
        }
    ), 404


@app.errorhandler(500)
def internal_error(error):

    return jsonify(
        {
            "error": True,
            "message": "Internal server error."
        }
    ), 500


if __name__ == "__main__":

    print("=" * 60)
    print("DOCUMENT RETRIEVAL LAB")
    print("=" * 60)
    print("Server: http://127.0.0.1:5000")
    print(
        f"Groq configured: {is_groq_configured()}"
    )
    print(
        f"Groq model: {GROQ_MODEL}"
    )
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )