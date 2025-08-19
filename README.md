# 💰 Expense Tracking System

An end-to-end Python project for managing and analyzing personal expenses.  
This system uses **FastAPI** as the backend, **MySQL** for database storage, and **Streamlit** for the frontend interface.  
It supports expense management, category-wise summaries, and testing with Postman and Pytest.

---

## 🚀 Features

- 📌 Add, view, and manage expenses  
- 📊 Get category-wise expense summaries  
- 🗓️ Fetch expenses by specific dates  
- 🔗 RESTful API built with **FastAPI**  
- 🗃️ Database interaction with **MySQL**  
- 📑 Input validation with **Pydantic**  
- 🧪 Unit testing with **Pytest**  
- 🖥️ Interactive dashboard with **Streamlit**  
- 📝 Logging for debugging and tracking  

---

## 🛠️ Tech Stack

- **Backend**: FastAPI  
- **Database**: MySQL  
- **Frontend**: Streamlit  
- **Testing**: Pytest, Postman  
- **Other Tools**: Pydantic, Logging, Context Managers  

---

## 📂 Project Structure
'''
expense-tracking-system/
│── backend/
│ ├── db_helper.py # Handles database operations
│ ├── server.py # FastAPI server application
│ ├── logging_setup.py # Logging configuration
│
│── frontend/
│ ├── app.py # Main Streamlit app
│ ├── add_update_ui.py # UI for adding/updating expenses
│ ├── analytics_category_ui.py # UI for category-wise analytics
│ ├── analytics_month_ui.py # UI for monthly analytics
│
│── tests/
│ ├── test_db_helper.py # Pytest unit tests
│ ├── conftest.py # Pytest fixtures (if needed)
│
│── requirements.txt # Dependencies
│── README.md # Project documentation
'''


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
git clone https://github.com/your-username/expense-tracking-system.git
cd expense-tracking-system


### 2️⃣ Create and activate virtual environment
python -m venv venv


### 3️⃣ Install dependencies
pip install -r requirements.txt


### 5️⃣ Run FastAPI backend
uvicorn server:app --reload

API will be available at:  
👉 [**http://127.0.0.1:8000**](http://127.0.0.1:8000)

### 6️⃣ Test API with Postman
- Import API endpoints  
- Test CRUD operations  

### 7️⃣ Run Streamlit frontend
streamlit run frontend/app.py

## 🧪 Running Tests
pytest

## 📸 Screenshots
Screenshots of the application are uploaded in the repository:
Streamlit App – User-friendly interface for expense tracking


