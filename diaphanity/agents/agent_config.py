from pydantic import BaseModel

class AgentConfig(BaseModel):
    system_prompt: str = "You are a helpful assistant."
    with_memory: bool = True
    with_tools: bool = True
