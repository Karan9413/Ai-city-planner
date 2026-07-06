import json
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "memory_store.json")
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "memory.json")


class MemoryEngine:

    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        if not os.path.exists(DB_PATH):
            with open(DB_PATH, "w") as f:
                json.dump({}, f)

    def _load(self):
        with open(DB_PATH, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(DB_PATH, "w") as f:
            json.dump(data, f, indent=2)

    def update_memory(self, user_id, message, response):
        data = self._load()
        if user_id not in data:
            data[user_id] = []
        data[user_id].append({"user": message, "assistant": response})
        self._save(data)

    def get_relevant_memory(self, user_id, query, k=5):
        """Simple keyword-overlap recall instead of vector search — fast, no extra deps."""
        data = self._load()
        history = data.get(user_id, [])
        if not history:
            return []

        query_words = set(query.lower().split())
        scored = []
        for turn in history:
            turn_words = set(turn["user"].lower().split())
            overlap = len(query_words & turn_words)
            scored.append((overlap, turn))

        scored.sort(key=lambda x: x[0], reverse=True)
        # fall back to most recent turns if nothing overlaps
        top = [t for score, t in scored if score > 0][:k]
        if not top:
            top = history[-k:]
        return top