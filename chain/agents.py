import json
from typing import List, Callable, Dict, Any, Optional
from .base import BaseModel

class Tool:
	"""A wrapper for a Python function that the Agent can call."""
	def __init__(self, name: str, func: Callable, description: str):
		self.name = name
		self.func = func
		self.description = description

class MiniAgent:
	"""An autonomous agent that can decide which tool to use."""
	def __init__(self, model: BaseModel, tools: List[Tool]):
		self.model = model
		self.tools = {t.name: t for t in tools}

	def _generate_system_prompt(self) -> str:
		"""Constructs instructions for the LLM on how to use tools."""
		tool_strings = "\n".join([f"- {t.name}: {t.description}" for t in self.tools.values()])

		return f"""You are a helpful assistant with access to tools. If you need to use a tool to answer, you MUST respond with a JSON object:
		{{""tool": "tool_name", "input": "search_query_or_input"}}

		Available tools:
		{tool_strings}

		If you have the final answer, just provide it as normal text.
		"""
	
	def run(self, user_input: str) -> str:
		"""The execution loop: LLM decides to use a tool or answer."""

		# Initialize messages with instructions
		messages = [
			{"role": "system", "content": self._generate_system_prompt()},
			{"role": "user", "content": user_input}
		]

		# First pass: Ask the model what to do
		response = self.model.generate(messages)

		# Check if the model is trying to call a tool
		try:
			if '{"tool":' in response:
				# Basic parsing: extract JSON from the text
				start_idx = response.find('{')
				end_idx = response.rfind('}') + 1
				tool_call = json.loads(response[start_idx:end_idx])

				tool_name = tool_call["tool"]
				tool_input = tool_call["input"]

				if tool_name in self.tools:
					# 1. Execute the tool
					observation = self.tools[tool_name].func(tool_input)

					# 2. Feed the 'Observation' back to the model
					messages.append({"role": "assistant", "content": response})
					messages.append({
						"role": "system",
						"content": f"Observation from {tool_name}: {observation}"
					})

					# 3. Get the final answer from the model
					return self.model.generate(messages)
		except Exception as e:
			return f"Agent Error: {str(e)} | Original Response: {response}"
		
		return response