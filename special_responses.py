def get_special_response(message):
    """
    Check if the message contains specific keywords and return appropriate response
    """
    message_lower = message.lower()
    
    special_keywords = {
        "fire assistant": {
            "title": "Fire Assistant",
            "description": "Er du ude for en brandskade? Fire Assistant er her for at hjælpe dig!",
            "link": "https://assistent.brandsikringafbyggeri.dk/",
            "image_url": "https://fire-assistant.dk/wp-content/uploads/2023/03/fire-assistant-logo.png"
        },
        "dbi": {
            "title": "DBI - Det Danske Brandværn",
            "description": "DBI er Danmarks førende center for brandforskning og sikkerhed.",
            "link": "https://assistent.brandsikringafbyggeri.dk/",
            "image_url": "https://www.dbi.dk/sites/default/files/2021-03/dbi-logo.png"
        },
        "brandrådgiver": {
            "title": "Brandrådgiver",
            "description": "Få professionel rådgivning om brandsikring og brandforebyggelse.",
            "link": "https://assistent.brandsikringafbyggeri.dk/",
            "image_url": "https://fire-assistant.dk/wp-content/uploads/2023/03/fire-assistant-logo.png"
        }
    }
    
    for keyword, response in special_keywords.items():
        if keyword in message_lower:
            return response
    
    return None 