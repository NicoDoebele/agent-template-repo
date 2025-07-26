"""Search agent core implementation.

This module contains the main SearchAgent class that provides intelligent
search capabilities using OpenAI and LangGraph.
"""

from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.agents.search_agent.prompts import search_agent_prompt
from app.agents.search_agent.tools import search_agent_tools
from app.core.config import get_settings
from app.agents.base import BaseAgent


class SearchAgent(BaseAgent):
    """A search agent that uses OpenAI and LangGraph for intelligent search operations.
    
    This agent provides web search capabilities through LangGraph tools and
    uses OpenAI's language models for processing and responding to queries.
    """

    def __init__(self):
        """Initialize the search agent with OpenAI LLM and LangGraph executor."""
        settings = get_settings()
        self.llm = ChatOpenAI(api_key=settings.openai_api_key,
                              model=settings.model_name)

        self.agent = create_react_agent(model=self.llm,
                                        tools=search_agent_tools,
                                        prompt=search_agent_prompt,
                                        debug=settings.verbose)

    async def run(self, user_input: str) -> str:
        """Execute the search agent's main logic.
        
        Args:
            user_input: The user's search query or question.
            
        Returns:
            The agent's response as a string.
        """

        result = await self.agent.ainvoke(
            {"messages": [HumanMessage(content=user_input)]})

        return str(result["messages"][-1].content)
