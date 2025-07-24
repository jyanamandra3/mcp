from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.llms import OpenAI
from pydantic import BaseModel, Field

class MathQuestion(BaseModel):
    question: str = Field(..., description="A math or logic question")

llm = OpenAI(
    openai_api_key="", 
    temperature=0.2
)

tools = [
    Tool(
        name="Python Calculator",
        func=PythonREPLTool().run,
        description="Useful for solving math and logic problems"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def solve_math_question(user_input: MathQuestion):
    return agent.run(user_input.question)

if __name__ == "__main__":
    user_input_text = input("Ask a math question: ")
    math_q = MathQuestion(question=user_input_text)
    print("Answer:", solve_math_question(math_q))
