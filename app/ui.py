from .model import Model, ModelError
import gradio as gr

import gradio as gr
import time

myModel2 = Model()

def process_question(question, history, retry = False):
    if not question.strip():
        return history, "", "Please enter a question to get started."
    history = history + [{"role": "user", "content": question}]
    try:
        if retry:
            markdown_result = myModel2.retry(upToDate = True, ret = True, question = question)
        else:
            markdown_result = myModel2.answer(upToDate = True, ret = True, question = question)
        history = history + [{"role": "assistant", "content": markdown_result}]
        return history, "", ""
    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        history = history + [{"role": "assistant", "content": error_msg}]
        return history, "", ""

def clear_chat():
    myModel2.clearHistory()
    return [], "", "Chat cleared. Ask me anything!"

def retry_last(history):
    if not history or len(history) < 2:
        return history, "", "No previous question to retry."
    last_question = next((m["content"] for m in reversed(history) if m["role"] == "user"), None)
    if not last_question:
        return history, "", "No previous question found."
    while history and history[-1]["role"] == "assistant":
        history.pop()
    if history and history[-1]["role"] == "user":
        history.pop()
    return process_question(last_question, history, retry = True)

theme = gr.themes.Soft(
    primary_hue = "sky", 
    secondary_hue = "slate",
    radius_size = "lg",
    text_size = "lg"
)

CUSTOM_CSS = """
/* page background */
html, body, .gradio-container, .main {
    background: #0f172a !important;
    color: #f8fafc !important;
}
/* chatbot bubbles */
.message.user   {background:#5b5b5b !important;color:#ffffff !important;}
.message.bot {
    background: #000000 !important;
    color: #ffffff !important;       /* dark gray text */
    border: 1px solid #e0e7ff !important;
}
.message {
    border-radius: 12px !important;
    padding: 10px !important;
}
/* buttons */
button {border-radius:12px !important;font-weight:600;}
/* hide gradio footer *
footer {display:none !important;}
"""

with gr.Blocks(title = "News Summarizer & Validator",
               css = CUSTOM_CSS,
               theme = theme) as demo:

    gr.HTML("""
        <div class="py-4 text-center">
            <h1 class="text-3xl font-bold text-indigo-600">
                News Summarizer&nbsp;&middot;&nbsp;Validator
            </h1>
            <p class="text-slate-600 text-base">
                Ask anything and get concise, verified answers.
            </p>
        </div>
    """)

    with gr.Row():
        chatbot = gr.Chatbot(label = None,
                             height = 700,
                             value = [],
                             show_copy_button = True,
                             render_markdown = True,
                             type = "messages",
                             avatar_images = (
                                 "user.png",
                                 "bot.png"
                             ))

    status_text = gr.Markdown("💡 Ready!", visible = True)

    with gr.Row():
        with gr.Column(scale = 7):
            question_input = gr.Textbox(
                placeholder="Ask me anything...",
                lines = 2,
                max_lines = 6,
                show_label = False,
                container = False
            )
        with gr.Column(scale = 1, min_width = 100):
            send_btn = gr.Button("Send", variant = "primary", size = "sm")
        with gr.Column(scale = 1, min_width = 100):
            retry_btn = gr.Button("🔄 Retry", variant = "secondary", size = "sm")
        with gr.Column(scale = 1, min_width = 100):
            clear_btn = gr.Button("🗑️ Clear", variant = "secondary", size = "sm")

            
    # with gr.Row():
    #     question_input = gr.Textbox(
    #         placeholder="Type your question here…",
    #         lines=2,
    #         max_lines=6,
    #         show_label=False
    #     )
    #     send_btn  = gr.Button("Send", variant="primary")
    #     retry_btn = gr.Button("Retry 🔄", variant="secondary")
    #     clear_btn = gr.Button("Clear 🗑️", variant="secondary")

    with gr.Accordion("Example questions", open = False):
        gr.Examples(
            examples = [
                "Explain the sequence of events that lead to the India-Pakistan escalation.",
                "How did other countries react to the India-Pakistan escalation?",
                "Did Bitcoin hit its all time high recently?",
                "What's the situation between Trump and Harvard University?",
                "Explain the bill that Republicans want to pass in USA.",
                "What is the latest news in the Automobile industry?",
                "Is there something worth knowing about the recent Geopolitics?",
                "What's new in NLP?",
                "How are markets doing today?",
                "Who is the winner of the Norway Chess?",
                "What has been going in the Formula 1 world recently?",
                "What are some big events of 2025?",
                "Tell me something about FIFA WC."
            ],
            inputs = question_input
        )

    def _send(msg, hist): return process_question(msg, hist)
    send_btn.click(_send,  [question_input, chatbot], [chatbot, question_input, status_text], show_progress = True)
    question_input.submit(_send, [question_input, chatbot], [chatbot, question_input, status_text], show_progress = True)
    retry_btn.click(retry_last, chatbot, [chatbot, question_input, status_text])
    clear_btn.click(clear_chat, None, [chatbot, question_input, status_text])

if __name__ == "__main__":
    demo.launch(inbrowser = True)
