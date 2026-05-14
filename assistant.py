import datetime
import pyttsx3

# Set up the voice
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def respond(command):
    command = command.lower().strip()

    if "hello" in command or "hi" in command or "hey" in command:
        speak("Hey! Good to see you. What can I do for you?")

    elif "how are you" in command:
        speak("I am doing great, thanks for asking! How about you?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time right now is " + now)

    elif "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak("Today is " + today)

    elif "joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "your name" in command or "who are you" in command:
        speak("I am your personal voice assistant, built with Python!")

    elif "thank" in command:
        speak("No problem at all, happy to help!")

    elif "help" in command:
        speak("You can ask me the time, the date, a joke, or just say hello!")

    elif "bye" in command or "exit" in command or "quit" in command:
        speak("Bye! Take care. See you soon.")
        return False

    else:
        speak("Hmm, I did not get that. Try asking the time, date, or say hello!")

    return True

speak("Hello! I am your voice assistant. Type your command and I will speak back to you!")
print()

running = True
while running:
    user_input = input("You: ")
    if user_input.strip():
        running = respond(user_input)
    print()