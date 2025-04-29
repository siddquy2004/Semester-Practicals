# simple customer service chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "order" in user_input:
        return "please provide your order id."
    elif "refund" in user_input:
        return "you can request a refund by visiting your orders page."
    elif "return" in user_input:
        return "returns are accepted within 30 days of delivery."
    elif "hello" in user_input or "hi" in user_input:
        return "hello! how can i assist you today?"
    elif "problem" in user_input or "issue" in user_input:
        return "i'm sorry to hear that. can you please describe your issue?"
    elif "thank you" in user_input or "thanks" in user_input:
        return "you're welcome! have a great day."
    else:
        return "i'm sorry, i didn't understand that. could you please rephrase?"

# chatbot main loop
print("chatbot: hello! i am your service assistant. how can i help you?")
while True:
    user_message = input("you: ")
    if user_message.lower() in ["bye", "exit", "quit"]:
        print("chatbot: thank you for contacting us. goodbye!")
        break
    response = chatbot_response(user_message)
    print("chatbot:", response)
