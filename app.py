import streamlit as st

st.set_page_config(
    page_title="MedAI Triage",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 MedAI Triage")
st.subheader("AI-assisted symptom triage prototype")

st.info(
    "Educational prototype only. This tool does not provide a medical diagnosis "
    "and does not replace a doctor."
)

symptoms = st.text_area(
    "Describe your symptoms",
    placeholder="Example: fever, severe headache and difficulty breathing"
)

if st.button("Assess risk"):
    if not symptoms.strip():
        st.warning("Please describe your symptoms.")
    else:
        text = symptoms.lower()

        emergency_signs = [
            "difficulty breathing",
            "can't breathe",
            "chest pain",
            "loss of consciousness",
            "unconscious",
            "severe bleeding",
            "stroke",
            "seizure",
            "convulsion"
        ]

        urgent_signs = [
            "high fever",
            "severe headache",
            "persistent vomiting",
            "severe abdominal pain",
            "confusion",
            "dehydration"
        ]

        if any(sign in text for sign in emergency_signs):
            st.error("🔴 HIGH RISK — seek emergency medical care immediately.")
            st.write(
                "The described symptom may indicate a potentially serious condition. "
                "Contact local emergency medical services."
            )

        elif any(sign in text for sign in urgent_signs):
            st.warning("🟠 MODERATE RISK — medical assessment is recommended soon.")
            st.write(
                "Consider contacting a healthcare professional, especially if "
                "symptoms are worsening or persistent."
            )

        else:
            st.success("🟢 LOWER RISK — no emergency pattern detected.")
            st.write(
                "This does not rule out illness. Monitor your symptoms and "
                "consult a healthcare professional if they persist or worsen."
            )

st.divider()

st.caption(
    "MedAI Triage is an educational software prototype created to explore "
    "AI-assisted healthcare decision support."
)
