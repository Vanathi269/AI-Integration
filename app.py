import streamlit as st
import google.generativeai as genai

# Set page configuration
st.set_page_config(page_title="AI Chatbot", layout="centered")

# Define colors and styles for the app
heading_color = "#b360a6"
subheading_color = "#ffcc29"
background_color = "#4d4d4d"  # Grey background
text_color = "#FFFFFF"  # White text for visibility
button_color = "#ff6f61"
box_color = "#666666"
response_box_color = "#333333"
success_color = "#4CAF50"
warning_color = "#FF9800"

# Customize the layout with some padding and spacing
st.markdown(f"""
    <style>
        .reportview-container {{
            background: {background_color};
        }}
        .main {{
            background: {background_color};
            padding: 1rem;
        }}
        .stTextInput input {{
            background-color: {box_color};
            color: {text_color};
            border-radius: 5px;
            padding: 0.5rem;
        }}
        h1 {{
            color: {heading_color};
        }}
        h3 {{
            color: {subheading_color};
        }}
        .stButton button {{
            background-color: {button_color};
            color: {text_color};
        }}
    </style>
""", unsafe_allow_html=True)

# Main heading with animation
st.markdown(f"<h1 style='text-align: center;'>🤖 Welcome to Chatbot Application 🤖</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>Your new interactive AI friend!</h3>", unsafe_allow_html=True)

# Integrate Google Generative AI
genai.configure(api_key="AIzaSyDqeYIpvsqCO64849ypZgVQcku_AuiyqNg")
text = st.text_input(
    "Type your message below:", 
    placeholder="Ask anything...", 
    key="text_input"
)

# Customize interactive elements like buttons and progress bars
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Interactive container with columns for better layout
col1, col2, col3 = st.columns(3)
if col2.button("💬 Send Message", help="Click to send your message and receive a response!"):
    if text:
        try:
            with st.spinner("🔄 AI is thinking..."):
                response = chat.send_message(text)
                st.success("✔️ Here's the response!", icon="✅")
                
                # Show the response with a large, visible box
                st.markdown(
                    f"<div style='background-color:{response_box_color}; color:{text_color}; padding: 20px; margin-top: 20px; font-size: 18px; border-radius: 10px;'>"
                    f"<strong>AI's Response:</strong><br><br>{response.text}</div>",
                    unsafe_allow_html=True
                )
                
                # Display progress and download button
                st.progress(100)
                st.download_button(
                    label="⬇️ Download response",
                    data=response.text,
                    file_name='response.txt',
                    mime='text/plain'
                )

                # Add a slider for user engagement
                slider_val = st.slider("How helpful was this response?", 0, 10, 5)
                st.write(f"You rated the response: {slider_val}/10")

                # Interactive expander for additional options
                with st.expander("🔧 Advanced Options"):
                    st.write("You can customize settings here!")
                    st.checkbox("Enable debug mode")
                    st.checkbox("Show previous responses")
                    
        except Exception as e:
            st.error("⚠️ An error occurred while generating the response.")
            st.markdown(
                f"<div style='background-color:{warning_color}; color:{text_color}; padding: 15px; border-radius: 10px;'>{str(e)}</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter some text before clicking the button.")
        
# Add footer with social media buttons for engagement
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Stay Connected:</h4>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f"""
        <div style='display: flex; justify-content: space-around;'>
            <a href="https://twitter.com" target="_blank"><img src="https://img.icons8.com/color/48/000000/twitter.png" /></a>
            <a href="https://linkedin.com" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png" /></a>
            <a href="https://github.com" target="_blank"><img src="https://img.icons8.com/color/48/000000/github.png" /></a>
        </div>
    """, unsafe_allow_html=True)
