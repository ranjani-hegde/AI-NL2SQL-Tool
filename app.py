from ai_sql import generate_ai_sql
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NL2SQL Tool", layout="wide")

st.title("🤖 AI-Powered NL2SQL Tool")
st.caption("Convert natural language into SQL queries using Gemini API and analyze data instantly")

if "history" not in st.session_state:
    st.session_state.history = []

db_name = "sample.db"
table_name = "sales"

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df_upload = pd.read_csv(uploaded_file)
    df_upload.columns = df_upload.columns.str.lower()

    conn = sqlite3.connect(db_name)
    df_upload.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    st.success("CSV uploaded and converted into database table successfully!")
    st.subheader("Uploaded Dataset")
    st.dataframe(df_upload)


def show_dashboard_summary():
    conn = sqlite3.connect(db_name)

    try:
        df = pd.read_sql_query("SELECT * FROM sales", conn)

        if not df.empty:
            st.subheader("📌 Dashboard Summary")

            col1, col2, col3, col4 = st.columns(4)

            sales_col = "sales_amount" if "sales_amount" in df.columns else "salesamount"

            total_sales = df[sales_col].sum()
            total_orders = len(df)
            total_quantity = df["quantity"].sum()
            top_category = df.groupby("category")[sales_col].sum().idxmax()

            col1.metric("📊 Total Sales", f"₹{total_sales:,.0f}")
            col2.metric("📦 Total Orders", total_orders)
            col3.metric("🛒 Total Quantity", total_quantity)
            col4.metric("🏆 Top Category", str(top_category))

    except Exception:
        st.info("Upload a valid CSV or use a database with sales data.")

    conn.close()


show_dashboard_summary()

question = st.text_input("Enter your question")

st.info("""
Try:
• Show all products
• Top selling product in January
• Show sales by category
• Show sales by month
• Show top 5 products
• Show total sales
• Show quantity by product
""")


def run_sql(query):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


if st.button("Generate SQL"):
    if question:
        sql_query = generate_ai_sql(question)
        st.session_state.history.append(sql_query)

        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")

        if sql_query == "INVALID QUERY":
            st.error("This question cannot be answered using the available database columns.")

        else:
            try:
                result = run_sql(sql_query)

                st.subheader("Result")
                st.dataframe(result)

                st.success(f"Total Records: {len(result)}")

                if "total_sales" in result.columns and len(result.columns) >= 2:
                    st.subheader("Sales Bar Chart")
                    st.bar_chart(result.set_index(result.columns[0]))

                    st.subheader("Sales Pie Chart")
                    fig, ax = plt.subplots()
                    ax.pie(
                        result["total_sales"],
                        labels=result.iloc[:, 0],
                        autopct="%1.1f%%"
                    )
                    st.pyplot(fig)

                csv = result.to_csv(index=False)

                st.download_button(
                    "Download Result CSV",
                    csv,
                    "result.csv",
                    "text/csv"
                )

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question")


st.sidebar.title("Query History")

if st.sidebar.button("Clear History"):
    st.session_state.history = []

for q in st.session_state.history:
    st.sidebar.code(q)

st.markdown("---")
st.caption("Developed by Ranjani Hegde | Python + SQLite + Streamlit + LangChain + Gemini API")