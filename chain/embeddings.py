from typing import List, Optional
from huggingface_hub import InferenceClient

class Embedder:
	"""Turns text into a list of numbers (Vectors)."""
	def __init__(self, model_id: str = "sentence-transformers/all-MiniLM-L6-v2", token: Optional[str] = None):
		self.client = InferenceClient(model=model_id, token=token)

	def embed_text(self, text: str) -> List[float]:
		"""Calls Hugging Face to get the numerical coordinate for a string."""
		# This returns a list of about 384 numbers representing the 'meaning'
		# ~~return self.client.feature_extraction(text)~~
		return self.client.feature_extraction(text).tolist()