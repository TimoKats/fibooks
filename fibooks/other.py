__author__ = 'Timo Kats'
__name__ = 'other.py'
__desciption__ = 'contains the dcf and other functionalities'

import pandas as pd

def npv(cashflow, r):
    return sum(f / ((1 + r) ** i) for i, f in enumerate(cashflow, 1))

def combine_statements(statements, ignore_index=False):
    combine = {}
    for statement in statements:
        combine[statement.company_name] = statement.content
    return pd.concat(combine, ignore_index=ignore_index)   

def income_based_valuation(statement_of_cashflows, r=0):
    fcf = statement_of_cashflows.get_fcf()
    return sum(f / ((1 + r) ** i) for i, f in enumerate(fcf, 1))

def info():
    print("\n--\n")
    print("fibooks version 2.0.0")
    print("Created by Timo Kats and Alex Kobrin")
    print("\n--\n")