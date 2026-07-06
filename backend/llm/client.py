 
def generate_response(prompt: str) -> str:
    prompt_lower = prompt.lower()
    
    if "why" in prompt_lower and "water" in prompt_lower:
        return "Water was prioritized because it has a 99% infrastructure gap - nearly complete shortage. Clean water prevents disease and is the foundation for all development."
    
    if "why" in prompt_lower and "electricity" in prompt_lower:
        return "Electricity enables schools, hospitals, water pumping, and businesses. Your city showed 99% gap in coverage, so it received the largest allocation."
    
    if "why" in prompt_lower and "transport" in prompt_lower:
        return "Transport connects people to jobs and services, but is less critical than water/electricity. It's prioritized in Phase 3 after essential infrastructure is in place."
    
    if "why" in prompt_lower:
        return "The allocation is based on infrastructure gap analysis. Sectors with larger gaps get larger budgets because they represent critical shortages."
    
    return "City planning tool ready. Ask about budget allocation, priorities, or development phases."
 