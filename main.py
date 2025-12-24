def jarvis():
    print("Hello, I am Jarvis.")
    print("How can I help you?")

    while True:
        command = input("You: ").lower()

        if "hello" in command:
            print("Jarvis: Hello! Nice to meet you.")
        elif "your name" in command:
            print("Jarvis: I am Jarvis, your AI assistant.")
        elif "exit" in command or "bye" in command:
            print("Jarvis: Goodbye! Have a nice day.")
            break
        else:
            print("Jarvis: Sorry, I didn't understand that.")


if __name__ == "__main__":
    jarvis()
