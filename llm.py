from typing import List, Dict
import cohere # type: ignore

class CohereAPI:
    def __init__(self, api_key: str, model: str = "command-r-plus-08-2024"):
        self.client = cohere.ClientV2(api_key=api_key)
        self.model = model
        self.documents = []

    def set_documents(self, documents: List[Dict[str, str]]):
        self.documents = [
            {"data": {"title": doc["title"], "snippet": doc["snippet"]}}
            for doc in documents
        ]
        
    def add_document(self, title: str, snippet: str):
        self.documents.append({"data": {"title": title, "snippet": snippet}})
        
    def pop_document(self):
        self.documents.pop()

    def send_prompt(self, prompt: str, max_tokens: int = 1024, temperature: float = 0.2) -> Dict[str, str]:
        response = self.client.chat(
            model=self.model,
            documents=self.documents,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )

        return response.message.content[0].text
        