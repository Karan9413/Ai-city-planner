from backend.core.intent import detect_intent
from backend.core.memory import MemoryEngine
from backend.core.profile import ProfileEngine
from backend.core.planner import Planner
from backend.core.executor import Executor


class AgentEngine:
    def __init__(self, llm, tools: dict):
        self.llm = llm
        self.tools = tools
        self.memory = MemoryEngine()
        self.profile = ProfileEngine()
        self.planner = Planner()
        self.executor = Executor(llm, tools)

    async def run(self, user_id: str, message: str):
        profile = self.profile.get_profile(user_id)
        relevant_memory = self.memory.get_relevant_memory(user_id, message)
        intent = detect_intent(message)
        plan = self.planner.create_plan(intent, message)

        final_response = ""
        for step in plan:
            async for output in self.executor.run_step(step):
                final_response += output
                yield output

        self.memory.update_memory(user_id, message, final_response)
        self.profile.update(user_id, message, final_response, intent)

    async def run_once(self, user_id: str, message: str) -> dict:
        """Non-streaming entry point used by /chat."""
        final_response = ""
        async for chunk in self.run(user_id, message):
            final_response += chunk
        return {"response": final_response}