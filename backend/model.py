class Gemma2Chatbot:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        return "Gemma2 Model Loaded"

    def get_response(self, message):
        return f"Gemma2 says: '{message}' is received!"
