from abc import ABC, abstractmethod
from diaphanity.agents import AgentPrompt


class LLM(ABC):
    @abstractmethod
    async def call(self, prompt: AgentPrompt | str) -> str: ...
