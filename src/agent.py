"""
SpoonOS ReAct Agent - Crypto Price Analyzer

This agent uses SpoonOS SDK to analyze cryptocurrency prices and provide insights.
"""

import asyncio
import logging
import os
from typing import List, Optional

from spoon_ai.agents.spoon_react import SpoonReactAI
from spoon_ai.chat import ChatBot
from spoon_ai.tools import ToolManager
from spoon_toolkits import (
    GetTokenPriceTool,
    Get24hStatsTool,
    GetKlineDataTool,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_crypto_tools() -> List:
    """Create and return the list of crypto analysis tools."""
    tools = [
        GetTokenPriceTool(),
        Get24hStatsTool(),
        GetKlineDataTool(),
    ]
    return tools


def create_agent(
    name: str = "crypto_analyzer",
    max_steps: int = 10,
    llm_provider: str = None,
) -> SpoonReactAI:
    """
    Create a ReAct Agent for cryptocurrency analysis.

    Args:
        name: Agent name
        max_steps: Maximum steps for agent execution
        llm_provider: LLM provider to use ("openai" or "anthropic")

    Returns:
        Configured SpoonReactAI instance
    """
    tools = create_crypto_tools()

    # Use specified provider or read from environment
    # Default to deepseek (free credits for new users)
    provider = llm_provider or os.getenv("LLM_PROVIDER", "deepseek")
    logger.info(f"Using LLM provider: {provider}")

    # Create ChatBot with specified provider
    chatbot = ChatBot(llm_provider=provider)

    agent = SpoonReactAI(
        name=name,
        description="A cryptocurrency price analysis agent powered by SpoonOS",
        tools=tools,
        max_steps=max_steps,
        llm=chatbot,
    )

    logger.info(f"Created agent '{name}' with {len(tools)} tools")
    return agent


async def run_agent(agent: SpoonReactAI, query: str) -> str:
    """
    Run the agent with a given query.

    Args:
        agent: The SpoonReactAI instance
        query: User query to process

    Returns:
        Agent response
    """
    logger.info(f"Processing query: {query}")

    try:
        response = await agent.run(request=query)
        return response
    except Exception as e:
        logger.error(f"Agent execution failed: {e}")
        raise
