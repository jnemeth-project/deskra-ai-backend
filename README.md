# Deskra Support Agent

A production-grade AI customer support agent built with Python and FastAPI. Features a modular, offline-first architecture with session memory, knowledge base integration, and extensible adapters for Jira and Zendesk.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Overview

Deskra is an **offline-first, modular AI support agent** designed to demonstrate production-grade architecture patterns without requiring external API keys or collecting real user data.

**Key Features:**
- 🧠 **Decision Engine** — Routes queries through intent classification and confidence scoring
- 💾 **Session Memory** — Maintains conversation context across interactions
- 📚 **Knowledge Base** — Structured Q&A retrieval system
- 🔌 **Adapter Pattern** — Ready for Jira, Zendesk, and custom integrations
- 🔒 **Offline-First** — No external APIs required, fully compliant by design
- 📊 **Audit Logging** — Every interaction logged for analysis and compliance

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│                           DESKRA CORE                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐          │
│   │   Frontend  │────▶│   FastAPI   │────▶│  Decision   │          │
│   │  (React UI) │     │   Gateway   │     │   Engine    │          │
│   └─────────────┘     └─────────────┘     └──────┬──────┘          │
│                                                   │                 │
│                    ┌──────────────────────────────┼────────────┐    │
│                    │                              │            │    │
│                    ▼                              ▼            ▼    │
│            ┌─────────────┐              ┌─────────────┐ ┌──────────┐│
│            │  Knowledge  │              │   Mock LLM  │ │  Memory  ││
│            │    Base     │              │   Client    │ │  Store   ││
│            └─────────────┘              └─────────────┘ └──────────┘│
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                        ADAPTERS                              │  │
│   │    ┌─────────┐    ┌─────────┐    ┌─────────┐               │  │
│   │    │  Jira   │    │ Zendesk │    │ OpenAI  │               │  │
│   │    └─────────┘    └─────────┘    └─────────┘               │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure
```
deskra_support_agent/
├── app/
│   ├── adapters/           # External service integrations
│   │   ├── jira.py         # Jira ticket integration
│   │   └── zendesk.py      # Zendesk integration
│   │
│   ├── ai/                 # AI/ML components
│   │   └── openai_client.py    # LLM client (mock/real)
│   │
│   ├── api/                # FastAPI route handlers
│   │   ├── chat.py         # POST /chat/message endpoint
│   │   └── health.py       # Health check endpoint
│   │
│   ├── config/             # Configuration management
│   │   └── settings.py     # Pydantic settings with .env support
│   │
│   ├── core/               # Business logic layer
│   │   ├── decision.py     # Core decision engine
│   │   ├── llm.py          # Mock LLM implementation
│   │   ├── memory.py       # Session history management
│   │   ├── logger.py       # Audit logging
│   │   ├── intent.py       # Intent classification (placeholder)
│   │   ├── confidence.py   # Confidence scoring (placeholder)
│   │   ├── policies.py     # Business rules (placeholder)
│   │   └── audit.py        # Compliance auditing (placeholder)
│   │
│   ├── kb/                 # Knowledge Base
│   │   └── knowledge_base.py   # Structured Q&A store
│   │
│   ├── logging/            # Structured logging utilities
│   │
│   ├── models/             # Pydantic data models
│   │   └── schemas.py      # Request/Response schemas
│   │
│   ├── rag/                # RAG components (future)
│   │   ├── embeddings.py   # Vector embeddings
│   │   └── retriever.py    # Document retrieval
│   │
│   ├── tests/              # Test suite
│   │
│   └── main.py             # FastAPI application entry point
│
├── demo_logs/              # Session storage (JSON files)
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.14+
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/jnemeth-project/deskra-support-agent.git
cd deskra-support-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Server
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000`

### API Documentation

Once running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 📡 API Reference

### Chat Endpoint
```http
POST /chat/message
Content-Type: application/json
```

**Request Body:**
```json
{
  "session_id": "unique-session-id",
  "message": "How do I reset my password?",
  "channel": "web",
  "metadata": {}
}
```

**Response:**
```json
{
  "response": "To reset your password, go to the login page and click 'Forgot Password'...",
  "confidence": 0.9,
  "action": "respond"
}
```

### Supported Channels

| Channel | Description |
|---------|-------------|
| `web` | Web chat interface |
| `widget` | Embedded widget |
| `jira` | Jira integration |
| `zendesk` | Zendesk integration |

### Action Types

| Action | Description |
|--------|-------------|
| `respond` | Normal response to user |
| `clarify` | Request more information |
| `escalate` | Escalate to human agent |

---

## 🧠 Core Components

### Decision Engine (`core/decision.py`)

The brain of the system. Processes user input through:
1. Session history retrieval
2. Mock LLM response generation
3. Action determination (respond/clarify/escalate)
4. Confidence scoring
```python
def decide_response(user_message: str, session_history: List[Dict]) -> Tuple[str, ChatAction, float]:
    # Returns: (response_text, action, confidence)
```

### Memory System (`core/memory.py`)

Session-based conversation storage:
- Each session stored as a separate JSON file
- Maintains full conversation history
- Enables context-aware responses

### Knowledge Base (`kb/knowledge_base.py`)

Structured Q&A retrieval:
- Pre-defined answers for common questions
- Confidence scores per answer
- Easily extensible

---

## ⚙️ Configuration

Create a `.env` file in the project root:
```env
APP_NAME=Deskra Core API
DEBUG=true
```

Configuration is managed via Pydantic Settings (`config/settings.py`).

---

## 🧪 Testing
```bash
# Run tests
pytest app/tests/

# With coverage
pytest --cov=app app/tests/
```

---

## 🔮 Future Enhancements

The architecture is designed for easy extension:

- [ ] **Real LLM Integration** — Swap MockLLMClient for OpenAI/Anthropic
- [ ] **RAG Pipeline** — Vector embeddings + semantic retrieval
- [ ] **Intent Classification** — ML-based intent detection
- [ ] **Confidence Calibration** — Dynamic confidence thresholds
- [ ] **Policy Engine** — Business rules and escalation policies
- [ ] **Analytics Dashboard** — Conversation insights and metrics

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Janka Nemeth**

- GitHub: [@jnemeth-project](https://github.com/jnemeth-project)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/janka-n%C3%A9meth-aa3999163/)

---

<p align="center">
  Built with ❤️ as a demonstration of production-grade AI architecture
</p>