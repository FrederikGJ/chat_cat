import streamlit as st
import random
from datetime import datetime
from special_responses import get_special_response
from themes import get_theme_css, THEMES

# Initialize session state for chat history and theme
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_theme" not in st.session_state:
    st.session_state.current_theme = "cat"

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

# Apply theme CSS
st.markdown(get_theme_css(st.session_state.current_theme), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title(f"{THEMES[st.session_state.current_theme]['icon']} Cat Chat Info")
    st.markdown("---")
    st.write("Welcome to Cat Chat! This is a simple chat application where you can talk to a cat.")
    st.write("The cat will respond with various cat sounds and expressions.")
    st.write("⚠️ Warning: Don't say 'ak' or 'AK' unless you want to make the cat angry! 😾")
    st.write("Try asking about 'fire assistant', 'dbi', or 'brandrådgiver' for special responses!")
    st.markdown("---")
    st.write("Current time:", datetime.now().strftime("%H:%M:%S"))
    
    # Theme switcher
    st.markdown("### Theme Settings")
    if st.button(f"Switch to {THEMES['ocean' if st.session_state.current_theme == 'cat' else 'cat']['name']} {THEMES['ocean' if st.session_state.current_theme == 'cat' else 'cat']['icon']}"):
        st.session_state.current_theme = 'ocean' if st.session_state.current_theme == 'cat' else 'cat'
        st.rerun()
    
    if st.button("Clear Chat", key="sidebar_clear"):
        st.session_state.messages = []
        st.rerun()

# Main content
st.title(f"Chat with a Cat {THEMES[st.session_state.current_theme]['icon']}")
st.markdown(f"<div style='text-align: center; color: #666;'>Write something to the cat and it will respond with cat sounds!<br>⚠️ Warning: Don't say 'ak' or 'AK' unless you want to make the cat angry! 😾<br>Try asking about 'fire assistant', 'dbi', or 'brandrådgiver' for special responses!</div>", unsafe_allow_html=True)

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
    
    # Check for special responses
    special_response = get_special_response(prompt)
    
    if special_response:
        # Add special response to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"Hey! I noticed you mentioned '{special_response['title']}'. Here's some information about it:"
        })
        
        # Display special response card
        st.markdown(f"""
            <div class="special-response">
                <img src="{special_response['image_url']}" alt="{special_response['title']}">
                <h3>{special_response['title']}</h3>
                <p>{special_response['description']}</p>
                <a href="{special_response['link']}" target="_blank">Learn more</a>
            </div>
        """, unsafe_allow_html=True)
    else:
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