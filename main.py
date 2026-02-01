"""
SpoonOS ReAct Agent Demo - Entry Point

Usage:
    python main.py                    # Interactive mode
    python main.py "your query here"  # Single query mode
"""

import asyncio
import sys
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.agent import create_agent, run_agent


def print_banner():
    """Print welcome banner."""
    print("=" * 60)
    print("  SpoonOS ReAct Agent - Crypto Price Analyzer")
    print("=" * 60)
    print()


async def interactive_mode():
    """Run agent in interactive mode."""
    print_banner()
    print("Type your questions about cryptocurrency prices.")
    print("Type 'quit' or 'exit' to stop.\n")

    agent = create_agent()

    while True:
        try:
            query = input("\n[You]: ").strip()

            if not query:
                continue

            if query.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye!")
                break

            print("\n[Agent]: Thinking...\n")
            response = await run_agent(agent, query)
            print(f"[Agent]: {response}")

        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n[Error]: {e}")


async def single_query_mode(query: str):
    """Run agent with a single query."""
    print_banner()

    agent = create_agent()
    print(f"[Query]: {query}\n")
    print("[Agent]: Thinking...\n")

    response = await run_agent(agent, query)
    print(f"[Agent]: {response}")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        # Single query mode
        query = " ".join(sys.argv[1:])
        asyncio.run(single_query_mode(query))
    else:
        # Interactive mode
        asyncio.run(interactive_mode())


if __name__ == "__main__":
    main()
