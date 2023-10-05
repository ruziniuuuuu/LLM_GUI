import openai

class APIHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_response(self, prompt):
        # Handle interaction sith the OpenAI API
        pass
