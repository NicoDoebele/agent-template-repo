"""Search agent core implementation.

This module contains the main SearchAgent class that provides intelligent
search capabilities using OpenAI and LangChain.
"""

from langchain_openai import OpenAI
from langchain.agents import AgentExecutor, initialize_agent, AgentType
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.agents.search_agent.prompts import search_agent_prompt
from app.agents.search_agent.tools import search_agent_tools
from app.core.config import get_settings
from app.agents.base import BaseAgent


class SearchAgent(BaseAgent):
    """A search agent that uses OpenAI and LangChain for intelligent search operations.
    
    This agent provides web search capabilities through LangChain tools and
    uses OpenAI's language models for processing and responding to queries.
    """

    def __init__(self):
        """Initialize the search agent with OpenAI LLM and LangChain executor."""
        settings = get_settings()
        self.llm = OpenAI(api_key=settings.openai_api_key)

        self.agent_executor = initialize_agent(
            tools=search_agent_tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=settings.verbose,
            handle_parsing_errors=True,
            agent_kwargs={"system_message": search_agent_prompt})

    async def run(self, user_input: str) -> str:
        """Execute the search agent's main logic.
        
        Args:
            user_input: The user's search query or question.
            
        Returns:
            The agent's response as a string.
        """
        result = await self.agent_executor.ainvoke({"input": user_input})
        return result["output"]
