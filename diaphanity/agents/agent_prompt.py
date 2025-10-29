from pydantic import BaseModel

class AgentPrompt(BaseModel):
    system_prompt: str
    user_prompt: str

    def add_memory(self, messages: str) -> None:
        pass  # Implementation for adding memory messages

    def add_tools(self, tools: str) -> None:
        pass  # Implementation for adding tool information
