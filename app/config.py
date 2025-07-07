from newsapi import NewsApiClient
from finlight_client import FinlightApi, ApiConfig
import google.generativeai as genai

api_key  = "your_news_api_key"
api_key2 = "your_finlight_api_key"
gemini_api = "your_gemini_api_key"

newsapi = NewsApiClient(api_key=api_key)

client = FinlightApi(
    config=ApiConfig(api_key=api_key2)
)

genai.configure(api_key=gemini_api)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
