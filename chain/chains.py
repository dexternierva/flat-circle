from typing import Any
from .base import BaseModel
from .prompts import PromptTemplate

class LLMChain:
	def __init__(self, model: BaseModel, prompt: PromptTemplate):
		self.model = model
		self.prompt = prompt
	def run(self, **kwargs: Any):
		text = self.prompt.format(**kwargs)
		return self.model.generate([{"role": "user", "content": text}])
