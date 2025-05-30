# GCP AI Blueprint

A cloud-native GenAI demo project showcasing multi-agent intelligence using Google Cloud Platform. Built to demonstrate practical GCP architecture and AI tooling, this project simulates an enterprise assistant with modular, scalable design.

---

## ✨ Features

- Vertex AI for LLM, summarization, classification, and embedding generation
- Multi-agent routing (IT, HR, General agents)
- Document ingestion and RAG:
  - Upload and parse documents
  - Generate text embeddings using Vertex AI
  - Store in a vector DB (Matching Engine or PGVector) for semantic search and agent grounding
- Cloud-native stack:
  - Cloud Run (containerized backend)
  - Firestore (context and state storage)
  - Pub/Sub (event-based messaging)
  - Cloud Functions (agent glue logic)
- Optional support for Agent Development Kit (ADK), Agentspace, or Agent2Agent Protocol
- Simple CLI or web frontend
- Dependency management via Astral UV

---

## 🧠 Use Case

Users interact with a GenAI-powered assistant. Input is routed to specialized agents for task-specific responses (IT, HR, or General), simulating a real-world enterprise scenario.

In addition, documents can be ingested into a vector database. These documents are chunked, embedded with Vertex AI, and stored for contextual grounding using Retrieval-Augmented Generation (RAG). Agents retrieve relevant information from these embeddings to enhance response quality.

---

## 🛠️ Tech Stack

- Python (managed with [uv](https://astral.sh/uv/))
- Vertex AI (LLMs + Embeddings)
- Cloud Run
- Firestore
- Pub/Sub
- Cloud Functions
- Terraform (for infrastructure as code)
- Vector DB (Vertex AI Matching Engine or PGVector)

---

## 📦 Project Structure

```text
gcp_ai_blueprint/
├── agents/            # Domain-specific agent logic (IT, HR, General)
├── backend/           # Python app for routing, Vertex AI, etc.
├── ingestion/         # Document ingestion: parsing, embedding, vector upload
├── frontend/          # Optional CLI or web interface
├── infra/             # Terraform config for GCP resources
├── .gcloudignore      # Ignore file for gcloud CLI
├── .gitignore         # Git ignore rules
├── Dockerfile         # Container build for Cloud Run
├── README.md          # Project overview
└── pyproject.toml     # UV-managed Python dependencies
