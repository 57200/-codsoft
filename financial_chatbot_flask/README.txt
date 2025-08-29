# Financial Chatbot 💬

## 📌 Project Overview
A simple **rule-based chatbot** that answers predefined financial queries for companies using demo data.  
It is built with **Flask** for the web interface and uses **if-else logic** to simulate conversational flow.

---

## ✨ Features
- Accepts **Company name** and **Year** as input.
- Answers predefined queries:
  - *"What is the total revenue?"*
  - *"How has net income changed over the last year?"*
- Clean and simple web interface.
- Rule-based (no machine learning).

---

## 🛠️ Tech Stack
- **Python (Flask)** – Web framework.  
- **Pandas** – For reading financial CSV data.  
- **HTML/CSS** – Frontend interface.  

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
pip install -r requirements.txt

2. Run the app:
python chatbot.py

3. Open browser at:
http://127.0.0.1:5000

📂 Folder Structure
financial_chatbot_flask/
├── chatbot.py               # Main Flask app
├── financial_data_demo.csv  # Demo financial data
├── requirements.txt         # Dependencies
└── README.md                # Documentation
