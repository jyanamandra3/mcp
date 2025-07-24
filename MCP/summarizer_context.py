from openai import OpenAI
from base_context import ModelContext

class SummarizerContext(ModelContext):
    def __init__(self):
        super().__init__("summarizer")
        self.client = OpenAI(api_key="")  
    def handle(self, user_input):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                    {"role": "user", "content": f"Summarize this in 3-5 bullet points:\n\n{user_input}"}
                ],
                temperature=0.2,
                max_tokens=100
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"[Error] {str(e)}"
