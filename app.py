import streamlit as st
import requests
import os

st.set_page_config(page_title="Explanation Generator", page_icon="🤖", layout="centered")
st.title("Explanation Generator")
st.write("Enter a topic and instantly get three explanations: Super Simple, Easy, and Expert.")

st.markdown(
    "<span style='color: #aaa; font-size: 0.9em;'>Tip: For best results, use full topic names, include context, or ask about related concepts.</span>",
    unsafe_allow_html=True
)

topic = st.text_input("Enter a topic:")

# User-friendly labels and mapping
level_labels = {
    "Super Simple": "Super Simple",
    "Easy": "Easy",
    "Expert": "Expert"
}

# Checkbox selection for levels
selected_levels = []
if st.checkbox(level_labels["Super Simple"], value=True):
    selected_levels.append("Super Simple")
if st.checkbox(level_labels["Easy"], value=True):
    selected_levels.append("Easy")
if st.checkbox(level_labels["Expert"], value=True):
    selected_levels.append("Expert")

system_prompt = """
You are ExplainMaster, an AI that explains concepts at multiple levels.
For each query, you must provide three explanations, each starting with its label on a new line and nothing else before the label.
Use these exact section headers, in this order, and do not add any extra text or formatting:

Super Simple:
• (your first simple point)
...

Easy:
• (your first easy point)
...

Expert:
• (your first expert point)
...

Do NOT use numbering. Only use bullet points (•) and the section headers as shown.
If you don't know, say 'I'm not sure, but here's what I can infer:'.
Each section should have at least 8-10 bullet points, and elaborate on each point for maximum detail.
"""

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct"

# You can set this to your email or localhost for local dev
HTTP_REFERER = "http://localhost"
X_TITLE = "Explain-It-All-AI"

# --- Google CSE Hybrid Search ---
def google_cse_search(query):
    cse_id = st.secrets.get("GOOGLE_CSE_ID")
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not cse_id or not api_key:
        return None
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        results = data.get("items", [])
        return results[:3]  # Top 3 results
    return None

def summarize_cse_results(results):
    if not results:
        return ""
    summary = "Here are some relevant web results for context:\n"
    for i, item in enumerate(results, 1):
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        summary += f"{i}. {title}\n{snippet}\nSource: {link}\n\n"
    summary += "\nUse these results to inform your explanations if relevant.\n"
    return summary

# --- LLM Explanation ---
def get_explanations(topic):
    api_key = st.secrets["OPENROUTER_API_KEY"] if "OPENROUTER_API_KEY" in st.secrets else os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        st.error("OpenRouter API key not found. Set it in Streamlit secrets or as an environment variable.")
        return None
    # Hybrid: Get web results
    cse_results = google_cse_search(topic)
    cse_summary = summarize_cse_results(cse_results) if cse_results else ""
    # Compose prompt
    full_prompt = cse_summary + system_prompt
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": HTTP_REFERER,
        "X-Title": X_TITLE,
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": full_prompt},
        {"role": "user", "content": f"Explain: {topic}"}
    ]
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": messages,
        "max_tokens": 2500,
        "temperature": 0.7
    }
    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            st.error("Unexpected response format from OpenRouter API.")
            return None
    else:
        st.error(f"OpenRouter API error: {response.status_code} - {response.text}")
        return None

def parse_explanations(text):
    import re
    sections = {"Super Simple": "", "Easy": "", "Expert": ""}
    for level in sections:
        # Use re.IGNORECASE for robustness
        pattern = rf"{level}:\s*(.*?)(?=\n[A-Z][a-z ]+:|$)"
        m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if m:
            sections[level] = m.group(1).strip()
    return sections

if st.button("Explain") and topic:
    with st.spinner("Generating explanations..."):
        result = get_explanations(topic)
        if result:
            explanations = parse_explanations(result)
            for level in selected_levels:
                st.markdown(f"### {level_labels[level]}")
                explanation = explanations.get(level, "No explanation found.")
                explanation_md = explanation.replace("•", "-")
                st.markdown(explanation_md) 