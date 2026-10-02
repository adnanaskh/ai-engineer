import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.capabilities import WebSearch
from pydantic_ai_harness import Advisor, Coder

load_dotenv()

agent = Agent(
    'google:gemini-1.5-pro',
    capabilities=[
        Coder(workspace='.'),  
        WebSearch(),
        Advisor('google:gemini-1.5-flash')
    ]
)

if __name__ == "__main__":
    result = agent.run_sync("Write a hello world script")
    print(result.data)