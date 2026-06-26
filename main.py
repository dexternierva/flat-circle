import os
from dotenv import load_dotenv
from chain import HuggingFaceModel, Tool, MiniAgent

load_dotenv()

# 1. Define a custom tool
def calculator(expression: str):
	"""A simple math tool."""
	try:
		# Note: eval is dangerous in production, but okay for a mini-project
		return str(eval(expression))
	except:
		return "Error: Could not calculate."
	
# 2. Setup the pieces
math_tool = Tool(
	name="calculator",
	func=calculator,
	description="Useful for solving math problems. Input should be a math expression like 2+2."
)

model = HuggingFaceModel(
    model_id="mistralai/Mistral-7B-Instruct-v0.2:featherless-ai",
    token=os.getenv("HF_TOKEN", "")
)

# 3. Run the agent
agent = MiniAgent(model=model, tools=[math_tool])

print("--- Calling Agent ---")
result = agent.run("What is 1234 multiplied by 56?")
print(f"Final Answer: {result}")