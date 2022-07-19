__author__ = 'Timo Kats'
__name__ = 'statement_of_cashflows.py'
__desciption__ = 'contains the statement of cashflows class'

from fibooks.excel_parser import *
import json, pandas as pd

class statement_of_cashflows:
    def __init__(self, company_name):
        # meta data
        self.company_name = company_name
        # fibooks parts
        self.content = {}
        self.template = {
            'operations':["income taxes"], 
            'investing':["purchase of investment securities","making loans to other entities"], 
            'financing':["dividends"],
            'ignore': [
            "net cash flow from operations",
            "net cash flow from investing activities",
            "net cash flow from financing activities",
            "net cash flow",
            "beginning cash",
            "total change in cash",
            "ending cash"
            ]
            }
        self.standard_categories = {
            'operations':[], 
            'investing':[], 
            'financing':[]
            }
        self.custom_categories = {}
        self.cash_opening = 0
        
    # category functions

    def set_standard_categories(self):
        current_catagory = 'operations'
        for account in self.content:
            if account not in self.template['ignore']:
                self.standard_categories[current_catagory].append(account)
            if account in self.template['operations']:
                current_catagory = 'investing'
            elif account in self.template['investing']: 
                current_catagory = 'financing'

    def add_custom_category(self, name, accounts):
        self.custom_categories[name] = accounts

    def add_account(self, name, value, category=None):
        if category is not None:
            self.custom_categories[category] = name
        self.content[name] = value

    def delete_account(self, name):
        self.content.drop([name], axis=1, inplace=True)
        for category, accounts in self.standard_categories.items():
            for account in accounts:
                if account == name:
                    self.standard_categories[category].remove(account)
        for category in self.custom_categories:
            for account in category:
                if account == name:
                    self.standard_categories[category].remove(account)   

    # import

    def load_excel(self, filename, min_row=None, max_row=None, min_column=None, max_column=None):
        dataset = import_excel(filename, min_row, max_row, min_column, max_column)
        temp = {}
        for account, values in dataset.items():
            if account not in self.template['ignore']:
                temp[account] = values
        self.content = pd.DataFrame.from_dict(temp, orient='index').transpose()
        self.set_standard_categories()

    def load_csv(self, filename, sep=','):
        self.content = pd.DataFrame.read_csv(filename, sep=sep)
        self.set_standard_categories()

    def load_pandas(self, df):
        self.content = df
        self.set_standard_categories()       

    # calculations

    def get_total(self, category):
        total = [0] * len(self.content.index)
        for column in self.content:
            try:
                if column in self.standard_categories[category]:
                    for index, cell in enumerate(self.content[column]):
                        total[index] += self.content[column][index]
            except:
                if column in self.custom_categories[category]:
                    for index, cell in enumerate(self.content[column]):
                        total[index] += self.content[column][index]                
        return total

    def get_fcf(self, capex="capex"):
        fcf = list()
        try:
            capex_list = list(self.content[capex])
            for cpx, opr in zip(capex_list, self.get_total('operations')):
                fcf.append(opr - cpx)
        except:
            fcf = self.get_total('operations')
        return fcf

    def get_cash_change(self):
        return self.get_total('operations') + self.get_total('financing') + self.get_total('investing')

    def get_cash_close(self):
        return self.cash_opening + self.get_cash_change()

    # export

    def export_csv(self, filename):
        self.content.to_csv(filename, index=False)

    def export_pandas(self):
        return pd.DataFrame.from_dict(self.content, orient='index').transpose()

    # settings

    def set_template(self, filename):
        statement_of_cashflows_json = open(filename)
        self.template = json.load(statement_of_cashflows_json)

    def set_mapping(self, mapping):
        self.content.rename(mapping, axis=1, inplace=True)

    # convert

    def convert_excel_to_csv(self, filename_in, filename_out, min_row=None, max_row=None, min_column=None, max_column=None):
        dataset = import_excel(filename_in, min_row, max_row, min_column, max_column)
        csv = pd.DataFrame.from_dict(dataset, orient='index').transpose()
        csv.to_csv(filename_out, index=False)

    def convert_excel_to_pandas(self, filename, min_row=None, max_row=None, min_column=None, max_column=None):
        dataset = import_excel(filename, min_row, max_row, min_column, max_column)
        return pd.DataFrame.from_dict(dataset, orient='index').transpose() 