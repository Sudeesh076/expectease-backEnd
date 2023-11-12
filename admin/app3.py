import sqlite3
import streamlit as st
import pandas as pd


def app(selection):
    st.title("Services")
    st.header("Workers and Users")

    db = sqlite3.connect(r"C:\Users\dell\Desktop\backend\expectease-backEnd\expect-ease.db")
    cursor = db.cursor()

    user_id_filter = st.text_input("Enter User ID:")
    worker_id_filter = st.text_input("Enter Worker ID:")
    status_filter = st.radio("Select Status Filter", ["", "Pending", "Confirm", "Started", "Open", "Closed"])
    type_filter = st.radio("Select Type Filter", ["", "ELECTRICIAN", "PLUMBER", "CARPENTER", "PAINTER"])

    query = "SELECT * FROM service WHERE 1=1"
    if user_id_filter:
        query += f" AND user_id LIKE '%{user_id_filter}%'"
    if worker_id_filter:
        query += f" AND worker_id LIKE '%{worker_id_filter}%'"
    if status_filter:
        query += f" AND status = '{status_filter}'"
    if type_filter:
        query += f" AND type = '{type_filter}'"

    cursor.execute(query)
    result = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(result, columns=columns)

    st.dataframe(df.style.set_properties(**{'max-width': '500px'}))

    if st.button("Download CSV"):
        csv_file = df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv_file, file_name="service_details.csv", mime="text/csv")

    db.close()
