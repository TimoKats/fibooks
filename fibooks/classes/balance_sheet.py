# fibooks by Timo Kats
# version 1.0.3
# April 2021
# balance_sheet.py

import json
import xlsxwriter

class balance_sheet:
    def __init__(self, company_name):
        # meta data
        self.company_name = company_name
        # fibooks parts
        self.balance_sheet = {}
        self.assets = {}
        self.equity = {}
        self.liabilities = {}
        # subsets
        self.current_assets = {}
        self.longterm_assets = {}
        self.current_liabilities = {}
        self.longterm_liabilities = {}

    # balance sheet functions

    def check_identity(self):
        return self.get_assets() == self.get_equity() + self.get_liabilities()

    def get_assets(self):
        value_assets = 0
        for item in self.balance_sheet:
            if item == 'assets':
                for sub_item, value in self.current_assets.items():
                    value_assets += value
                for sub_item, value in self.longterm_assets.items():
                    value_assets += value
        return round(value_assets, 2)

    def get_equity(self):
        value_equity = 0
        for item in self.balance_sheet:
            if item == 'equity':
                for sub_item, value in self.equity.items():
                    value_equity += value
        return round(value_equity, 2)

    def get_liabilities(self):
        value_liabilities = 0
        for item in self.balance_sheet:
            if item == 'liabilities':
                for sub_item, value in self.current_liabilities.items():
                    value_liabilities += value
                for sub_item, value in self.longterm_liabilities.items():
                    value_liabilities += value
        return round(value_liabilities, 2)

    def get_current_assets(self):
        value_assets = 0
        for item in self.balance_sheet:
            if item == 'assets':
                for sub_item, value in self.current_assets.items():
                    value_assets += value
        return round(value_assets, 2)

    def get_longterm_assets(self):
        value_assets = 0
        for item in self.balance_sheet:
            if item == 'assets':
                for sub_item, value in self.longterm_assets.items():
                    value_assets += value
        return round(value_assets, 2)

    def get_current_liabilities(self):
        value_liabilities = 0
        for item in self.balance_sheet:
            if item == 'liabilities':
                for sub_item, value in self.current_liabilities.items():
                    value_liabilities += value
        return round(value_liabilities, 2)

    def get_longterm_liabilities(self):
        value_liabilities = 0
        for item in self.balance_sheet:
            if item == 'liabilities':
                for sub_item, value in self.longterm_liabilities.items():
                    value_liabilities += value
        return round(value_liabilities, 2)

    def get_field(self, field):
        for item in self.balance_sheet:
            if item == 'assets':
                for sub_item, value in self.current_assets.items():
                    if sub_item == field:
                        return value
                for sub_item, value in self.longterm_assets.items():
                    if sub_item == field:
                        return value
            if item == 'liabilities':
                for sub_item, value in self.current_liabilities.items():
                    if sub_item == field:
                        return value
                for sub_item, value in self.longterm_liabilities.items():
                    if sub_item == field:
                        return value
            if item == 'equity':
                for sub_item, value in self.equity.items():
                    if sub_item == field:
                        return value
        print('field (' + field + ') not found...')
        return 0

    def empty(self):
        # fibooks parts
        self.balance_sheet = {}
        self.assets = {}
        self.equity = {}
        self.liabilities = {}
        # subsets
        self.current_assets = {}
        self.longterm_assets = {}
        self.current_liabilities = {}
        self.longterm_liabilities = {}

    def make(self):
        # set assets
        self.assets['current_assets'] = self.current_assets
        self.assets['longterm_assets'] = self.longterm_assets
        self.balance_sheet['assets'] = self.assets
        # set liabilities
        self.liabilities['current_liabilities'] = self.current_liabilities
        self.liabilities['longterm_liabilities'] = self.longterm_liabilities
        self.balance_sheet['liabilities'] = self.liabilities
        # set equity
        self.balance_sheet['equity'] = self.equity

        if not self.check_identity():
            self.print_warning('make')

    def add_current_asset(self, field, value):
        self.current_assets[field] = value

    def add_longterm_asset(self, field, value):
        self.longterm_assets[field] = value

    def add_current_liability(self, field, value):
        self.current_liabilities[field] = value

    def add_longterm_liability(self, field, value):
        self.longterm_liabilities[field] = value

    def delete_current_asset(self, field):
        del self.current_assets[field]

    def delete_longterm_asset(self, field):
        del self.longterm_assets[field]

    def delete_current_liability(self, field):
        del self.current_liabilities[field]

    def delete_longterm_liability(self, field):
        del self.longterm_liabilities[field]

    def add_equity(self, field, value):
        self.equity[field] = value

    # file import/export functions

    def import_json(self, filename):
        with open(filename) as balance_sheet:
            data = json.load(balance_sheet)
            self.current_assets = data['assets']['current_assets']
            self.longterm_assets = data['assets']['longterm_assets']
            self.current_liabilities = data['liabilities']['current_liabilities']
            self.longterm_liabilities = data['liabilities']['longterm_liabilities']
            self.equity = data['equity']

    def export_json(self, filename):
        if not self.check_identity():
            self.print_warning('export_json')
        file = open(filename, 'w+')
        file.write(str(json.dumps(self.balance_sheet, indent=4)))
        file.close()

    def export_excel(self, filename):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 20)
        bold = workbook.add_format({'bold': True})
        row = 0

        if not self.check_identity():
            self.print_warning('export_excel')

        for item in self.balance_sheet:
            if item == 'assets':
                worksheet.write(row, 0, 'assets', bold)
                row += 1
                worksheet.write(row, 0, 'current assets', bold)
                for sub_item, value in self.current_assets.items():
                    row += 1
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                row += 1
                worksheet.write(row, 0, 'longterm assets', bold)
                for sub_item, value in self.longterm_assets.items():
                    row += 1
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                worksheet.write(row + 1, 1, self.get_assets())
            row += 1
            if item == 'liabilities':
                worksheet.write(row, 0, 'liabilities', bold)
                row += 1
                worksheet.write(row, 0, 'current liabilities', bold)
                for sub_item, value in self.current_liabilities.items():
                    row += 1
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                row += 1
                worksheet.write(row, 0, 'longterm liabilities', bold)
                for sub_item, value in self.longterm_liabilities.items():
                    row += 1
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                worksheet.write(row + 1, 1, self.get_liabilities())
            row += 1
            if item == 'equity':
                worksheet.write(row, 0, 'equity', bold)
                for sub_item, value in self.equity.items():
                    row += 1
                    worksheet.write(row, 0, sub_item)
                    worksheet.write(row, 1, value)
                worksheet.write(row + 1, 1, self.get_equity())
        workbook.close()

    def export_text(self, filename):

        file = open(filename, 'w+')

        if not self.check_identity():
            self.print_warning('export_text')

        file.write("The balance sheet of: " + self.company_name)
        for item in self.balance_sheet:
            if item == 'assets':
                file.write("\nassets\n")
                file.write("\tcurrent assets\n")
                for sub_item, value in self.current_assets.items():
                    file.write("\n\t\t" + sub_item + self.get_spaces_text(sub_item) + str(value))
                file.write("\n\tlong-term assets\n")
                for sub_item, value in self.longterm_assets.items():
                    file.write("\n\t\t" + sub_item + self.get_spaces_text(sub_item) + str(value))
                file.write("\n\t\t" + self.get_spaces_text_equity("") + "___+")
                file.write(
                    "\n\t" + "total assets" + self.get_spaces_text_equity("total assets") + str(self.get_assets()))
            if item == 'liabilities':
                file.write("\nliabilities\n")
                file.write("\tcurrent liabilities\n")
                for sub_item, value in self.current_liabilities.items():
                    file.write("\n\t\t" + sub_item + self.get_spaces_text(sub_item) + str(value))
                file.write("\n\tlong-term liabilities\n")
                for sub_item, value in self.longterm_liabilities.items():
                    file.write("\n\t\t" + sub_item + self.get_spaces_text(sub_item) + str(value))
                file.write("\n\t\t" + self.get_spaces_text_equity("") + "___+")
                file.write("\n\t" + "total liabilities" + self.get_spaces_text_equity("total liabilities") + str(
                    self.get_liabilities()))
            if item == 'equity':
                file.write("\nequity\n")
                for sub_item, value in self.equity.items():
                    file.write("\n\t" + sub_item + self.get_spaces_text_equity(sub_item) + str(value))
                file.write("\n\t\t" + self.get_spaces_text_equity("") + "___+")
                file.write(
                    "\n\t" + "total equity" + self.get_spaces_text_equity("total equity") + str(self.get_equity()))

    # printing to screen functions

    def print_warning(self, function):
        print("error in", function, ": balance sheet identity not correct!")

    def get_spaces_text(self, item):
        spaces = 40 - len(item)
        return spaces * ' '

    def get_spaces_text_equity(self, item):
        spaces = 40 - len(item)
        return (spaces * ' ') + '\t'

    def get_spaces_print(self, item):
        spaces = 30 - len(item)
        return spaces * ' '

    def get_spaces_print_equity(self, item):
        spaces = 30 - len(item)
        return (spaces * ' ') + '\t'

    def print(self):

        if not self.check_identity():
            self.print_warning('print')

        print("The balance sheet of: ", self.company_name)
        for item in self.balance_sheet:
            if item == 'assets':
                print("\nassets")
                print("\tcurrent assets")
                for sub_item, value in self.current_assets.items():
                    print("\t\t", sub_item, self.get_spaces_print(sub_item), value)
                print("\tlong-term assets")
                for sub_item, value in self.longterm_assets.items():
                    print("\t\t", sub_item, self.get_spaces_print(sub_item), value)
                print("\t\t", self.get_spaces_print_equity(""), "___+")
                print("\t", "total assets", self.get_spaces_print_equity("total assets"), self.get_assets())
            if item == 'liabilities':
                print("\nliabilities")
                print("\tcurrent liabilities")
                for sub_item, value in self.current_liabilities.items():
                    print("\t\t", sub_item, self.get_spaces_print(sub_item), value)
                print("\tlong-term liabilities")
                for sub_item, value in self.longterm_liabilities.items():
                    print("\t\t", sub_item, self.get_spaces_print(sub_item), value)
                print("\t\t", self.get_spaces_print_equity(""), "___+")
                print("\t", "total liabilities", self.get_spaces_print_equity("total liabilities"),
                      self.get_liabilities())
            if item == 'equity':
                print("\nequity")
                for sub_item, value in self.equity.items():
                    print("\t", sub_item, self.get_spaces_print_equity(sub_item), value)
                print("\t\t", self.get_spaces_print_equity(""), "___+")
                print("\t", "total equity", self.get_spaces_print_equity("total equity"), self.get_equity())
