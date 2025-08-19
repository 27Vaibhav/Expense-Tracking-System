import streamlit as st
from datetime import datetime
import requests

API_URL='http://localhost:8000'

def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        expenses = response.json()

    else:
        st.error("Failed to retrieve expense")
        expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        for i in range(6):
            if len(expenses) > i:
                amount = expenses[i]["amount"]
                category = expenses[i]["category"]
                notes = expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes{i}", label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            filtered_expense = [expense for expense in expenses if expense["amount"] > 0]

            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expense)
            if response.status_code == 200:
                st.success("Successfully updated expense")
            else:
                st.error("Failed to update expense")
