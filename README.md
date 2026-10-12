
# 🤖 Static Prompt UI — Gemini Research Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4?logo=google)
![Generative AI](https://img.shields.io/badge/Field-Generative%20AI-green)

## 📌 Project Overview

**Static Prompt UI** is a lightweight web application built with Streamlit that demonstrates how to interact with Google's Gemini generative AI model through a simple user interface.

Users can enter a text prompt, submit it to the Gemini model, and view the generated response directly in the application. The project provides a practical introduction to connecting a large language model (LLM) with a Python-based web interface.

It focuses on the basic workflow of prompt input, model invocation, response generation, and error handling.

## Project Objectives

- Build a simple user interface for interacting with a generative AI model.
- Understand how text prompts are passed to an LLM.
- Integrate the Gemini API into a Python application.
- Load API credentials securely using environment variables.
- Display generated responses through Streamlit.
- Handle missing prompts, missing API keys, and model errors.

## How It Works

The application follows a straightforward workflow:

1. **Load Configuration:** Load environment variables from a `.env` file.
2. **Read API Credentials:** Retrieve the Google API key from the environment.
3. **Initialize Gemini:** Configure the Gemini client and select a model.
4. **Accept User Input:** Provide a text field where users enter their prompts.
5. **Generate a Response:** Send the prompt to the selected Gemini model when the Generate button is clicked.
6. **Display the Output:** Show the generated text in the Streamlit interface.
7. **Handle Errors:** Display appropriate messages when the API key is missing or a model request fails.

## Key Concepts

### 1. Prompt Engineering

A prompt is the instruction or question given to a language model. The wording and context of a prompt can influence the relevance, clarity, and usefulness of the generated response.

### 2. Large Language Models

Large language models generate text based on the input they receive and patterns learned during training. This project demonstrates how an LLM can be accessed through an API rather than running the model locally.

### 3. API Integration

The application connects Python code to Google's Gemini service. This introduces the basic process of configuring credentials, submitting requests, receiving model responses, and handling errors.

### 4. Streamlit Interface

Streamlit makes it possible to create an interactive web interface using Python without building a separate frontend with HTML, CSS, or JavaScript.

### 5. Environment Variables

The Google API key is loaded from an environment variable rather than being written directly into the source code.

## Technology Stack

- **Language:** Python
- **Web Interface:** Streamlit
- **Generative AI Model:** Google Gemini
- **API Integration:** Google Generative AI Python SDK
- **Configuration:** python-dotenv

## Getting Started

### Prerequisites

- Python 3.x
- A Google Gemini API key with access to the selected model
- An internet connection

### 1. Clone the Repository

```bash
git clone https://github.com/mani787060/static_prompt_ui.git
cd static_prompt_ui
```

### 2. Install Dependencies

```bash
pip install streamlit google-generativeai python-dotenv
```

### 3. Configure the API Key

Create a file named `.env` in the project directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with your actual API key.

**Security note:** Add `.env` to `.gitignore` and never commit your API key to GitHub.

### 4. Run the Application

The Python file in this repository is named `1_static_prompt_ui.py`. Start the application with:

```bash
streamlit run 1_static_prompt_ui.py
```

### 5. Use the Interface

1. Open the local URL provided by Streamlit.
2. Enter a prompt in the text field.
3. Click **Generate**.
4. Read the response displayed in the results section.

## Example Use Cases

- Asking general research questions.
- Summarizing short passages of text.
- Explaining technical concepts.
- Generating ideas or outlines.
- Experimenting with prompt wording and model responses.

These are potential uses of the prompt interface, not separate features currently implemented in the application.

## Learning Outcomes

This project helps develop an understanding of:

- Basic prompt engineering.
- LLM API integration.
- Streamlit application development.
- Environment-variable configuration.
- Text generation workflows.
- Basic exception handling in generative AI applications.

## Future Improvements

- Add reusable prompt templates for summarization, translation, and code review.
- Support system instructions and configurable generation settings.
- Add conversation history for multi-turn interactions.
- Display loading indicators and improve error messages.
- Add response copying and download options.
- Introduce structured outputs and input validation.
- Extend the application into a multi-model prompt interface.
- Migrate to a currently supported Google Gen AI SDK and model configuration.

## Implementation Notes

The application currently demonstrates a basic, single-prompt interaction rather than a complete conversational agent. API compatibility depends on the installed SDK version and the availability of the configured Gemini model. Check the current Google Gen AI documentation if you encounter model or endpoint errors.

## Conclusion

Static Prompt UI is a starting point for exploring how generative AI can be integrated into a Python web application. By connecting a Streamlit interface to Gemini, the project demonstrates the core workflow of accepting prompts, generating responses, and presenting LLM output to users.

It also provides a foundation for experimenting with more advanced prompt engineering techniques and building richer AI-powered applications.
