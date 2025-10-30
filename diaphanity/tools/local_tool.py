from .tool import Tool
from collections.abc import Callable
from typing_extensions import Any

class LocalTool(Tool):
    func: Callable[..., Any]
