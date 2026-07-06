from core.intent import detect_intent
from core.memory import MemoryEngine
from core.profile import ProfileEngine
from core.prompt import build_prompt

from core.planner import Planner
from core.executor import Executor
from backend.core.intent import detect_intent
from backend.core.memory import MemoryEngine
from backend.core.profile import ProfileEngine
from backend.core.planner import Planner
from backend.core.executor import Executor

memory = MemoryEngine()
profile_engine = ProfileEngine()
planner = Planner()


def run_agent(user_id: str, message: str):
def run_agent(user_id: str, message: str, llm, tools: dict):

    # 1. Load memory + profile
    profile = memory.get_profile(user_id)

    profile = memory.get_profile(user_id) if hasattr(memory, "get_profile") else profile_engine.get_profile(user_id)
    # 2. Intent detection (ML)
    intent = detect_intent(message)

    # 3. PLANNING STEP (CRITICAL)
    plan_result = plan(message, intent, profile)

    plan = planner.create_plan(intent, message)
    # 4. EXECUTION STEP (tools OR LLM)
    response = execute(plan_result, message, profile)

    executor = Executor(llm, tools)
    response = ""
    for step in plan:
        for output in executor.run_step_sync(step):
            response += output
    # 5. UPDATE MEMORY
    memory.update_memory(user_id, message, response, intent)
    memory.update_memory(user_id, message, response)

    # 6. PROFILE LEARNING (adaptive behavior)
    profile = update_profile(profile, message, intent)
    profile_engine.update(user_id, message, response, intent)

    return {
        "response": response,
        "intent": intent,
        "profile": profile,
        "trace": plan_result
        "trace": plan,
    }