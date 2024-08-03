import streamlit as st
from utlis import *

from st_audiorec import st_audiorec

st.title("Live Speech to Job Offer Generator")
    
    # Capture live audio
wav_audio_data = st_audiorec()
print(wav_audio_data)
if wav_audio_data is not None:
    print("HELLO")
    # Convert audio to text
    with st.spinner("Converting..."):
        transcribed_text = audio_to_text(wav_audio_data)
        st.markdown("_Transcribed Text:_", unsafe_allow_html=True)  # Italicize and center the label
        st.markdown(f'<p style="text-align: center;">"{transcribed_text}"</p>', unsafe_allow_html=True)  # Center the transcribed text and keep it in quotes


    if transcribed_text and st.button("Generate Job Offer"):
        # Generate the job offer from the text
        with st.spinner("Generate..."):
            job_offer = call_ai_api(transcribed_text)
            st.write("Generated Job Offer:")
            st.write(job_offer)
