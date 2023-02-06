import streamlit as st
import sklearn
import pandas
import numpy as np
import pyaudio
import wave

st.markdown("<h1 style='text-align: center;'>Transcribing Audio to Text</h1>", unsafe_allow_html=True)

def main():
    st.title("Employee Information")

    name = st.text_input("Employee Name", "Enter employee name")
    domain = st.text_input("Domain", "Enter domain")
    age = st.number_input("Age", value=18, min_value=18, max_value=100)
    role = st.selectbox("Role", ["Data Analyst", "Data Scientist", "Manager", "Machine Learning Engineer"])

    status = st.empty()

    if st.button("Start Recording"):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        WAVE_OUTPUT_FILENAME = "recording.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        status.write("Recording...")
        frames = []

        while True:
            data = stream.read(CHUNK)
            frames.append(data)

            if st.button("Stop Recording"):
                stream.stop_stream()
                stream.close()
                p.terminate()
                break

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        status.write("Done recording.")

    if st.button("Submit"):
        st.success("Employee Information:")
        st.write("Name: ", name)
        st.write("Domain: ", domain)
        st.write("Age: ", age)
        st.write("Role: ", role)

if __name__ == "__main__":
    main()


