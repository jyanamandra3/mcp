def classify_task(input_data):
    input_lower = input_data.lower()

    if "summary" in input_lower or "summarize" in input_lower:
        return "summarizer"
    
    elif "translate" in input_lower:
        return "translator"
    
    else:
        return "Unknown"