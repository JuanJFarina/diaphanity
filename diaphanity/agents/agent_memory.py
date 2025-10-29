from pydantic import BaseModel

class AgentMemory(BaseModel):
    messages: list[str] = []

    def add_message(self, message: str):
        self.messages.append(message)

    def get_messages(self) -> str:
        return '\n'.join(self.messages)
