# fibooks by Timo Kats and Alexandre Kobrin
# version 1.0.3
# April 2021
# compute.py

class compute:

    # leverage ratios

    def debt_to_capital_ratio(balance_sheet):
        return round((balance_sheet.get_liabilities() / (balance_sheet.get_equity() + balance_sheet.get_liabilities())), 2)

    def debt_equity_ratio(balance_sheet):
        return round(((balance_sheet.get_liabilities() - balance_sheet.get_field('cash')) / (balance_sheet.get_equity() + balance_sheet.get_liabilities())), 2)

    def MB_ratio(MV_equity, balance_sheet):
        return round(MV_equity / balance_sheet.get_equity(),2)

    # liquidity ratios

    def current_ratio(balance_sheet):
        return round(balance_sheet.get_current_assets() / balance_sheet.get_current_liabilities(), 2)

    def quick_ratio(balance_sheet):
        return round((balance_sheet.get_field('cash') + balance_sheet.get_field('accounts recievable')) / balance_sheet.get_current_liabilities(), 2)

    def cash_ratio(balance_sheet):
        return round(balance_sheet.get_field('cash') / balance_sheet.get_current_liabilities(), 2)

    # other

    def enterprise_value(MV_equity, balance_sheet):
        return MV_equity + balance_sheet.get_liabilities() - balance_sheet.get_field('cash')

    def MV_equity(stocks, stockprice):
        return round(stocks * stockprice, 2)
