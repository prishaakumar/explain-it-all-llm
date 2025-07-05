# Explain-It-All AI: Multi-Level Explanation Generator

A Streamlit app that generates explanations for any topic at three levels:
- **Super Simple:** ELI5-style explanations
- **Easy:** For educated adults  
- **Expert:** Technical, detailed explanations

## 🚀 Live Demo

**Try it now:** [Live Demo](https://explain-it-all-llm-avzkqjaehghsdqtntbss4z.streamlit.app/)

## Features

- 🤖 **AI-Powered Explanations:** Uses OpenRouter API with Mistral-7B model
- 🔍 **Hybrid Search:** Combines AI with Google Custom Search for enhanced accuracy
- 📊 **Three Difficulty Levels:** From super simple to expert-level explanations
- ⚡ **Real-time Generation:** Instant explanations with loading indicators
- 🎨 **Clean UI:** Modern Streamlit interface with responsive design
- 🔒 **Secure:** API keys stored in Streamlit secrets

## Quick Start

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/explain-it-all-llm.git
   cd explain-it-all-llm
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys:**
   Create a `.streamlit/secrets.toml` file with:
   ```toml
   OPENROUTER_API_KEY = "your-openrouter-api-key"
   GOOGLE_API_KEY = "your-google-api-key"
   GOOGLE_CSE_ID = "your-google-cse-id"
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```



## 🔧 Configuration

### Required API Keys

1. **OpenRouter API Key:**
   - Sign up at [openrouter.ai](https://openrouter.ai)
   - Get your API key from the dashboard
   - Add to secrets as `OPENROUTER_API_KEY`

2. **Google Custom Search (Optional):**
   - Create a Custom Search Engine at [programmablesearchengine.google.com](https://programmablesearchengine.google.com)
   - Get your API key from [Google Cloud Console](https://console.cloud.google.com)
   - Add to secrets as `GOOGLE_API_KEY` and `GOOGLE_CSE_ID`

### Environment Variables

For deployment platforms that use environment variables instead of Streamlit secrets:

```bash
OPENROUTER_API_KEY=your-key-here
GOOGLE_API_KEY=your-key-here
GOOGLE_CSE_ID=your-cse-id-here
```

## 📝 Usage

1. **Enter a topic** in the text input
2. **Select difficulty levels** using the checkboxes
3. **Click "Explain"** to generate explanations
4. **Copy or share** the generated explanations

## 🛠️ Technical Details

- **Framework:** Streamlit
- **AI Model:** Mistral-7B via OpenRouter
- **Search:** Google Custom Search API
- **Deployment:** Multi-platform support
- **Security:** API keys in secrets/environment variables

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Showcase your AI integration skills with this live demo!** 🚀 