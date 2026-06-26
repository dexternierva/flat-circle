from typing import List, Dict

class ConversationMemory:
	"""Manages the state of a conversation (Chat History)."""

	def __init__(self):
		self.messages: List[Dict[str, str]] = []

	def add_messages(self, role: str, content: str) -> None:
		"""Adds a message to the history. Role should be 'user' or 'assistant'."""
		self.messages.append({"role": role, "content": content})

	def get_message(self) -> List[Dict[str, str]]:
		"""Returns the full conversation history."""
		return self.messages
	
	def clear(self) -> None:
		"""Wipes the memory clean."""
		self.messages = []