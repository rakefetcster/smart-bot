
from config import GOOGLE_API_KEY
import google.generativeai as genai
import json

from IPython.display import display
from IPython.display import Markdown
# from google.colab import userdata


class Manager:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self,message):
        print(message)
        response = self.model.generate_content(message).text
        return(response)