# 📊 Chatbot for Excel Data Analysis

An **AI-powered chatbot** that lets you query Excel/CSV files in **natural language**.
Built using **Python, Streamlit, Gemini API, and Pandas**, this tool helps non-technical users extract insights, summarize data, and interpret KPIs without writing code.

---

## 🚀 Features

* Upload **Excel/CSV files** and chat with your data.
* **Natural language queries** powered by Gemini API.
* Handles **entire sheets**, not just previews.
* Provides **summaries, KPI extraction, and trends**.
* Clean and interactive **Streamlit UI**.

---

## 🛠️ Tech Stack

* **Python** – Data handling and backend logic
* **Streamlit** – Interactive web app interface
* **Pandas** – Data preprocessing and analysis
* **Gemini API** – LLM integration for natural language Q\&A

---

## 📂 Project Structure

```
ChatBot_for_Excel/
│-- main.py              # Streamlit app
│-- requirements.txt     # Dependencies
│-- .streamlit/
│   └── secrets.toml     # API key (not committed to GitHub)
│-- sample_data.xlsx     # Example dataset
│-- README.md            # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ChatBot_for_Excel.git
cd ChatBot_for_Excel
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API key

Create a file at `.streamlit/secrets.toml` and add:

```toml
API = "your_api_key_here"
```

### 4️⃣ Run the app

```bash
streamlit run main.py
```

## 🔮 Future Improvements

* Support for **Google Sheets / SQL databases**
* Advanced **charting and visualization** in responses
* Multi-file support with **cross-dataset queries**
