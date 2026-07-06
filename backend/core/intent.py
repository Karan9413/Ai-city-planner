
def detect_intent(message: str):
    msg = message.lower()
    
    if any(x in msg for x in ["search", "look up", "find"]):
        return "search"
    
    if any(x in msg for x in ["hi", "hello", "hey"]):
        return "greeting"
    
    return "explanation"