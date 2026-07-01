# 🤖 AI-Powered NL2SQL Tool

An AI-powered web application that converts **Natural Language** questions into **SQL queries** using **Google Gemini API** and **LangChain**, executes them on a SQLite database, and displays the results through an interactive Streamlit dashboard.

---

## 📌 Project Overview

The AI-Powered NL2SQL Tool enables users to analyze structured data without writing SQL queries.

Users can simply upload a CSV file, ask questions in plain English, and the application automatically:

- Converts the CSV into a SQLite database
- Generates SQL queries using Gemini AI
- Executes the generated SQL
- Displays results in tables and charts
- Allows downloading query results as CSV

This project combines **Artificial Intelligence**, **Natural Language Processing**, and **Database Management** to simplify data analysis for everyone.

---

# ✨ Features

- 🤖 AI-generated SQL queries using Google Gemini API
- 🧠 LangChain integration for Natural Language Processing
- 📂 Upload CSV datasets
- 🗄 Automatic SQLite database creation
- 🔍 Automatic SQL query execution
- 📊 Dashboard Summary (KPI Cards)
- 📈 Interactive Charts
- 📜 Query History
- 📥 Download results as CSV
- 🎨 User-friendly Streamlit interface

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | Web Application |
| SQLite | Database |
| Pandas | Data Processing |
| Matplotlib | Data Visualization |
| LangChain | LLM Integration |
| Google Gemini API | SQL Generation |
| python-dotenv | API Key Management |

---

# 📂 Project Structure

```
AI-NL2SQL-Tool
│
├── app.py
├── ai_sql.py
├── database.py
├── sample.db
├── requirements.txt
├── .gitignore
├── README.md
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/ranjani-hegde/AI-NL2SQL-Tool.git
```

### Move into Project Folder

```bash
cd AI-NL2SQL-Tool
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Gemini API

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Application

```bash
python -m streamlit run app.py
```

---

# 💻 Example Questions

Try asking questions like:

- Show all products
- Show total sales
- Top selling product in January
- Show quantity by product
- Show sales by category
- Show sales by month
- Show average sales
- Show top 5 products

---

# ⚙️ Workflow

```
CSV Upload
      │
      ▼
SQLite Database
      │
      ▼
User enters question
      │
      ▼
Gemini API + LangChain
      │
      ▼
Generate SQL Query
      │
      ▼
Execute SQL
      │
      ▼
Display Results
      │
      ▼
Charts + Dashboard + CSV Download
```

---

# 🌟 Key Features

✅ Natural Language to SQL Conversion

✅ AI-Powered Query Generation

✅ Interactive Dashboard

✅ Query History

✅ CSV Upload

✅ Download Query Results

✅ Data Visualization

---

# 🔮 Future Enhancements

- Support MySQL and PostgreSQL
- AI-powered SQL correction
- Voice-to-SQL conversion
- Authentication & User Login
- SQL Explanation in Natural Language
- Export Reports as PDF
- Chat-style Interface
- Multi-table Database Support

---

# 👩‍💻 Developer

**Ranjani Hegde**

B.E. Computer Science & Design Engineering

Alva's Institute of Engineering and Technology

GitHub: https://github.com/ranjani-hegde

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
