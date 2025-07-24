from summarizer_context import SummarizerContext
from translator_context import TranslatorContext
from mcp_router import MCPRouter
from classifer import classify_task

def main():
    router=MCPRouter()
    router.register("summarizer",SummarizerContext())
    router.register("translator",TranslatorContext())

    user_input = input("Enter a task : ")
summa
    task=classify_task(user_input)
    print(f"Task Detected : {task}")

    result=router.route(task,user_input)
    print("Result : ",result)


if __name__ =="__main__":
    main()