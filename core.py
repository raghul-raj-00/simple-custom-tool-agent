import os
from dotenv import load_dotenv
load_dotenv()


from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b
@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b
@tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

model=ChatMistralAI(model="mistral-small-latest", temperature=0.4, max_tokens=512)
tools=[add, subtract, multiply, divide]
agent=create_agent(model=model,
                   tools=tools, 
                   system_prompt="""
    You are an arithmetic assistant.

    Always use the available tools for calculations.
    You can use multiple tools when necessary.
    """)
inp=input("Enter your calculation: ")
result=agent.invoke({
    "messages":[
        {
            "role":"user",
            "content":inp
        }
        
    ]
})

#print("API KEY LOADED:", os.getenv("MISTRAL_API_KEY") is not None)
print("agent:",result["messages"][-1].content)
