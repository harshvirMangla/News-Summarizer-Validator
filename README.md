# News Summarizer & Validator

A professional, AI-powered web application that fetches, summarizes, and validates news headlines in real-time using multiple APIs, delivering concise and verified answers to user queries.

## Overview

The **News Summarizer & Validator** is a Python-based web application built with Gradio, designed to provide users with accurate and up-to-date news summaries. It integrates with the **NewsAPI**, **FinlightAPI**, and **Google Gemini API** to fetch relevant headlines, validate information, and generate well-formatted responses. The application features a sleek, user-friendly interface with a dark-themed chatbot, markdown rendering, and error handling for a seamless user experience.

## Features

- **Real-Time News Fetching**: Retrieves the latest headlines from NewsAPI and FinlightAPI based on user queries.
- **AI-Powered Summarization**: Uses the Google Gemini 2.0 Flash model to generate concise, professional, and well-formatted answers.
- **Error Handling**: Custom error classes handle API rate limits and other issues gracefully, with user-friendly messages.
- **Interactive UI**: Built with Gradio, featuring a dark-themed chatbot with markdown support, user and bot avatars, and responsive design.
- **Retry and Clear Functionality**: Allows users to retry their last query or clear the chat history for a fresh start.
- **Custom Styling**: Tailored CSS for a modern, professional look with rounded chat bubbles, custom fonts, and a clean layout.
- **Example Questions**: Predefined examples to guide users on how to interact with the application.

## Project Structure

```
news-summarizer-validator/
├── assets/
│   ├── user.png           # User avatar image
│   └── bot.png            # Bot avatar image
├── config.py              # API client initialization and configuration
├── model.py               # Model class for news processing and response generation
├── main.py                # Main application script with Gradio UI
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore file for version control
└── README.md              # Project documentation
```

## Installation

### Prerequisites
- Python 3.8+
- Git
- A modern web browser

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/news-summarizer-validator.git
   cd news-summarizer-validator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**:
   - Obtain API keys from:
     - [NewsAPI](https://newsapi.org/) for news headlines
     - [FinlightAPI](https://finlightapi.com/) for financial data
     - [Google Gemini API](https://ai.google.dev/) for AI model access
   - Replace the placeholder API keys in `config.py`:
     ```python
     api_key = "your_news_api_key"
     api_key2 = "your_finlight_api_key"
     gemini_api = "your_gemini_api_key"
     ```

4. **Run the Application**:
   ```bash
   python main.py
   ```
   The application will launch in your default web browser.

## Usage

1. **Ask a Question**: Type your question in the text box (e.g., "What's the latest news in the Automobile industry?").
2. **View Response**: The chatbot will fetch relevant headlines, validate them, and provide a summarized answer in markdown format.
3. **Retry or Clear**: Use the "Retry" button to reprocess the last question or "Clear" to reset the chat history.
4. **Explore Examples**: Open the "Example questions" accordion for sample queries to try.

## Dependencies

The project relies on the following Python packages (listed in `requirements.txt`):
- `newsapi-python`: For fetching news headlines
- `finlight-client`: For financial data integration
- `google-generativeai`: For AI-powered summarization
- `gradio`: For the web-based user interface
- `rich`: For enhanced console output
- `python-dateutil`: For date handling

Install them using:
```bash
pip install newsapi-python finlight-client google-generativeai gradio rich python-dateutil
```

## Configuration

The `config.py` file initializes the API clients:
- **NewsAPI**: Configured with the `api_key` for fetching news headlines.
- **FinlightAPI**: Configured with `ApiConfig` and `api_key2` for financial data.
- **Google Gemini API**: Configured with `gemini_api` for the Gemini 2.0 Flash model.

Ensure all API keys are valid and not rate-limited to avoid `ModelError` exceptions.

## Error Handling

The application includes a custom `ModelError` class to handle API-related errors:
- **Code 100**: NewsAPI free trial limit exceeded.
- **Code 200**: FinlightAPI free trial limit exceeded.
- **Code 300**: Daily free limit exhausted for both APIs.

Error messages are displayed in the chatbot interface for user clarity.

## Development

### Tech Stack
- **Python**: Core programming language
- **Gradio**: Web interface framework
- **Google Gemini 2.0 Flash**: AI model for summarization
- **NewsAPI & FinlightAPI**: Data sources
- **Rich**: Console output formatting
- **Markdown**: Response formatting

### Customization
- **UI Styling**: Modify `CUSTOM_CSS` in `main.py` to adjust the Gradio theme, colors, or layout.
- **Model Parameters**: Update `model_name` in `model.py` to use a different Gemini model (if available).
- **Prompt Instructions**: Edit the `h3` method in `model.py` to customize the AI's response style or formatting.

### Version Control
- The `.gitignore` file excludes unnecessary files (e.g., `__pycache__`, `.env`) from the repository.
- Use Git for version control:
  ```bash
  git add .
  git commit -m "Your commit message"
  git push origin main
  ```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [your-email@example.com](mailto:your-email@example.com) or open an issue on the GitHub repository.
