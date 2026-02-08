def chatbot_response(user_input):
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

print("🤖 Chatbot is running (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input == "bye":
        break
