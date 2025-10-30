from pydantic import BaseModel
from .tool import Tool


class Toolkit(BaseModel):
    tools: list[Tool] = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def get_tools(self) -> str:
        return "\n".join([tool.name for tool in self.tools])
