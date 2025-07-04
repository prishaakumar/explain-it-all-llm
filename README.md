# Explain-It-All AI: Multi-Level Explanation Generator

A minimal Streamlit app that generates explanations for any topic at three levels:
- **ELI5:** Simple, analogy-driven
- **Pro:** For educated adults
- **Expert:** Technical, detailed

## Setup
1. Clone this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key using Streamlit secrets:**
   - Create a folder named `.streamlit` in your project directory (if it doesn't exist).
   - Inside `.streamlit`, create a file named `secrets.toml`.
   - Add this line to the file (replace with your actual key):
     ```
     OPENAI_API_KEY = "your-api-key-here"
     ```
   - Your `.streamlit/secrets.toml` file is already excluded from git for security.
4. Run the app:
   ```
   streamlit run app.py
   ```

## Usage
- Enter any topic and click "Explain" to get three tailored explanations instantly.

## Features
- Fast, real-time AI explanations
- No database required
- Clean Streamlit UI
- Supports OpenAI (GPT-3.5/4) or Hugging Face models

## How It Works
1. Enter a topic
2. Instantly receive three tailored explanations
3. Copy, share, or use as you wish

## Deployment
- Deploy on Streamlit Cloud or Hugging Face Spaces for a live demo

---

*Showcase your prompt engineering, API integration, and UX skills with this project!* 