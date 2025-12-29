import streamlit as st
import google.generativeai as genai

# ==================================================
# 🔴 GEMINI API KEY (INBUILT ONLY)
# ==================================================
GEMINI_API_KEY = "AIzaSyAT4yWYWjm37h_H9chBiVmbEshYDM5n6lc"

genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config("Super Home AI 🏠", layout="wide")

st.title("🏠 Super Home AI Agent")
st.caption("Meal planning • Grocery lists • Smart home decisions")

tabs = st.tabs(["🍳 Meal Planner", "🛒 Grocery Planner", "📊 Dashboard"])

def ask_ai(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model.generate_content(prompt).text

with tabs[0]:
    ing = st.text_input("Available ingredients")
    diet = st.selectbox("Diet", ["None","Vegetarian","Vegan"])
    time = st.slider("Cooking time (mins)", 10, 60, 30)
    if st.button("Suggest Meals"):
        st.success(ask_ai(f"Suggest meals using {ing}, diet {diet}, time {time} mins"))

with tabs[1]:
    meals = st.text_area("Planned meals")
    if st.button("Generate Grocery List"):
        st.success(ask_ai(f"Create grocery list for: {meals}"))

with tabs[2]:
    st.success(ask_ai("Give daily smart home optimization tips"))
