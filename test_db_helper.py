from backend import db_helper

def test_fetch_expenses_for_data():
    expense=db_helper.fetch_expenses_for_date('2024-08-15')
    assert len(expense)==1
    assert expense[0]['amount']==10
    assert expense[0]['category']=='Shopping'
    assert expense[0]['notes']=='Bought potatoes'


def test_fetch_expenses_for_data_invalid():
    expense=db_helper.fetch_expenses_for_date('9999-08-15')
    assert len(expense)==0


def test_fetch_expense_summary_bycategory_invalid():
    sumary=db_helper.fetch_expense_summary_bycategory("2099-08-05" , "2099-08-15")
    assert len(sumary)==0
