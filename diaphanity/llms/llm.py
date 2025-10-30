from typing import TypeVar, Generic
from pydantic import BaseModel
import aiohttp
from .base_config import LLMConfig


T = TypeVar("T", bound=LLMConfig)


class LLM(Generic[T], BaseModel):
    endpoint: str
    api_key: str
    config: T

    async def call(self, prompt: str) -> str:
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "prompt": prompt,
                **self.config.model_dump(),
            }
            async with session.post(
                self.endpoint, json=payload, headers=headers
            ) as response:
                return await response.json()

    async def raw_call(self, headers: dict[str, str], payload: dict[str, str]) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.endpoint, json=payload, headers=headers
            ) as response:
                return await response.json()
