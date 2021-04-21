# fibooks by Timo Kats
# version 1.0.3
# April 2021
# statement_of_cash_flows.py

import json
import xlsxwriter

class statement_of_cash_flows:
    def __init__(self, company_name):
        # meta data
        self.company_name = company_name
        # fibooks parts
        self.operating = {}
        self.investing = {}
        self.financing = {}
        self.statement_of_cash_flows = {}

    # statement of cash flows functions

    def add_operating_activity(self, field, value):
        self.operating[field] = value

    def add_investing_activity(self, field, value):
        self.investing[field] = value

    def add_financing_activity(self, field, value):
        self.financing[field] = value

    def get_operating_cash(self):
        value_operating_cash = 0
        for item, value in self.operating.items():
            value_operating_cash += value
        return value_operating_cash

    def get_investing_cash(self):
        value_investing_cash = 0
        for item, value in self.investing.items():
            value_investing_cash += value
        return value_investing_cash

    def get_financing_cash(self):
        value_financing_cash = 0
        for item, value in self.financing.items():
            value_financing_cash += value
        return value_financing_cash

    def get_net_cash(self):
        return self.get_operating_cash() + self.get_investing_cash() + self.get_financing_cash()

    def delete_operating_activity(self, field):
        del self.operating[field]

    def delete_investing_activity(self, field):
        del self.investing[field]

    def delete_financing_activity(self, field):
        del self.financing[field]

    def empty(self):
        self.operating = {}
        self.investing = {}
        self.financing = {}
        self.statement_of_cash_flows = {}

    def make(self):
        self.statement_of_cash_flows['operating'] = self.operating
        self.statement_of_cash_flows['investing'] = self.investing
        self.statement_of_cash_flows['financing'] = self.financing

    # file import/export functions

    def import_json(self, filename):
        with open(filename) as statement_of_cash_flows:
            data = json.load(statement_of_cash_flows)
            self.operating = data['operating']
            self.investing = data['investing']
            self.financing = data['financing']

    def export_json(self, filename):
        file = open(filename, 'w+')
        file.write(str(json.dumps(self.statement_of_cash_flows, indent=4)))
        file.close()

    def export_excel(self, filename):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        bold = workbook.add_format({'bold': True})
        row = 0

        for item in self.statement_of_cash_flows:
            if item == 'operating':
                worksheet.write(row, 0, 'operating activities', bold)
                row += 1
                for sub_item, value in self.operating.items():
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                    row += 1
            if item == 'investing':
                worksheet.write(row, 0, 'investing activities', bold)
                row += 1
                for sub_item, value in self.investing.items():
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                    row += 1
            if item == 'financing':
                worksheet.write(row, 0, 'financing activities', bold)
                row += 1
                for sub_item, value in self.financing.items():
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                    row += 1
        row += 1
        worksheet.write(row, 0, 'change in cash', bold)
        worksheet.write(row, 1, self.get_net_cash())
        workbook.close()

    def export_text(self, filename):

        file = open(filename, 'w+')

        file.write('The income statement of ' + self.company_name)

        for item in self.statement_of_cash_flows:
            if item == 'operating':
                file.write('\n' + item)
                for subitem, value in self.operating.items():
                    file.write('\n\t' + subitem + self.get_spaces_print(subitem) + str(value))
            if item == 'investing':
                file.write('\n' + item)
                for subitem, value in self.investing.items():
                    file.write('\n\t' + subitem + self.get_spaces_print(subitem) + str(value))
            if item == 'financing':
                file.write('\n' + item)
                for subitem, value in self.financing.items():
                    file.write('\n\t' + subitem + self.get_spaces_print(subitem) + str(value))
        file.write("\nnchange in cash\t" + self.get_spaces_print('change in cash') + str(self.get_net_cash()))

    # printing to screen functions

    def get_spaces_print(self, item):
        spaces = 30 - len(item)
        return spaces * ' '

    def print(self):
        print('The statement of cash flows of', self.company_name)

        for item in self.statement_of_cash_flows:
            if item == 'operating':
                print(item)
                for subitem, value in self.operating.items():
                    print('\t', subitem, self.get_spaces_print(subitem), value)
            if item == 'investing':
                print(item)
                for subitem, value in self.investing.items():
                    print('\t', subitem, self.get_spaces_print(subitem), value)
            if item == 'financing':
                print(item)
                for subitem, value in self.financing.items():
                    print('\t', subitem, self.get_spaces_print(subitem), value)
        print("\nchange in cash\t", self.get_spaces_print('change in cash'), self.get_net_cash())