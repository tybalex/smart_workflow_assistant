from typing import Dict, List, Any, Optional, Callable
from pydantic import BaseModel


class Function(BaseModel):
    """Represents a function in the registry"""
    name: str
    description: str
    category: str
    parameters: Dict[str, str]
    required_credentials: List[str]
    
    class Config:
        arbitrary_types_allowed = True


class FunctionListResponse(BaseModel):
    """Response model for listing functions"""
    functions: List[Function]
    total: int


class FunctionDetailResponse(BaseModel):
    """Response model for a single function"""
    function: Function


class CategoryResponse(BaseModel):
    """Response model for categories"""
    categories: List[str]


class SearchResponse(BaseModel):
    """Response model for search results"""
    functions: List[Function]
    total: int
    query: str


class FunctionExecuteRequest(BaseModel):
    """Request model for executing a function"""
    parameters: Dict[str, Any]
    
    class Config:
        json_schema_extra = {
            "example": {
                "parameters": {
                    "sheet_id": "abc123",
                    "range": "Sheet1!A1",
                    "values": [["Name", "Email"], ["John", "john@example.com"]]
                }
            }
        }


class FunctionExecuteResponse(BaseModel):
    """Response model for function execution"""
    function_name: str
    result: str
    success: bool
    error: Optional[str] = None

