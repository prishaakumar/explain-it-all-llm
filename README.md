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

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account
2. **Sign up** at [share.streamlit.io](https://share.streamlit.io)
3. **Connect your GitHub account**
4. **Deploy:**
   - Click "New app"
   - Select your forked repository
   - Set the path to `app.py`
   - Add your secrets in the Streamlit Cloud dashboard
5. **Share your live demo URL!**

### Option 2: Hugging Face Spaces

1. **Create a new Space** on [huggingface.co/spaces](https://huggingface.co/spaces)
2. **Choose Streamlit** as the SDK
3. **Upload your files** or connect your GitHub repo
4. **Add secrets** in the Space settings
5. **Your app will be live** at `https://huggingface.co/spaces/your-username/explain-it-all-llm`

### Option 3: Railway

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect your GitHub repository**
3. **Add environment variables** for your API keys
4. **Deploy automatically** on every push

### Option 4: Render

1. **Sign up** at [render.com](https://render.com)
2. **Create a new Web Service**
3. **Connect your GitHub repository**
4. **Add environment variables** for your API keys
5. **Deploy with automatic updates**

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