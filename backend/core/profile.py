class ProfileEngine:
    def __init__(self):
        self.profiles = {}

    def get_profile(self, user_id: str):
        if user_id not in self.profiles:
            self.profiles[user_id] = {
                "level": 0.5,
                "verbosity": 0.5,
                "technical_interest": 0.3,
                "interaction_count": 0
            }
        return self.profiles[user_id]

    def update(self, user_id: str, message: str, response: str, intent: str):
        profile = self.get_profile(user_id)

        profile["interaction_count"] += 1

        # SIMPLE LEARNING LOGIC (we will upgrade later to AI-based learning)
        if "code" in message.lower():
            profile["technical_interest"] = min(1.0, profile["technical_interest"] + 0.05)

        if len(message) > 100:
            profile["verbosity"] = min(1.0, profile["verbosity"] + 0.05)

        if intent == "question":
            profile["level"] = min(1.0, profile["level"] + 0.02)

        self.profiles[user_id] = profile
        return profile