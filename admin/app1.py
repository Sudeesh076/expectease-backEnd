import sqlite3
import streamlit as st
import pandas as pd


def app(selection):
    st.title("View User Details")
    st.header("Workers and Users")

    db = sqlite3.connect(r"C:\Users\dell\Desktop\backend\expectease-backEnd\expect-ease.db")
    cursor = db.cursor()

    email_filter = st.text_input("Enter Email to Filter:")
    phone_filter = st.text_input("Enter Phone Number to Filter:")
    first_name_filter = st.text_input("Enter First Name to Filter:")
    last_name_filter = st.text_input("Enter Last Name to Filter:")

    table_selector = st.radio("Select a table", ["Users", "Workers"])
    table_name = "users" if table_selector == "Users" else "workers"

    query = f"SELECT * FROM {table_name} WHERE 1=1"
    if email_filter:
        query += f" AND email LIKE '%{email_filter}%'"
    if phone_filter:
        query += f" AND ph_number LIKE '%{phone_filter}%'"
    if first_name_filter:
        query += f" AND first_name LIKE '%{first_name_filter}%'"
    if last_name_filter:
        query += f" AND last_name LIKE '%{last_name_filter}%'"

    cursor.execute(query)
    result = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    df = df.drop('password', axis=1)

    st.dataframe(df.style.set_properties(**{'max-width': '500px'}))

    if st.button("Download CSV"):
        csv_file = df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv_file, file_name="user_details.csv", mime="text/csv")

    db.close()
