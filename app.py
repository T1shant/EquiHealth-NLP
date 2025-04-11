import streamlit as st
import spacy
import pandas as pd
import numpy as np

# Load the trained spaCy model (ensure the folder is present in your repo or local dir)
nlp = spacy.load("equihealth_spacy_model_v2")  # Update this path if needed

st.set_page_config(page_title="EquiHealth Classifier", layout="centered")
st.title("🧠 EquiHealth NLP Classifier")
st.markdown("Classify healthcare-related sentences into key child health dimensions.")

# User input
input_text = st.text_area("Enter sentence(s) to classify:", height=150)

if st.button("Classify"):
    if input_text.strip():
        lines = [line.strip() for line in input_text.split("\n") if line.strip()]
        results = []

        for line in lines:
            # Handle uncertainty in short/ambiguous sentences
            if len(line.split()) < 3:
                results.append((line, "⚠️ Too short/ambiguous", 0.0))
                continue
            doc = nlp(line)
            pred = max(doc.cats, key=doc.cats.get)
            confidence = round(doc.cats[pred], 4)
            results.append((line, pred, confidence))

        df = pd.DataFrame(results, columns=["Sentence", "Predicted Category", "Confidence"])
        st.success("Classification complete.")
        st.dataframe(df)

        # Flag low-confidence outputs
        low_conf = df[df["Confidence"] < 0.6]
        if not low_conf.empty:
            st.warning("Some predictions had low confidence (< 0.6). Consider reviewing them manually.")
    else:
        st.warning("Please enter at least one sentence.")

st.markdown("---")
st.caption("Built with ❤️ by the EquiHealth Team")
