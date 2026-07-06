from dataclasses import dataclass
from typing import List


@dataclass
class PlanStep:
    action: str   # "llm" or "tool"
    input: str
    tool: str = None


class Planner:
    def create_plan(self, intent: str, message: str) -> List[PlanStep]:
        if intent == "calculation":
            return [PlanStep(action="tool", input=message, tool="calculator")]
        if intent == "search":
            return [PlanStep(action="tool", input=message, tool="web_search")]
        if intent == "greeting":
            return [PlanStep(action="llm", input="Respond naturally and briefly to this greeting: " + message)]
        # "explanation" and any fallback
        return [PlanStep(action="llm", input=message)]