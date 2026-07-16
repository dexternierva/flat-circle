import os
from typing import List

class TextLoader:
	"""The Scanner: Reads a file and breaks it into chunnks."""

	def __init__(self, file_path: str):
		self.file_path = file_path

	def load_and_split(self, chunk_size: int = 500) -> List[str]:
		"""Reads the file and cuts it into pieces of 'chunk_size' characters."""
		if not os.path.exists(self.file_path):
			return[f"Error: File {self.file_path} not found."]
		
		with open(self.file_path, 'r', encoding='utf-8') as f:
			text = f.read()

		# "Chunking" - We cut the text every 500 characters
		# so it fits nicely in the AI's memory.
		chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
		return chunks