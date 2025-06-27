from base_context import ModelContext

class TranslatorContext(ModelContext):
    def __init__(self):
        super().__init__("translator")

    def handle(self, user_input):
        return f"[Translated] {user_input[::-1]}"