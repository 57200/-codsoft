from flask import Flask, render_template_string, request
import pandas as pd

# Load demo financial data
data = pd.read_csv("financial_data_demo.csv")

app = Flask(__name__)

# --- Simple rule-based chatbot logic ---
def simple_chatbot(company, year, query):
    try:
        row = data[(data["Company"] == company) & (data["Year"] == int(year))].iloc[0]
    except IndexError:
        return f"Sorry, I couldn't find data for {company} in {year}."

    if query.lower() == "what is the total revenue?":
        return f"The total revenue for {company} in {year} is ${row['Revenue']} million."
    elif query.lower() == "how has net income changed over the last year?":
        prev_year = int(year) - 1
        try:
            prev_row = data[(data["Company"] == company) & (data["Year"] == prev_year)].iloc[0]
            change = row["NetIncome"] - prev_row["NetIncome"]
            trend = "increased" if change > 0 else "decreased"
            return f"The net income has {trend} by ${abs(change)} million compared to {prev_year}."
        except IndexError:
            return f"Net income data for {prev_year} is not available."
    else:
        return "Sorry, I can only answer predefined queries like 'What is the total revenue?' or 'How has net income changed over the last year?'."

# --- HTML Template ---
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Financial Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f9; padding: 40px; }
        .chatbox { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #333; }
        input, select { width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background: #007bff; color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 5px; }
        button:hover { background: #0056b3; }
        .response { margin-top: 20px; padding: 15px; background: #e9f7ef; border-left: 5px solid #28a745; }
    </style>
</head>
<body>
    <div class="chatbox">
        <h2>📊 Financial Chatbot</h2>
        <form method="POST">
            <label>Company:</label>
            <input type="text" name="company" placeholder="e.g. Apple" required>

            <label>Year:</label>
            <input type="number" name="year" placeholder="e.g. 2024" required>

            <label>Query:</label>
            <select name="query">
                <option>What is the total revenue?</option>
                <option>How has net income changed over the last year?</option>
            </select>

            <button type="submit">Ask</button>
        </form>

        {% if response %}
        <div class="response">
            <strong>Answer:</strong> {{ response }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        company = request.form["company"]
        year = request.form["year"]
        query = request.form["query"]
        response = simple_chatbot(company, year, query)
    return render_template_string(html_template, response=response)

if __name__ == "__main__":
    app.run(debug=True)
