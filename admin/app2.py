import sqlite3
import streamlit as st
import pandas as pd


def app(selection):
    st.title("Remove User")
    st.header("Workers and Users")

    db = sqlite3.connect(r"C:\Users\dell\Desktop\backend\expectease-backEnd\expect-ease.db")
    cursor = db.cursor()

    selected_table = st.radio("Select a table", ["Users", "Workers"])
    table_name = "users" if selected_table == "Users" else "workers"

    id_to_remove = st.text_input("Enter ID to Remove:")
    if st.button("Remove"):
        remove_user_or_worker(table_name, id_to_remove, cursor, db)


def remove_user_or_worker(table_name, id_to_remove, cursor, db):
    check_query = f"SELECT * FROM {table_name} WHERE id = ?"
    cursor.execute(check_query, (id_to_remove,))
    existing_record = cursor.fetchone()

    if existing_record:
        delete_query = f"DELETE FROM {table_name} WHERE id = ?"
        cursor.execute(delete_query, (id_to_remove,))
        st.success(f"{table_name.capitalize()} with ID {id_to_remove} has been successfully deleted.")
        db.commit()
        db.close()
    else:
        st.error(f"{table_name.capitalize()} with ID {id_to_remove} not found.")
