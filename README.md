# 🧠 Ingredient Co‑Pilot

An **AI‑native consumer health co‑pilot** that helps users quickly understand food ingredients in plain, human language — **not raw data**.

Instead of listing chemicals, the system explains **what actually matters**, **why it matters**, and **where uncertainty remains**, right at the moment a decision is made.

---

## 🚀 Problem This Solves

Food labels are written for **regulatory compliance**, not for humans.

Consumers are forced to interpret:
- Long ingredient lists
- Unfamiliar chemical names
- Conflicting health advice

This creates confusion exactly when people are trying to choose what to eat.

**Ingredient Co‑Pilot** bridges this gap using an **AI‑native experience**.

---

## ✨ What Makes This AI‑Native

- **Intent‑first**  
  Users simply paste ingredients — no forms, no filters.

- **Reasoning‑driven**  
  Explains *why* ingredients matter, not just what they are.

- **Low cognitive load**  
  Short, scannable, decision‑focused output.

- **Honest uncertainty**  
  Clearly states what is known vs what is uncertain.

- **Co‑pilot mindset**  
  Acts as a guide, not a database browser.

---

## 🧩 How It Works

1. User pastes an ingredient list  
2. AI infers what matters most  
3. System produces a structured, easy‑to‑read explanation:
   - Overview  
   - Key ingredients  
   - Why it matters  
   - Uncertainty  
   - Final take  

No medical advice.  
No information overload.

---

## 🛠️ Tech Stack

- **Frontend & App Framework**: Streamlit  
- **AI Model**: Google Gemini (Free tier)  
- **Language**: Python 3.10  
- **Deployment**: Streamlit Community Cloud  

---

## 📁 Project Structure

ingredient-copilot/
 ├── app.py # Main Streamlit app
 ├── config.py # API key loader (ignored in GitHub)
 ├── requirements.txt # Dependencies
 ├── .gitignore # Security & cleanup
 └── README.md # Project documentation

yaml
Copy code

---

## 🔐 API Key & Security

- API keys are **NOT stored in the repository**
- Local development uses `config.py`
- Deployment uses **Streamlit Secrets**
- `.gitignore` ensures secrets are never pushed

---

## ▶️ Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---
🌍 Live Demo
👉 Deployed on Streamlit Community Cloud
(Deployment link added after launch)

🎯 Hackathon Alignment
This project directly aligns with the challenge goals:

✅ AI is the interface, not a feature

✅ Reasoning over raw data

✅ Experience over datasets

✅ Honest uncertainty communication

✅ Clean, minimal cognitive design

⚠️ Disclaimer
This tool provides AI‑assisted explanations for awareness only.
It does not offer medical or dietary advice.
