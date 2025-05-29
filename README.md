# GCP AI Blueprint

A cloud-native GenAI demo project showcasing multi-agent intelligence using Google Cloud Platform. Built to demonstrate practical GCP architecture and AI tooling.

## ✨ Features

- **Vertex AI** for LLM, summarization, and classification
- **Multi-agent routing** (IT, HR, General agents)
- **Cloud-native stack**:
  - Cloud Run (containerized backend)
  - Firestore (context and state storage)
  - Pub/Sub (event-based messaging)
  - Cloud Functions (agent glue logic)
- Optionally includes Agent Development Kit (ADK), Agentspace, or Agent2Agent Protocol
- Simple CLI or web frontend
- Dependency management via **[Astral UV](https://astral.sh/blog/uv/)**

## 🧠 Use Case

Users interact with a GenAI-powered assistant. Input is routed to specialized agents for task-specific responses, simulating an enterprise AI experience.

## 🛠️ Tech Stack

- Python (managed with `uv`)
- Vertex AI
- Cloud Run
- Firestore
- Pub/Sub
- Cloud Functions
- Terraform (for infrastructure)

## 📦 Project Structure

```text
gcp_ai_blueprint/
├── agents/            # Domain-specific agent logic (IT, HR, General)
├── backend/           # Python app for routing, Vertex AI, etc.
├── frontend/          # Optional CLI or web interface
├── infra/             # Terraform config for GCP resources
├── .gcloudignore      # Ignore file for gcloud CLI
├── .gitignore         # Git ignore rules
├── Dockerfile         # Container build for Cloud Run
├── README.md          # Project overview
└── pyproject.toml     # UV-managed Python dependencies
