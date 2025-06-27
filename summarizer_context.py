from base_context import ModelContext

class SummarizerContext(ModelContext):
    def __init__(self):
        super().__init__("summarizer")

    def handle(self, user_input):
        return f"[Summary] {user_input[:50]}..."