from .config import newsapi, client, model

import gradio as gr
import time

from rich.console import Console
from rich.markdown import Markdown

class Model:
    def __init__(self):
        self.model_name = "gemini-2.0-flash"
        self.model = model
        self.history = ""

    # keep everything exactly the same
    def h1(self):
        return "The following is the User Query: \n"

    def h2(self):
        return "The following are the relevant headlines found from news API:\n"

    def h3(self):
        from datetime import date
        today = date.today()
        t1 = "\nCheck if any matches user question and tell the user."
        t2 = "Else handle the situation appropriately."
        t3 = "\nAct professionally and try to explain the matching results a bit.\nDon't mention provided headlines. Act like you are the agent."
        t4 = "\nMention sources if any and also try possible expansions of abbreviations."
        t0 = "Dont ever mention about 'the articles'. Reply as if it were your knowledge in the first place. As if you were a super intelligent person."
        t5 = f"Today's date is {today} for your additional knowledge."

        prompt = f"""
        You are a news assistant bot. When the user asks a question, match it with current headlines and generate a well-formatted answer.
        **Instructions**:
        - Use **bold** for important entities or keywords or maybe location names.
        - Use *italics* for quotes or indirect information.
        - Use __underline__ for dates or time references.
        Use double line breaks in markdown (\n\n) between paragraphs for clearer separation in chat bubbles.
        """
        return t1 + t2 + t3 + t4 + t5 + t0 + prompt

    def contextProvider(self, retry=False):
        return ""

    # keep all other methods exactly as you wrote
    # get_data, get_more_data, fetch_news, clearHistory, answer, retry

class ModelError(Exception):
    def __init__(self, code):
        self.code = code
        self.message = self._generate_message(code)
        super().__init__(self.message)

    def _generate_message(self, code):
        messages = {
            100: "News-API has exceeded its free trial limit. Please purchase the premium package.",
            200: "Finlight-API has exceeded its free trial limit. Please purchase the premium package.",
            300: "Daily free limit of both APIs has been exhausted. Please purchase the premium package.",
        }
        return messages.get(code, f"⚠️ Unknown error occurred. Code: {code}")
