class Executor:
    def __init__(self, llm, tools: dict):
        self.llm = llm          # plain sync function
        self.tools = tools

    async def run_step(self, step):
        if step.action == "tool":
            tool = self.tools.get(step.tool)
            if tool:
                result = tool(step.input)
                yield str(result)
                return
            yield f"[Tool '{step.tool}' not found]"
            return

        if step.action == "llm":
            # Call sync function directly (no await)
            result = self.llm(step.input)
            yield result