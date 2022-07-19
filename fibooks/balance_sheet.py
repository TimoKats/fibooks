__author__ = 'Timo Kats'
__name__ = 'balance_sheet.py'
__desciption__ = 'contains the statement of cashflows class'

from fibooks.excel_parser import *
import json, pandas as pd

class balance_sheet:
    def __init__(self, company_name):
        # meta data
        self.company_name = company_name
        # fibooks parts
        self.content = {}
        self.template = {
            'current assets':["other"],
            'longterm assets':["less accumulated depreciation"], 
            'current liabilities':["other"], 
            'longterm liabilities':["mortgage payable"], 
            'equity':["accumulated retained earnings"],
            'ignore': [        
            "total current assets",
            "total fixed assets",
            "total long-term liabilities",
            "total owner's equity"]
            }
        self.standard_categories = {
            'current assets':[],
            'longterm assets':[], 
            'current liabilities':[], 
            'longterm liabilities':[], 
            'equity':[]
            }
        self.custom_categories = {}
        
    # category functions

    def set_standard_categories(self):
        current_catagory = 'current assets'
        for account in self.content:
            if account not in self.template['ignore']:
                self.standard_categories[current_catagory].append(account)
            if account in self.template['current assets']:
                current_catagory = 'longterm assets'
            elif account in self.template['longterm assets']: 
                current_catagory = 'current liabilities'
            elif account in self.template['current liabilities']:
                current_catagory = 'longterm liabilities'
            elif account in self.template['longterm liabilities']:
                current_catagory = 'equity'

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

    # ratios

    def current_ratio(self):
        current_ratio = list()
        for ca, cl in zip(self.get_total('current assets'), self.get_total('current liabilities')):
            cr = ca / cl
            current_ratio.append(cr)
        return current_ratio

    def custom_ratio(self, category1, catagory2):
        custom_ratio = list()
        for c1, c2 in zip(self.get_total(category1), self.get_total(catagory2)):
            cr = c1 / c2
            custom_ratio.append(cr)
        return custom_ratio

    def load_pandas(self, df):
        self.content = df
        self.set_standard_categories()  

    # export

    def export_csv(self, filename):
        self.content.to_csv(filename, index=False)

    def export_pandas(self):
        return pd.DataFrame.from_dict(self.content, orient='index').transpose()

    # settings

    def set_template(self, filename):
        balance_sheet_json = open(filename)
        self.template = json.load(balance_sheet_json)

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
