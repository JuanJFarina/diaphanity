from pydantic import BaseModel

class Toolkit(BaseModel):
    tools: list[str] = []

    def add_tool(self, tool: str):
        self.tools.append(tool)

    def get_tools(self) -> str:
        return '\n'.join(self.tools)
