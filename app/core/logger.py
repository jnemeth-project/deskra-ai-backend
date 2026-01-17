import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("demo_logs/chat_logs.json")


def log_chat_event(
    session_id: str,
    user_message: str,
    response: str,
    action: str,
    confidence: float,
    environment: str,
    data_class: str
):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "user_message": user_message,
        "response": response,
        "action": action,
        "confidence": confidence,
        "environment": environment,
        "data_class": data_class
    }

    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
