def get_bot_response(user_message):
    """
    This function receives the user's message
    and returns the chatbot's response.
    """

    message = user_message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello! I am your Smart Chatbot Assistant. How can I help you?"

    elif "name" in message:
        return "My name is SmartAssist AI."

    elif "resume" in message:
        return "I can help analyze resumes and give improvement suggestions."

    elif "expense" in message or "spending" in message:
        return "I can help track and analyze your expenses."

    elif "voice" in message:
        return "Voice assistant feature will allow users to speak and hear responses."

    elif "bye" in message or "exit" in message:
        return "Goodbye! Have a productive day."

    else:
        return "I am still learning. Please ask about resume, expenses, voice assistant, or chatbot features."


def start_chatbot():
    """
    This function starts the chatbot conversation in the terminal.
    """

    print("===================================")
    print("       SmartAssist AI Chatbot       ")
    print("===================================")
    print("Type 'exit' to close the chatbot.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            print("Bot: Goodbye! Have a productive day.")
            break

        response = get_bot_response(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    start_chatbot()