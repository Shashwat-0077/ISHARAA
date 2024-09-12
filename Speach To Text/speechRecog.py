import speech_recognition as sr

# Initialize the Recognizer
recognizer = sr.Recognizer()


def listen_and_convert():
    """Listens to the user's voice input and converts it to text."""
    try:
        with sr.Microphone() as mic:
            # Adjust for ambient noise and notify the user
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            print("Recording has started. Please speak...")

            # Capture the user's voice input
            audio = recognizer.listen(mic)

            # Convert speech to text using Google API
            text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")
            return text
    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
        return None
    except sr.RequestError:
        print("API request failed. Please check your internet connection.")
        return None


while True:
    try:
        spoken_text = listen_and_convert()

        if spoken_text:
            # Check for stop or exit command
            if spoken_text in ["stop", "exit"]:
                print("Stopping the recording...")
                break

    except KeyboardInterrupt:
        print("KeyboardInterrupt detected. Exiting...")
        break

print("Program terminated.")