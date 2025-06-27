class ModelContext:
    def __init__(self,name):
        self.name = name

    def handle(self,user_input):
        raise NotImplementedError("Subclasses must implement handle()")
        