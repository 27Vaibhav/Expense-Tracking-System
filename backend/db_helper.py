import mysql.connector
from logging_setup import setup_logger
from contextlib import contextmanager
import logging


logger=setup_logger('db_helper',log_file='server.log',level=logging.DEBUG)

@contextmanager
def get_db_cursor(commit=False):
    conn = mysql.connector.connect(
        host="localhost",
        user= 'root',
        password= 'root',
        database= 'expense_manager'
    )

    cursor = conn.cursor(dictionary=True)

    yield cursor
    if commit:
        conn.commit()

    cursor.close()
    conn.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses=cursor.fetchall()
        return expenses


def delete_expenses_for_date(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date,amount,category,notes):
    logger.info(f"Inserting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date,amount,category,notes)
        )


def fetch_expense_summary_bycategory(start_date,end_date):
    logger.info(f"Fetching expense summary between {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category,SUM(amount) AS Total 
            FROM expenses WHERE expense_date
            BETWEEN %s AND %s
            GROUP BY category
            ''', (start_date,end_date)
        )

        data=cursor.fetchall()
        return data


def fetch_expense_summary_by_months():
    logger.info(f"Fetching expense summary by months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month,
            SUM(amount) AS total
            FROM expenses
            GROUP BY DATE_FORMAT(expense_date, '%Y-%m')
            ORDER BY DATE_FORMAT(expense_date, '%Y-%m');
            '''
        )

        data=cursor.fetchall()
        return data

#For checking above functions
if __name__ == '__main__':
    expenses=fetch_expenses_for_date('2024-08-30')
    print(expenses)

    #insert_expense("2024-08-25",40,"Food","Eating pizza")

    #delete_expenses_for_date("2024-08-25")

    #print(fetch_expense_summary_bycategory('2024-08-01','2024-08-05'))
