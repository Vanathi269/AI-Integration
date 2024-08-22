import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title="AI Chatbot", layout="centered")

heading_color = "#b360a6"
background_color = "#333333"  # Dark background for the text box in dark mode
text_color = "#FFFFFF"  # White text for contrast in dark mode
st.markdown(f"<h1 style='text-align: center; color: {heading_color};'>Welcome to Chatbot Application</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: {heading_color};'>Will be your new best friend......</h3>", unsafe_allow_html=True)


genai.configure(api_key="AIzaSyDqeYIpvsqCO64849ypZgVQcku_AuiyqNg")
text = st.text_input(
    "Enter something:", 
    placeholder="Type your message here...", 
    key="text_input"
)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("Click me", help="Click to send your message and receive a response!"):
    if text:
        try:
            with st.spinner("Generating response..."):
                response = chat.send_message(text)
                st.success("Here's the response!")
                st.markdown(
                    f"<p style='background-color:{background_color}; color:{text_color}; padding: 10px; border-radius: 5px;'>{response.text}</p>",
                    unsafe_allow_html=True
                )
                st.progress(100)
                st.download_button(
                    label="Download response",
                    data=response.text,
                    file_name='response.txt',
                    mime='text/plain'
                )
        except Exception as e:
            st.warning("An error occurred while generating the response. Here is the partial response:")
            st.markdown(
                f"<p style='background-color:{background_color}; color:{text_color}; padding: 10px; border-radius: 5px;'>{str(e)}</p>",
                unsafe_allow_html=True
            )
    else:
        st.warning("Please enter some text before clicking the button.")
