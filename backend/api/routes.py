
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from backend.core.engine import AgentEngine
from backend.core.memory import MemoryEngine
from backend.core.scoring import ScoringEngine
from backend.llm.client import generate_response
from backend.tools.calculator import calculator_tool
from backend.tools.web_search import web_search_tool
 
router = APIRouter()
 
TOOLS = {
    "calculator": calculator_tool,
    "web_search": web_search_tool
}
 
agent = AgentEngine(generate_response, TOOLS)
memory = MemoryEngine()
scoring = ScoringEngine()
 
 
class ChatRequest(BaseModel):
    user_id: str = "default"
    message: str
 
 
@router.post("/plan")
async def city_plan(payload: dict):
    user_id = payload.get("user_id", "default")
    score_result = scoring.score_plan(payload)
 
    plan_text = f"""CITY DEVELOPMENT PLAN
 
Total Budget: ${score_result['budget']:,}
Population: {score_result['population']:,}
 
ALLOCATION:
Healthcare: {score_result['allocation_percentages'].get('healthcare', 0):.1f}%
Water: {score_result['allocation_percentages'].get('water', 0):.1f}%
Electricity: {score_result['allocation_percentages'].get('electricity', 0):.1f}%
Housing: {score_result['allocation_percentages'].get('housing', 0):.1f}%
Transport: {score_result['allocation_percentages'].get('transport', 0):.1f}%
Education: {score_result['allocation_percentages'].get('education', 0):.1f}%
 
PHASE 1 (Years 1-2): Foundation
- Healthcare: Establish 15 primary health centers
- Water: Build treatment plants, reach 80% coverage
- Electricity: Install renewable grids, 95%+ coverage
- Transport: Build 80km primary roads
 
PHASE 2 (Years 3-4): Social Infrastructure  
- Housing: 8,000 affordable units
- Education: 40 new schools
- Sanitation: 500km sewage network
 
PHASE 3 (Years 5+): Quality of Life
- Transport: 500 bus fleet + light rail
- Green Space: 25 parks (750 acres)
- Smart City: Digital systems
 
SUCCESS METRICS:
- Healthcare distance: 15km → 8km
- Water coverage: 35% → 80%
- Electricity access: 95% → 100%
- Jobs created: 5,000+
- HDI improvement: +0.15 points"""
 
    memory.update_memory(user_id, f"Generated plan for population {score_result['population']}", plan_text)
 
    return {
        "allocation_percentages": score_result["allocation_percentages"],
        "final_allocation": score_result["final_allocation"],
        "plan": plan_text,
        "gaps": score_result["sector_gaps"],
    }
 
 
@router.post("/chat")
async def chat(payload: ChatRequest):
    result = await agent.run_once(payload.user_id, payload.message)
    return result
 
 
@router.post("/chat/stream")
async def chat_stream(payload: ChatRequest):
    async def event_stream():
        async for token in agent.run(payload.user_id, payload.message):
            yield f"data: {token}\n\n"
    return StreamingResponse(event_stream(), media_type="text/event-stream")
 