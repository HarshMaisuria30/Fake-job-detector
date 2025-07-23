# =========================================
# Fake Job Detector Project
# Author: Harsh Maisuria
# Year: 2025
# Description: Streamlit-based web app to detect fake job postings
# =========================================

import streamlit as st
from utils.heuristics import is_suspect_job  

st.set_page_config(page_title="Fake Job Detector", layout="centered")

st.title("🚨 Fake Job Postings Detector")
st.write("Paste a job description and requirements below. The app will tell you if the job seems suspicious.")

description = st.text_area("📝 Job Description (Enter at least 10 to 15 words)")
requirements = st.text_area("📌 Job Requirements")

if st.button("Check If Suspicious"):
    if description.strip() == "" and requirements.strip() == "":
        st.warning("Please enter a job description or requirements.")

    elif len(description.split()) < 10 and len(requirements.split()) < 10:
        st.warning("⚠️ This job post is too short. Be cautious.")
    
    elif description.strip().lower() == requirements.strip().lower():
        st.warning("⚠️ The job description and requirements are nearly identical. This might be suspicious.")
    
    else:
        is_fake, match_info = is_suspect_job(description, requirements)
        
        if is_fake:
            st.error("⚠️ This job seems suspicious!")
            st.toast("❌ You are not eligible!", icon="👎🏻")
        else:
            st.success("✅ This job looks fine.")
            st.toast("🎉 You are eligible!", icon="✅")

        st.info(f"🔍 {match_info}")
       
st.set_page_config(page_title="Fake Job Detector | Harsh Maisuria", layout="centered")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: blue;'>🛡️ Project by <strong>Harsh Maisuria</strong> © 2025</p>",
    unsafe_allow_html=True
)

