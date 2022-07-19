
try:
    from fibooks.balance_sheet import balance_sheet
    from fibooks.income_statement import income_statement
    from fibooks.statement_of_cashflows import statement_of_cashflows
    from fibooks.other import npv, combine_statements, income_based_valuation, info
except:
    print("something went wrong with the installation :/")