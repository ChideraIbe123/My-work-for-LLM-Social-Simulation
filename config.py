''' A configuration file with LLM config and keys, to avoid circular imports'''

victor_opeai_key = ""


AUTOGEN_LLM_CONFIG = {
    "config_list": [
        {
            "model": "gpt-3.5-turbo",
            "api_key": victor_opeai_key,
        },  
    ], 
    "temperature": 0.0, 
}
