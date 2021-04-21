# fibooks by Timo Kats
# version 1.0.3
# April 2021
# income_statement.py

import json
import xlsxwriter

class income_statement:
    def __init__(self, company_name):
        # meta data
        self.company_name = company_name
        # fibooks parts
        self.revenue = {}
        self.expenses = {}
        self.income_statement = {}

    # income statement functions

    def add_revenue(self, field, value):
        self.revenue[field] = value

    def add_expense(self, field, value):
        self.expenses[field] = value

    def get_revenues(self):
        value_revenues = 0
        for item in self.income_statement:
            if item == 'revenue':
                for subitem, value in self.revenue.items():
                    value_revenues += value
        return value_revenues

    def get_expenses(self):
        value_expenses = 0
        for item in self.income_statement:
            if item == 'expenses':
                for subitem, value in self.expenses.items():
                    value_expenses += value
        return value_expenses

    def get_netincome(self):
        return self.get_revenues() - self.get_expenses()

    def delete_revenue(self, field):
        del self.revenue[field]

    def delete_expense(self, field):
        del self.expenses[field]

    def empty(self):
        self.revenue = {}
        self.expenses = {}
        self.income_statement = {}

    def make(self):
        self.income_statement['revenue'] = self.revenue
        self.income_statement['expenses'] = self.expenses

    # file import/export functions

    def import_json(self, filename):
        with open(filename) as income_statement:
            data = json.load(income_statement)
            self.revenue = data['revenue']
            self.expenses = data['expenses']

    def export_json(self, filename):
        file = open(filename, 'w+')
        file.write(str(json.dumps(self.income_statement, indent=4)))
        file.close()

    def export_excel(self, filename):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        bold = workbook.add_format({'bold': True})
        row = 0

        for item in self.income_statement:
            if item == 'revenue':
                worksheet.write(row, 0, 'revenue', bold)
                row += 1
                for sub_item, value in self.revenue.items():
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                    row += 1
            if item == 'expenses':
                worksheet.write(row, 0, 'expenses', bold)
                row += 1
                for sub_item, value in self.expenses.items():
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                    row += 1
        row += 1
        worksheet.write(row, 0, 'net income', bold)
        worksheet.write(row, 1, self.get_netincome())
        workbook.close()

    def export_text(self, filename):
        file = open(filename, 'w+')
        file.write('The income statement of ' + self.company_name)

        for item in self.income_statement:
            if item == 'revenue':
                file.write('\n' + item)
                for subitem, value in self.revenue.items():
                    file.write('\n\t' + subitem + self.get_spaces_print(subitem) + str(value))
            if item == 'expenses':
                file.write('\n' + item)
                for subitem, value in self.expenses.items():
                    file.write('\n\t' + subitem + self.get_spaces_print(subitem) + str(value))
        file.write("\nnet income\t" + self.get_spaces_print('net income') + str(self.get_netincome()))

    # printing to screen functions

    def get_spaces_print(self, item):
        spaces = 30 - len(item)
        return spaces * ' '

    def print(self):
        print('The income statement of', self.company_name)

        for item in self.income_statement:
            if item == 'revenue':
                print(item)
                for subitem, value in self.revenue.items():
                    print('\t', subitem, self.get_spaces_print(subitem), value)
            if item == 'expenses':
                print(item)
                for subitem, value in self.expenses.items():
                    print('\t', subitem, self.get_spaces_print(subitem), value)
        print("\nnet income\t", self.get_spaces_print('net income'), self.get_netincome())
