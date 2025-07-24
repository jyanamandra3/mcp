

class MCPRouter:
    def __init__(self):
        self.contexts ={}

    def register(self,task_name,context):
        self.contexts[task_name] = context

    def route(self,task_name,data):
        if task_name not in self.contexts:
            return f"[Error] Unknown task: {task_name}"
        
        return self.contexts[task_name].handle(data)