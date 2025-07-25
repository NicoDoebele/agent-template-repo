"""Search API endpoints for the agent-template-repo application."""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.agents.search_agent.core import SearchAgent

router = APIRouter()


class SearchRequest(BaseModel):
    """Request model for search operations.
    
    Attributes:
        query: The search query string.
        max_results: Maximum number of results to return (default: 10).
    """
    query: str
    max_results: Optional[int] = 10


class SearchResponse(BaseModel):
    """Response model for search operations.
    
    Attributes:
        result: The search result string.
        query: The original search query.
    """
    result: str
    query: str


@router.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    """
    Perform a search using the search agent.
    
    Args:
        request: SearchRequest containing the query and optional max_results
        
    Returns:
        SearchResponse with the search result
        
    Raises:
        HTTPException: If the search operation fails.
    """
    try:
        # Initialize the search agent
        search_agent = SearchAgent()

        # Run the search
        result = await search_agent.run(request.query)

        return SearchResponse(result=result, query=request.query)
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Search failed: {str(e)}") from e


@router.get("/search/health")
async def search_health():
    """Health check for the search endpoint.
    
    Returns:
        A dictionary indicating the search service is healthy.
    """
    return {"status": "search service healthy"}
