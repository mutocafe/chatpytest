import streamlit as st
import speech_recognition as sr


# 20240817 traial
ss = st.session_state
if 'flgVoiceMode' not in ss:
    ss['flgVoiceMode'] = False

def start_speech_recognition():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        st.write("Listening...")

        # Adjust the ambient noise threshold for better recognition
        r.adjust_for_ambient_noise(source)

        # Continuously listen for audio input
        while True:
            audio = r.listen(source)

            # Perform speech recognition
            try:
                text = r.recognize_google(audio, language="ja-JP")
                st.write("Recognized Text:", text)
            except sr.UnknownValueError:
                st.write("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                st.write("Sorry, an error occurred during speech recognition:", str(e))

def main():
    st.title("Speech Recognition Chat App")

    # Create a button to start/stop the speech recognition
    if st.button("Voice mode on/off"):
        ss.flgVoiceMode = not ss.flgVoiceMode
        if ss.flgVoiceMode:
            st.write("Voice mode is on.")
            start_speech_recognition()
        else:
            st.write("Voice mode is off.")

if __name__ == "__main__":
    main()