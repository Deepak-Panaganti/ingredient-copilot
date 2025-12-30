import streamlit as st
import google.generativeai as genai
from config import GEMINI_API_KEY  # 👈 import key from file

# -----------------------------
# Gemini Configuration (UNCHANGED)
# -----------------------------
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-flash-latest")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Ingredient Co-Pilot",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🧠 Ingredient Co-Pilot")
st.caption(
    "A simple AI co-pilot that explains what food ingredients really mean — quickly and clearly."
)

st.write("")

# -----------------------------
# Input
# -----------------------------
ingredients = st.text_area(
    "Paste ingredients here",
    placeholder="Skimmed milk powder, sugar, cocoa solids, emulsifier (soy lecithin), artificial chocolate flavor",
    height=120
)

st.write("")
analyze = st.button("Analyze Ingredients")

# -----------------------------
# Output
# -----------------------------
if analyze:
    if ingredients.strip() == "":
        st.warning("Please enter ingredients to analyze.")
    else:
        with st.spinner("Analyzing ingredients..."):
            prompt = f"""
You are an AI consumer health co-pilot.

The user wants a QUICK, EASY-TO-READ understanding of food ingredients.

Ingredients:
{ingredients}

Rules (very important):
- Keep the answer SHORT and SIMPLE
- Do NOT overload information
- Focus only on what truly matters
- Use plain, human language
- Avoid long explanations
- Avoid medical advice

Use EXACTLY this structure and keep each section concise:

OVERVIEW
(1–2 short lines)

KEY INGREDIENTS
• ingredient – very short impact

WHY IT MATTERS
(2–3 simple lines, no technical depth)

UNCERTAINTY
(1 short line)

FINAL TAKE
(1 clear sentence)
"""
            response = model.generate_content(prompt)

        st.divider()

        with st.container(border=True):
            formatted_output = (
            response.text
            .replace(
                "OVERVIEW",
                "<span style='color:#93C5FD; font-weight:700;'>OVERVIEW</span>"
            )
            .replace(
                "KEY INGREDIENTS",
                "<span style='color:#93C5FD; font-weight:700;'>KEY INGREDIENTS</span>"
            )
            .replace(
                "WHY IT MATTERS",
                "<span style='color:#93C5FD; font-weight:700;'>WHY IT MATTERS</span>"
            )
            .replace(
                "UNCERTAINTY",
                "<span style='color:#93C5FD; font-weight:700;'>UNCERTAINTY</span>"
            )
            .replace(
                "FINAL TAKE",
                "<span style='color:#93C5FD; font-weight:700;'>FINAL TAKE</span>"
            )
        )

            st.markdown(formatted_output, unsafe_allow_html=True)
        #     .replace("UNCERTAINTY", "**UNCERTAINTY**")
        #     .replace("FINAL TAKE", "**FINAL TAKE**")
        # )

        #     st.markdown(formatted_output)

            # st.markdown(response.text)

        st.write("")
        st.caption(
            "This is an AI-generated explanation for awareness, not medical advice."
        )
