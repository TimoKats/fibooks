# fibooks by Timo Kats
# version 1.0.3
# April 2021
# __init__.py

import json
import xlsxwriter

try:
    from fibooks.classes.info import info
    from fibooks.classes.balance_sheet import balance_sheet
    from fibooks.classes.income_statement import income_statement
    from fibooks.classes.statement_of_cash_flows import statement_of_cash_flows
    from fibooks.classes.statement_of_equity import statement_of_equity
    from fibooks.classes.compute import compute
except:
    print('fibooks failed to load. please check your installation and version.')