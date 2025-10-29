from pydantic import BaseModel
from .base_llm import LLM
from diaphanity.agents import AgentPrompt


class OpenAI(LLM, BaseModel):
    api_key: str
    model_name: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1500
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0

    async def call(self, prompt: AgentPrompt | str) -> str:
        # Placeholder for the actual OpenAI API call
        # In a real implementation, you would use the OpenAI SDK to generate text
        return f"Generated text based on the prompt: {prompt}"
