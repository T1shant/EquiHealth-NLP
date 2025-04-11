# EquiHealth-NLP

# 🌍 EquiHealth NLP Classifier

This is a Streamlit web app that classifies healthcare-related policy statements into one of five core child health categories:
**Availability**, **Accessibility**, **Acceptability**, **Quality**, and **Child-Specific Protections**.

Built with ❤️ by Tishant Doorgapersand and team for the EquiHealth project.

---

## 🔎 What It Does

- Accepts free-text health policy statements as input
- Uses a custom-trained spaCy NLP model to classify each line
- Outputs predictions with confidence scores
- Handles short/uncertain inputs gracefully
- (Optional) Saves inputs to a database for future analysis

---

## 🧪 Live Demo

Try it here: [https://equihealth-nlp.streamlit.app](https://equihealth-nlp.streamlit.app)  
*(Replace this link with your actual Streamlit URL once deployed)*

---


---

## ⚙️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py




