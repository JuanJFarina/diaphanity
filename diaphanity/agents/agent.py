from pydantic import BaseModel
from uuid import UUID, uuid4
from diaphanity.llms import LLM, LLMConfig
from .agent_config import AgentConfig
from .agent_prompt import AgentPrompt
from .agent_store import AgentStore
from .agent_memory import AgentMemory
from diaphanity.tools import Toolkit


class Agent(BaseModel):
    llm: LLM[LLMConfig]
    name: str = "Base Agent"
    id: UUID = uuid4()
    config: AgentConfig = AgentConfig()
    store: AgentStore = AgentStore()
    memory: AgentMemory = AgentMemory()
    tools: Toolkit = Toolkit()

    async def generate(self, prompt: str) -> str:
        agent_prompt = AgentPrompt(
            system_prompt=self.config.system_prompt, user_prompt=prompt
        )
        if self.config.with_memory:
            agent_prompt.add_memory(self.memory.get_messages())
        if self.config.with_tools:
            agent_prompt.add_tools(self.tools.get_tools())
        return await self.llm.call(agent_prompt.content)
