from typing import Dict, List, Any
from huggingface_hub import InferenceClient
from .base import BaseModel

class HuggingFaceModel(BaseModel):
    def __init__(self, model_id: str, token: str):
        # Ensure we are using the InferenceClient
        self.client = InferenceClient(model=model_id, token=token)

    def generate(self, messages: List[Dict[str, str]]) -> str:
        # Adding a timeout and ensuring max_new_tokens
        response = self.client.chat_completion(
            messages=messages, 
            max_tokens=500,
        )
        content = response.choices[0].message.content
        return content if content is not None else ""