import streamlit as st
import pickle
import numpy as np

st.title("🎓 Student Performance Predictor 🇹🇿")
st.markdown("Predict total score from study habits")

# Load model using pickle (works 100% on Streamlit)
try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("✅ Model loaded!")
except:
    st.error("❌ Model file missing. Check GitHub files.")
    st.stop()

# Input sliders
col1, col2, col3 = st.columns(3)
hours = col1.slider("📚 Weekly Study Hours", 0.0, 40.0, 15.0)
attend = col2.slider("📈 Attendance %", 0.0, 100.0, 85.0)
part = col3.slider("💬 Participation (0-10)", 0.0, 10.0, 5.0)

if st.button("🔮 **PREDICT SCORE**", type="primary"):
    input_data = np.array([[hours, attend, part]])
    score = model.predict(input_data)[0]
    
    st.success(f"**Predicted Score: {score:.1f}/100**")
    
    # Grade
    if score >= 90: grade = "A"
    elif score >= 80: grade = "B" 
    elif score >= 70: grade = "C"
    else: grade = "D"
    
    st.info(f"**Expected Grade: {grade}**")
    
    col1.metric("Study Hours", f"{hours} hrs")
    col2.metric("Attendance", f"{attend}%")
    col3.metric("Participation", f"{part}/10")

st.markdown("*Built for Tanzanian students* 🇹🇿")

st.markdown("*Built for Tanzanian students* 🇹🇿")
