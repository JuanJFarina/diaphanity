from .base_config import LLMConfig


class OpenAIConfig(LLMConfig):
    max_tokens: int = 2048
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
