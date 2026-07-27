def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hi! How can I help you today?"
    return "I'm still learning, but let's explore together!"


if __name__ == "__main__":
    print("Chatbot initialized! Type your message (or 'exit' to quit):")
    sample_inputs = ["Hello there!", "What can you do?", "Tell me a joke"]
    for sample in sample_inputs:
        print(f"User: {sample}")
        print(f"Bot: {chatbot_response(sample)}\n")
