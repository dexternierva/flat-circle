import math
from typing import List, Dict

class SimpleVectorStore:
	"""A simple 'Filing Cabinet' for numerical coordinates."""
	def __init__(self):
		# We store data as: [{"text": "...", "vector": [...]}]
		self.storage: List[Dict] = []

	def add_text(self, text: str, vector: List[float]):
		"""Saves a sentence and its GPS coordinates."""
		self.storage.append({"text": text, "vector": vector})

	def _cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
		"""Math to find how 'close' two lists of numbers are."""
		dot_product = sum(a * b for a, b in zip(v1, v2))
		magnitude1 = math.sqrt(sum(a * a for a in v1))
		magnitude2 = math.sqrt(sum(b * b for b in v2))
		return dot_product / (magnitude1 * magnitude2)
	
	def search(self, query_vector: List[float], top_n: int = 1) -> List[str]:
		"""Finds the 'top_n' most similar sentences."""
		scores = []
		for item in self.storage:
			similarity = self._cosine_similarity(query_vector, item["vector"])
			scores.append((similarity, item["text"]))

		# Sort by highest score first
		scores.sort(key=lambda x: x[0], reverse=True)
		return [text for score, text in scores[:top_n]]