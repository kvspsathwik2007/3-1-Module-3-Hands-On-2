# 3-1 Module 3 Hands-On 2 — Retrieval System Lab

## 📌 Project Title

**Retrieval System Lab – Document Retrieval Using Embeddings**

## 📖 Overview

This project implements a document retrieval system that searches a collection of documents using **AI-generated vector embeddings** and **cosine similarity**.

The project demonstrates how a mobile application can communicate with a Python Flask backend to perform semantic document retrieval.

Instead of relying on simple keyword matching, the system converts the query and documents into vector embeddings and compares them using cosine similarity to identify the most relevant documents.

---

## 🎯 Objective

The main objective of this hands-on project is to understand and implement a basic **semantic retrieval system using embeddings**.

The application allows users to:

- Enter a natural-language search query
- Send the query from an Android application
- Generate an embedding for the query
- Compare the query embedding with document embeddings
- Calculate cosine similarity
- Retrieve the top relevant documents
- Display similarity scores in the Android application

---

## 🏗️ Architecture

```text
┌─────────────────────────────┐
│       Android App           │
│        Kotlin + XML         │
└──────────────┬──────────────┘
               │
               │ HTTP REST API
               ▼
┌─────────────────────────────┐
│       Flask Backend         │
│          Python             │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Sentence Transformers    │
│     all-MiniLM-L6-v2        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Vector Embeddings        │
│      + Cosine Similarity    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Top K Documents         │
│       JSON Response         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Android UI            │
│   Search Results + Score    │
└─────────────────────────────┘
🛠️ Technologies Used
Android
Kotlin
XML
Android Studio
Material Design
RecyclerView
Retrofit
Gson
Kotlin Coroutines
Backend
Python
Flask
Flask-CORS
NumPy
Sentence Transformers
Groq API
Embedding Model
all-MiniLM-L6-v2
Similarity Algorithm
Cosine Similarity
📂 Project Structure
31MODULE3HANDSON2/
│
├── app/
│   └── src/
│       └── main/
│           ├── java/
│           │   └── com/example/a3_1module_3handson2/
│           │       ├── model/
│           │       │   ├── SearchRequest.kt
│           │       │   ├── SearchResponse.kt
│           │       │   └── DocumentResult.kt
│           │       │
│           │       ├── network/
│           │       │   ├── ApiService.kt
│           │       │   └── RetrofitClient.kt
│           │       │
│           │       ├── ui/
│           │       │   └── SearchAdapter.kt
│           │       │
│           │       └── MainActivity.kt
│           │
│           └── res/
│               ├── drawable/
│               ├── layout/
│               ├── values/
│               └── values-night/
│
└── python backend/
    ├── app.py
    ├── requirements.txt
    ├── generate_embeddings.py
    │
    ├── config/
    │   ├── __init__.py
    │   └── config.py
    │
    ├── routes/
    │   ├── __init__.py
    │   └── search_routes.py
    │
    ├── services/
    │   ├── __init__.py
    │   ├── embedding_service.py
    │   ├── document_service.py
    │   └── retrieval_service.py
    │
    ├── utils/
    │   ├── __init__.py
    │   └── similarity.py
    │
    └── data/
        └── documents.json
🔍 How It Works
1. User enters a query

Example:

machine learning
2. Android sends the request
POST /search

Request:

{
  "query": "machine learning"
}
3. Backend generates the query embedding

The query is converted into a numerical vector using:

all-MiniLM-L6-v2
4. Document embeddings are compared

The system calculates cosine similarity between the query vector and document vectors.

5. Results are ranked

Documents are sorted according to their similarity scores.

6. Top results are returned

The backend returns the top 3 relevant documents by default.

7. Android displays the results

The application displays:

Document title
Similarity score
Document content
🌐 API Endpoints
Method	Endpoint	Description
GET	/	Backend information
GET	/health	Health check
POST	/search	Search documents
GET	/documents	Get documents
POST	/documents	Add a document
POST	/rebuild-index	Rebuild embedding index
🚀 Running the Backend

Open PowerShell inside the backend directory.

Create virtual environment
python -m venv venv
Activate virtual environment
.\venv\Scripts\Activate.ps1
Install dependencies
pip install -r requirements.txt
Generate embeddings
python generate_embeddings.py
Start Flask server
python app.py

The backend runs on:

http://127.0.0.1:5000/
📱 Android Emulator Configuration

For the Android Emulator, use:

http://10.0.2.2:5000/

10.0.2.2 maps the Android Emulator to the host computer's localhost.

For a physical Android device, use the computer's local network IP address instead.

🔐 API Key Security

The Groq API key is stored only in the backend environment.

Example:

GROQ_API_KEY=YOUR_API_KEY
GROQ_MODEL=openai/gpt-oss-20b
TOP_K=3

The .env file should not be committed to GitHub.

Make sure .gitignore contains:

.env
venv/
__pycache__/
*.pyc
*.npy
🧪 Example Queries

Try searching for:

machine learning
deep learning
natural language processing
computer vision
database management
python programming
👨‍🏫 Mentor

Kanoj Kumar Chavallam

📚 Hands-On Information

Program: B.Tech – AIML

Semester: 3-1

Module: Module 3

Hands-On: Hands-On 2

Project: Retrieval System Lab – Document Retrieval Using Embeddings

👨‍💻 Developer

Sathwik

📌 Learning Outcomes

Through this hands-on project, the following concepts were implemented:

REST API communication
Android–Flask integration
Vector embeddings
Semantic document retrieval
Cosine similarity
Top-K retrieval
Sentence Transformers
Retrofit networking
JSON request/response handling
Python Flask backend development
Secure API-key management
⭐ Conclusion

This project demonstrates a complete end-to-end semantic document retrieval workflow, connecting an Android application with a Python Flask backend and an embedding-based retrieval system.

It provides a practical foundation for understanding how modern AI-powered search and retrieval systems work.


### Git commands

From your project root:

```powershell
git init
git add .
git commit -m "feat: implement document retrieval system using embeddings"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main🛠️ Technologies Used
Android
Kotlin
XML
Android Studio
Material Design
RecyclerView
Retrofit
Gson
Kotlin Coroutines
Backend
Python
Flask
Flask-CORS
NumPy
Sentence Transformers
Groq API
Embedding Model
all-MiniLM-L6-v2
Similarity Algorithm
Cosine Similarity
📂 Project Structure
31MODULE3HANDSON2/
│
├── app/
│   └── src/
│       └── main/
│           ├── java/
│           │   └── com/example/a3_1module_3handson2/
│           │       ├── model/
│           │       │   ├── SearchRequest.kt
│           │       │   ├── SearchResponse.kt
│           │       │   └── DocumentResult.kt
│           │       │
│           │       ├── network/
│           │       │   ├── ApiService.kt
│           │       │   └── RetrofitClient.kt
│           │       │
│           │       ├── ui/
│           │       │   └── SearchAdapter.kt
│           │       │
│           │       └── MainActivity.kt
│           │
│           └── res/
│               ├── drawable/
│               ├── layout/
│               ├── values/
│               └── values-night/
│
└── python backend/
    ├── app.py
    ├── requirements.txt
    ├── generate_embeddings.py
    │
    ├── config/
    │   ├── __init__.py
    │   └── config.py
    │
    ├── routes/
    │   ├── __init__.py
    │   └── search_routes.py
    │
    ├── services/
    │   ├── __init__.py
    │   ├── embedding_service.py
    │   ├── document_service.py
    │   └── retrieval_service.py
    │
    ├── utils/
    │   ├── __init__.py
    │   └── similarity.py
    │
    └── data/
        └── documents.json
🔍 How It Works
1. User enters a query

Example:

machine learning
2. Android sends the request
POST /search

Request:

{
  "query": "machine learning"
}
3. Backend generates the query embedding

The query is converted into a numerical vector using:

all-MiniLM-L6-v2
4. Document embeddings are compared

The system calculates cosine similarity between the query vector and document vectors.

5. Results are ranked

Documents are sorted according to their similarity scores.

6. Top results are returned

The backend returns the top 3 relevant documents by default.

7. Android displays the results

The application displays:

Document title
Similarity score
Document content
🌐 API Endpoints
Method	Endpoint	Description
GET	/	Backend information
GET	/health	Health check
POST	/search	Search documents
GET	/documents	Get documents
POST	/documents	Add a document
POST	/rebuild-index	Rebuild embedding index
🚀 Running the Backend

Open PowerShell inside the backend directory.

Create virtual environment
python -m venv venv
Activate virtual environment
.\venv\Scripts\Activate.ps1
Install dependencies
pip install -r requirements.txt
Generate embeddings
python generate_embeddings.py
Start Flask server
python app.py

The backend runs on:

http://127.0.0.1:5000/
📱 Android Emulator Configuration

For the Android Emulator, use:

http://10.0.2.2:5000/

10.0.2.2 maps the Android Emulator to the host computer's localhost.

For a physical Android device, use the computer's local network IP address instead.

🔐 API Key Security

The Groq API key is stored only in the backend environment.

Example:

GROQ_API_KEY=YOUR_API_KEY
GROQ_MODEL=openai/gpt-oss-20b
TOP_K=3

The .env file should not be committed to GitHub.

Make sure .gitignore contains:

.env
venv/
__pycache__/
*.pyc
*.npy
🧪 Example Queries

Try searching for:

machine learning
deep learning
natural language processing
computer vision
database management
python programming
👨‍🏫 Mentor

Kanoj Kumar Chavallam

📚 Hands-On Information

Program: B.Tech – AIML

Semester: 3-1

Module: Module 3

Hands-On: Hands-On 2

Project: Retrieval System Lab – Document Retrieval Using Embeddings

👨‍💻 Developer

Sathwik

📌 Learning Outcomes

Through this hands-on project, the following concepts were implemented:

REST API communication
Android–Flask integration
Vector embeddings
Semantic document retrieval
Cosine similarity
Top-K retrieval
Sentence Transformers
Retrofit networking
JSON request/response handling
Python Flask backend development
Secure API-key management
⭐ Conclusion

This project demonstrates a complete end-to-end semantic document retrieval workflow, connecting an Android application with a Python Flask backend and an embedding-based retrieval system.

It provides a practical foundation for understanding how modern AI-powered search and retrieval systems work.


### Git commands

From your project root:

```powershell
git init
git add .
git commit -m "feat: implement document retrieval system using embeddings"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
