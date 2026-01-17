import json
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = BASE_DIR / "demo_logs"
LOG_DIR.mkdir(exist_ok=True)


def _session_file(session_id: str) -> Path:
    return LOG_DIR / f"{session_id}.json"


def get_session_history(session_id: str) -> List[Dict[str, str]]:
    file_path = _session_file(session_id)
    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_session_history(
    session_id: str,
    user_message: str,
    assistant_message: str
) -> None:
    history = get_session_history(session_id)

    history.append({
        "role": "user",
        "content": user_message
    })

    history.append({
        "role": "assistant",
        "content": assistant_message
    })

    with open(_session_file(session_id), "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
