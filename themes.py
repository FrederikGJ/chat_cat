# Theme configurations
THEMES = {
    "cat": {
        "primary_color": "#FF6B6B",
        "background_color": "#FFF5F5",
        "secondary_background_color": "#FFE5E5",
        "text_color": "#4A4A4A",
        "button_color": "#FF6B6B",
        "button_hover_color": "#FF5252",
        "chat_bubble_color": "#FFE5E5",
        "special_card_background": "white",
        "special_card_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
        "sidebar_background": "#FFF5F5",
        "sidebar_text": "#4A4A4A",
        "sidebar_title": "#FF6B6B",
        "name": "Cat Theme",
        "icon": "😺"
    },
    "ocean": {
        "primary_color": "#4A90E2",
        "background_color": "#F5F9FF",
        "secondary_background_color": "#E5F0FF",
        "text_color": "#2C3E50",
        "button_color": "#4A90E2",
        "button_hover_color": "#357ABD",
        "chat_bubble_color": "#E5F0FF",
        "special_card_background": "white",
        "special_card_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
        "sidebar_background": "#F5F9FF",
        "sidebar_text": "#2C3E50",
        "sidebar_title": "#4A90E2",
        "name": "Ocean Theme",
        "icon": "🌊"
    }
}

def get_theme_css(theme_name):
    """Generate CSS for the specified theme"""
    theme = THEMES[theme_name]
    
    return f"""
        <style>
        /* Main app background and base styles */
        .stApp {{
            background-color: {theme['background_color']};
            color: {theme['text_color']};
        }}
        
        /* Sidebar styling - comprehensive selectors */
        section[data-testid="stSidebar"] {{
            background-color: {theme['sidebar_background']} !important;
            color: {theme['sidebar_text']} !important;
        }}
        .css-1d391kg, .css-1v0mbdj, .css-1vq4p4l, .css-163ttbj, .css-1oe5cao {{
            background-color: {theme['sidebar_background']} !important;
        }}
        section[data-testid="stSidebar"] h1 {{
            color: {theme['sidebar_title']} !important;
        }}
        section[data-testid="stSidebar"] p {{
            color: {theme['sidebar_text']} !important;
        }}
        section[data-testid="stSidebar"] .stMarkdown {{
            color: {theme['sidebar_text']} !important;
        }}
        
        /* Buttons and interactive elements */
        .stButton>button {{
            background-color: {theme['button_color']} !important;
            color: white !important;
            border-radius: 20px !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: all 0.3s ease !important;
        }}
        .stButton>button:hover {{
            background-color: {theme['button_hover_color']} !important;
            transform: scale(1.05);
        }}
        
        /* Chat messages and containers */
        .stChatMessage {{
            background-color: {theme['chat_bubble_color']} !important;
            border-radius: 15px !important;
            padding: 15px !important;
            margin: 10px 0 !important;
        }}
        .stChatMessage p {{
            color: {theme['text_color']} !important;
        }}
        
        /* Input fields and text areas */
        .stTextInput>div>div>input {{
            border-radius: 20px !important;
            border: 2px solid {theme['primary_color']} !important;
            background-color: white !important;
            color: {theme['text_color']} !important;
        }}
        
        /* Headers and text elements */
        h1, h2, h3 {{
            color: {theme['primary_color']} !important;
            text-align: center !important;
        }}
        h1 {{
            font-size: 3em !important;
            margin-bottom: 0.5em !important;
        }}
        .main h1 {{
            color: {theme['primary_color']} !important;
        }}
        
        /* Special response cards */
        .special-response {{
            background-color: {theme['special_card_background']} !important;
            border-radius: 15px !important;
            padding: 20px !important;
            margin: 20px 0 !important;
            box-shadow: {theme['special_card_shadow']} !important;
            text-align: center !important;
        }}
        .special-response img {{
            max-width: 200px !important;
            margin-bottom: 15px !important;
        }}
        .special-response a {{
            display: inline-block !important;
            background-color: {theme['button_color']} !important;
            color: white !important;
            padding: 10px 20px !important;
            border-radius: 20px !important;
            text-decoration: none !important;
            margin-top: 10px !important;
            transition: all 0.3s ease !important;
        }}
        .special-response a:hover {{
            background-color: {theme['button_hover_color']} !important;
            transform: scale(1.05) !important;
        }}
        
        /* Footer and additional containers */
        footer {{
            background-color: {theme['background_color']} !important;
            color: {theme['text_color']} !important;
        }}
        .main .block-container {{
            background-color: {theme['background_color']} !important;
        }}
        
        /* Links */
        a {{
            color: {theme['primary_color']} !important;
        }}
        
        /* Dividers */
        hr {{
            border-color: {theme['primary_color']} !important;
        }}
        
        /* Additional Streamlit elements */
        .css-1544g2n {{
            background-color: {theme['background_color']} !important;
        }}
        .css-1kyxreq {{
            background-color: {theme['sidebar_background']} !important;
        }}
        .css-1v0mbdj.etr89bj0 {{
            background-color: {theme['background_color']} !important;
        }}
        .css-1vq4p4l.e1fqkh3o4 {{
            background-color: {theme['background_color']} !important;
        }}
        
        /* Chat input container and related elements */
        .stChatInputContainer, 
        .css-7ym5gk,
        .css-1x8cf1d,
        .css-10trblm,
        .css-1n76uvr,
        .css-1uqz6qz,
        .css-1r6slb0,
        .css-12w0qpk,
        .css-1fv8s86 {{
            background-color: {theme['background_color']} !important;
        }}
        
        /* Top bar and other persistent elements */
        .css-18e3th9,
        .css-1dp5vir,
        .css-14xtw13,
        .css-1wrcr25,
        .css-6qob1r,
        .css-1y4p8pa {{
            background-color: {theme['background_color']} !important;
        }}
        
        /* Message containers */
        .stChatMessageContent {{
            background-color: {theme['chat_bubble_color']} !important;
            color: {theme['text_color']} !important;
        }}
        
        /* Ensure text colors are consistent */
        .stMarkdown {{
            color: {theme['text_color']} !important;
        }}

        /* Chat float button */
        .stChatFloatingInputContainer {{
            background-color: {theme['background_color']} !important;
        }}

        /* Additional chat container elements */
        div[data-testid="stChatMessageInput"] {{
            background-color: {theme['background_color']} !important;
        }}

        /* Main content area */
        .main .block-container {{
            background-color: {theme['background_color']} !important;
        }}

        /* Top decoration bar */
        .decoration {{
            background-color: {theme['background_color']} !important;
        }}
        </style>
    """ 