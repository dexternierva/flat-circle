import os
from dotenv import load_dotenv
from chain import HuggingFaceModel, Tool, MiniAgent, ConversationMemory
from chain.embeddings import Embedder
from chain.vectorstore import SimpleVectorStore
from chain.loaders import TextLoader

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN", "")

# --- PART 1: THE CALCULATOR TOOL ---

def calculator(expression: str):
	"""A simple math tool."""
	try:
		# Note: eval is dangerous in production, but okay for a mini-project
		return str(eval(expression))
	except:
		return "Error: Could not calculate."

math_tool = Tool(
	name="calculator",
	func=calculator,
	description="Useful for solving math problems. Input should be a math expression like 2+2."
)

model = HuggingFaceModel(
    model_id="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_TOKEN", "")
)

# --- PART 2: THE RAG COMPONENT ---

# 1. Initialize the Librarian (Embedder) and the Filing Cabinet (Vector Store)
embedder = Embedder(token=HF_TOKEN)
vstore = SimpleVectorStore()

# 2. Load the text document and split it into chunks for embedding
loader = TextLoader("my_school_notes.txt")
chunks = loader.load_and_split()
for chunk in chunks:
	vector = embedder.embed_text(chunk)
	vstore.add_text(chunk, vector)

# 3. Define the Search Tool function
def search_library(query: str):
	"""Searhes the private knowledge base for facts."""
	query_vector= embedder.embed_text(query)
	results = vstore.search(query_vector, top_n=1)
	return results[0] if results else "No relevant information found."

# 4. Wrap it in a Tool object so the Agent can see it
search_tool = Tool(
	name="search_library",
	func=search_library,
	description="Useful for finding private info about project codes, passwords, and meetings."
)

# --- PART 3: SETUP AMD RUN THE AGENT ---
model = HuggingFaceModel(
	model_id="Qwen/Qwen2.5-7B-Instruct",
	token=HF_TOKEN
)

# Give the agent TWO tools: the calculator AND the search library
agent = MiniAgent(model=model, tools=[math_tool, search_tool])

print("\n--- Calling Agent with a Math Question ---")
res1 = agent.run("What is 1234 multiplied by 56?")
print(f"Final Answer: {res1}")

print("\n--- Calling Agent with a Library Question ---")
res2 = agent.run("What is the secret code name for the project?")
print(f"Final Answer: {res2}")