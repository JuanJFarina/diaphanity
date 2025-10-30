class AgentPrompt:
    def __init__(self, system_prompt: str, user_prompt: str):
        self.content = f"{system_prompt}\n\n{user_prompt}"

    def add_memory(self, messages: str) -> None:
        self.content += f"\n\nMemory:\n{messages}"

    def add_tools(self, tools: str) -> None:
        self.content += f"\n\nTools:\n{tools}"
