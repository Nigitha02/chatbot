import streamlit as st
from groq import Groq
import time
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(api_key=os.getenv("api"))
st.set_page_config(page_title="Graq AI chat",page_icon="❤")
st.title("❤Groq AI assistant")
st.write("streaming response with animation☠")
if "message" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    if msg["role"]=="user":
        st.markdown("###YOu")
        st.write(msg["content"])
    else:
        st.markdown("###Assistant")
        st.write(msg["content"])
st.markdown("---")
prompt=st.text_input("Ask something...")
if st.button("send") and prompt:
    st.session_state.messages.append(
        {"role":"user","content":prompt}
        )
    st.markdown("###you")
    st.write(prompt)
    st.markdown("###Assistant")
    message_placeholder=st.empty()
    full_response=""
    completion=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages,
        stream=True,
        )
    for chunk in completion:
        if chunk.choices[0].delta.content:
            full_response+=chunk.choices[0].delta.content
            message_placeholder.markdown(full_response+" ")
            time.sleep(0.02)
    message_placeholder.markdown(full_response)
    st.session_state.messages.append(
        {"role":"assistant","content":full_response}
        )
    
    
                     
