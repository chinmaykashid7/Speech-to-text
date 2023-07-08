import speech_recognition as sr

recognizer = sr.Recognizer()

microphone = sr.Microphone()




print("Listening...")

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise

    while True:
        try:
            audio = recognizer.listen(source)  # Listen for audio input
            text = recognizer.recognize_google(audio)  # Perform speech recognition
            print("You said:", text)
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print("Error occurred: ", str(e))
        except KeyboardInterrupt:
            print('!!FINISH!!')
            break
