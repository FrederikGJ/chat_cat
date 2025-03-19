import streamlit as st
import random
from datetime import datetime

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Cat responses
cat_responses = [
    "Miaow! 😺",
    "Purrr... 😸",
    "Hiss! 😾",
    "Meow meow! 😽",
    "Mrow! 😺",
    "Purr purr... 😸",
    "Miaow miaow! 😽",
    "Hiss hiss! 😾",
    "Meow! 😺",
    "Purr... 😸"
]

# Angry cat responses (in Danish)
angry_cat_responses = [
    "MIAU FOR HELVEDE! Hvad fanden er det for noget at sige 'ak' til mig! 😾",
    "Hvad i alverden er det for noget lort! AK?! AK?! MIAU! 😾",
    "For satan da også! Nu bliver jeg fandme sur! AK er et forbudt ord! 😾",
    "MIAU! MIAU! MIAU! Hvad bilder du dig ind at sige AK til mig! 😾",
    "For fanden da også! Nu skal jeg fandme vise dig hvem der er boss her! AK er ikke okay! 😾",
    "MIAU! Du ved fandme godt at AK er et forbudt ord! 😾",
    "For helvede da også! Nu bliver jeg fandme sur! AK?! 😾",
    "MIAU! Hvad fanden er det for noget at sige AK til mig! 😾",
    "For satan! Nu skal jeg fandme vise dig hvem der er boss her! AK er ikke okay! 😾",
    "MIAU! MIAU! MIAU! AK er et forbudt ord, og du ved det! 😾"
]

# Set page config
st.set_page_config(
    page_title="Chat with a Cat",
    page_icon="😺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5F5;
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF5252;
        transform: scale(1.05);
    }
    .stChatMessage {
        background-color: #FFE5E5;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 2px solid #FF6B6B;
    }
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🐱 Cat Chat Info")
    st.markdown("---")
    st.write("Welcome to Cat Chat! This is a simple chat application where you can talk to a cat.")
    st.write("The cat will respond with various cat sounds and expressions.")
    st.write("⚠️ Warning: Don't say 'ak' or 'AK' unless you want to make the cat angry! 😾")
    st.markdown("---")
    st.write("Current time:", datetime.now().strftime("%H:%M:%S"))
    if st.button("Clear Chat", key="sidebar_clear"):
        st.session_state.messages = []
        st.rerun()

# Main content
st.title("Chat with a Cat 😺")
st.markdown("<div style='text-align: center; color: #666;'>Write something to the cat and it will respond with cat sounds!<br>⚠️ Warning: Don't say 'ak' or 'AK' unless you want to make the cat angry! 😾</div>", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to say to the cat?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Check if the message contains 'ak' or 'AK'
    if "ak" in prompt.lower():
        cat_response = random.choice(angry_cat_responses)
    else:
        cat_response = random.choice(cat_responses)
    
    # Add cat response to chat history
    st.session_state.messages.append({"role": "assistant", "content": cat_response})
    
    # Display cat response
    with st.chat_message("assistant"):
        st.write(cat_response)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>Made with ❤️ by a cat lover</div>", unsafe_allow_html=True) 