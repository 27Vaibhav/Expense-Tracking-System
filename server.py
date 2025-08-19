from datetime import date
from fastapi import FastAPI,Body
from typing import List

from param import DateRange
from pydantic import BaseModel
import db_helper

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date:date
    end_date:date
app = FastAPI(debug=True)

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

from fastapi import HTTPException

@app.post("/expenses/{expense_date}")
def add_or_update(expense_date: date, expenses: List[Expense] = Body(...)):
    try:
        db_helper.delete_expenses_for_date(expense_date)
        for expense in expenses:
            db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
        return {"message": "Items added Successfully"}
    except Exception as e:
        print(f"Error: {e}")  # This will print to the terminal
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analytics/")
def get_analytics(date_range : DateRange):
    data=db_helper.fetch_expense_summary_bycategory(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary from the database")

    total=sum(row['Total'] for row in data)

    breakdown={}
    for row in data:
        percentage=(row['Total']/total)*100 if total!=0 else 0
        breakdown[row['category']]={
            "total": row['Total'],
            "percentage": percentage
        }


    return breakdown

@app.get("/analytics/")
def get_analytics_bymonths():
    data=db_helper.fetch_expense_summary_by_months()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database")

    return data
