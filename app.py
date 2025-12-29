import streamlit as st
import google.generativeai as genai

# ==================================================
# 🔴 GEMINI API KEY (INBUILT)
# ==================================================
GEMINI_API_KEY = "AIzaSyAT4yWYWjm37h_H9chBiVmbEshYDM5n6lc"

genai.configure(api_key=GEMINI_API_KEY)

# ================== PAGE CONFIG ==================
st.set_page_config("Super Home AI 🏠", layout="wide")

st.title("🏠 Super Home AI Agent")
st.caption("Meal planning • Grocery lists • Smart home decisions")

tabs = st.tabs(["🍳 Meal Planner", "🛒 Grocery Planner", "📊 Dashboard"])

# ================== SAFE GEMINI CALL ==================
def ask_ai(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "⚠️ AI service temporarily unavailable. Please try again."

# ================== MEAL PLANNER ==================
with tabs[0]:
    ing = st.text_input("Available ingredients")
    diet = st.selectbox("Diet preference", ["None", "Vegetarian", "Vegan"])
    time = st.slider("Cooking time (mins)", 10, 60, 30)

    if st.button("🍳 Suggest Meals"):
        prompt = f"""
Suggest 3 meals using:
Ingredients: {ing}
Diet: {diet}
Cooking time: {time} minutes
"""
        with st.spinner("Thinking..."):
            st.success(ask_ai(prompt))

# ================== GROCERY PLANNER ==================
with tabs[1]:
    meals = st.text_area("Planned meals")
    if st.button("🛒 Generate Grocery List"):
        prompt = f"Create a grocery shopping list for these meals:\n{meals}"
        with st.spinner("Preparing list..."):
            st.success(ask_ai(prompt))

# ================== DASHBOARD ==================
with tabs[2]:
    st.info("📊 Smart Home Insights")

    if st.button("📊 Get Daily Home Tips"):
        prompt = """
Give smart daily home optimization tips covering:
- Meal planning
- Grocery efficiency
- Time & energy saving
"""
        with st.spinner("Optimizing home..."):
            st.success(ask_ai(prompt))

