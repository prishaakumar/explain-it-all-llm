# 🚀 Deployment Guide

This guide will help you deploy your Explain-It-All AI app to various platforms for a live demo.

## Prerequisites

1. **GitHub Account:** Make sure your code is pushed to GitHub
2. **API Keys:** You'll need your OpenRouter API key (and optionally Google API keys)
3. **Repository:** Your code should be in a public repository

## Platform Options

### 1. Streamlit Cloud (Easiest) ⭐

**Steps:**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Fill in the details:
   - **Repository:** `your-username/explain-it-all-llm`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click "Deploy"
6. Add your secrets in the app settings:
   ```
   OPENROUTER_API_KEY = your-api-key-here
   GOOGLE_API_KEY = your-google-api-key (optional)
   GOOGLE_CSE_ID = your-cse-id (optional)
   ```

**Result:** Your app will be live at `https://your-app-name.streamlit.app`

### 2. Hugging Face Spaces

**Steps:**
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose settings:
   - **Owner:** Your username
   - **Space name:** `explain-it-all-llm`
   - **SDK:** Streamlit
   - **License:** MIT
4. Upload your files or connect your GitHub repo
5. Add secrets in Settings → Repository secrets:
   ```
   OPENROUTER_API_KEY
   GOOGLE_API_KEY
   GOOGLE_CSE_ID
   ```

**Result:** Your app will be live at `https://huggingface.co/spaces/your-username/explain-it-all-llm`

### 3. Railway

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables:
   ```
   OPENROUTER_API_KEY=your-key-here
   GOOGLE_API_KEY=your-key-here
   GOOGLE_CSE_ID=your-id-here
   ```

**Result:** Railway will provide you with a custom domain

### 4. Render

**Steps:**
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New" → "Web Service"
4. Connect your repository
5. Configure:
   - **Name:** `explain-it-all-llm`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variables in the dashboard

**Result:** Your app will be live at `https://your-app-name.onrender.com`

### 5. Heroku (Legacy)

**Steps:**
1. Install Heroku CLI
2. Run these commands:
   ```bash
   heroku create your-app-name
   heroku config:set OPENROUTER_API_KEY=your-key-here
   git push heroku main
   ```

## Environment Variables

For platforms that don't support Streamlit secrets, use these environment variables:

```bash
OPENROUTER_API_KEY=your-openrouter-api-key
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CSE_ID=your-google-cse-id
```

## Troubleshooting

### Common Issues:

1. **"API key not found" error:**
   - Make sure you've added the secrets/environment variables correctly
   - Check the variable names match exactly

2. **App won't start:**
   - Verify `requirements.txt` is in the root directory
   - Check that `app.py` is the main file

3. **Import errors:**
   - All dependencies should be in `requirements.txt`
   - Some platforms may need additional system packages

### Getting API Keys:

1. **OpenRouter API Key:**
   - Sign up at [openrouter.ai](https://openrouter.ai)
   - Go to API Keys in your dashboard
   - Create a new key

2. **Google API Keys (Optional):**
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Enable Custom Search API
   - Create credentials
   - Set up Custom Search Engine at [programmablesearchengine.google.com](https://programmablesearchengine.google.com)

## Updating Your Live Demo

After making changes to your code:

1. **Push to GitHub:** `git push origin main`
2. **Most platforms will auto-deploy** from your main branch
3. **For manual platforms:** Trigger a new deployment

## Custom Domain (Optional)

Some platforms allow custom domains:
- **Streamlit Cloud:** Not supported
- **Railway:** Yes, in the dashboard
- **Render:** Yes, in the dashboard
- **Heroku:** Yes, with custom domain add-on

## Monitoring

- **Streamlit Cloud:** Built-in analytics
- **Railway:** Usage metrics in dashboard
- **Render:** Basic metrics included
- **Hugging Face:** Space analytics

---

**Your live demo is ready! Share the URL in your README and portfolio.** 🎉 