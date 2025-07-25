"""Base agent module providing the abstract base class for all agents."""

from abc import ABC, abstractmethod


class BaseAgent(ABC):  # pylint: disable=too-few-public-methods
    """Abstract base class for all agents in the system.
    
    This class defines the interface that all concrete agent implementations
    must follow. Agents are responsible for processing user input and
    returning appropriate responses.
    """

    @abstractmethod
    async def run(self, user_input: str) -> str:
        """Execute the agent's main logic.
        
        Args:
            user_input: The user's input string to process.
            
        Returns:
            The agent's response as a string.
        """
