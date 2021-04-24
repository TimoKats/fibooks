# fibooks 1.0.3
fibooks is a python library for financial statement analysis. This library (for now) supports 3 of the 4 main financial statements (balance sheet, income statement and statement of cashflows) and offers a set of formulas and ratios.
## Getting Started
fibooks can be installed using the *Python package manager*, also known as pip. If you use PyCharm (or any other IDE) then please follow their package installation guidelines. Do note that fibooks was developed using Python 3 so that's the version this package is optimized for regardless of your environment.
``` shell
pip3 install fibooks
```
Once your download is completed you can test whether fibooks has been installed sucessfully. If the following code outputs the current version then you're good to go, if not then please check your installation. If fibooks still refuses to work please let me know through the feedback form down below.
``` python
from fibooks import info

info.get_version()
```
## Documentation
### balance sheet
To create a balance sheet you must import the class and initiate it.
``` python
from fibooks import balance_sheet
my_company = balance_sheet('my company in 2021')
```

<details>
<summary>
balance sheet functions
</summary>
<ul>
  <li><b>check_identity()</b>: Checks balance sheet identity. Takes no parameters, returns boolean value</li>
  <li><b>get_assets()</b>: Gets the total value of assets. Takes no parameters, returns float value.</li> 
  <li><b>get_current_assets()</b>: Gets the total value of assets. Takes no parameters, returns float value.</li>  
  <li><b>get_longterm_assets()</b>: Gets the total value of longterm assets. Takes no parameters, returns float value.</li>  
  <li><b>get_equity()</b>: Gets the total value of equity. Takes no parameters, returns float value.</li>  
  <li><b>get_liabilities()</b>: Gets the total value of liabilities. Takes no parameters, returns float value.</li>    
  <li><b>get_current_liabilities()</b>: Gets the total value of current liabilities. Takes no parameters, returns float value. </li>
  <li><b>get_longterm_assets()</b>: Gets the total value of longterm liabilities. Takes no parameters, returns float value.</li>
  <li><b>get_field(field)</b>: Gets the value of a specific. Takes fieldname as parameter, returns field value.</li>
  <li><b>add_current_asset(field, value)</b>: Adds current asset to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li><b>add_longterm_asset(field, value)</b>: Adds longterm asset to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li><b>add_current_liability(field, value)</b>: Adds current liability to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li><b>add_longterm_liability(field, value)</b>: Adds longterm liability to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li><b>add_equity(field, value)</b>: Adds equity to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li><b>delete_current_asset(field)</b>: deletes current asset to the balance sheet. Takes fieldname as parameter, returns nothing.</li>
  <li><b>delete_longterm_asset(field)</b>: deletes longterm asset to the balance sheet. Takes fieldname as parameter, returns nothing.</li>
  <li><b>empty()</b>: Clears the current balance sheet. Takes no parameters, returns nothing.</li>
  <li><b>make()</b>: Creates the current balance sheet based on the previously given instructions. Takes no parameters, returns nothing.</li>
</ul>
</details>  
  
<details>
<summary>
file import/export functions
</summary>
<ul>
  <li><b>import_json(filename)</b>: Imports a .json file as balance sheet. Takes the filename as parameter, returns nothing.</li> 
  <li><b>export_json(filename)</b>: Exports the current balance sheet to a .json format. Takes the filename as parameter, returns nothing.</li> 
  <li><b>export_excel(filename)</b>: Exports the current balance sheet to an excel spreadsheet. Takes the filename as parameter, returns nothing.</li>  
  <li><b>export_text(filename)</b>: Exports the current balance sheet to a text file. Takes the filename as parameter, returns nothing.</li>  
</ul>   
</details>

<details>
<summary>
printing functions
</summary>
<ul>
  <li><b>print()</b>: Prints the current balance sheet to the standard output. Takes no parameters, returns nothing</li>
</ul>
</details>

---

### income statement
To create an income statement you must import the class and initiate it.
``` python
from fibooks import income_statement
my_company = income_statement('my company in 2021')
```

<details>
<summary>
income statement functions
</summary>
<ul>
  <li><b>add_revenue(field, value)</b>: Adds a revenue field to the income statement. Takes the fieldname and value as parameters, returns nothing.</li> 
  <li><b>add_expense(field, value)</b>: Adds an expense field to the income statement. Takes the fieldname and value as parameters, returns nothing.</li>  
  <li><b>delete_revenue(field)</b>: Deletes a revenue field to the income statement. Takes the fieldname as parameter, returns nothing.</li> 
  <li><b>delete_expense(field)</b>: Deletes an expense field to the income statement. Takes the fieldname as parameter, returns nothing.</li>   
  <li><b>get_revenues()</b>: Gets the total amount of revenues in the income statement. Takes no parameters, returns float value.</li> 
  <li><b>get_expenses()</b>: Adds an expense field to the income statement. Takes the fieldname and value as parameters, returns nothing.</li> 
  <li><b>get_netincome()</b>: Gets the net income of the income statement. Takes no parametes, returns float value.</li> 
  <li><b>empty()</b>: Clears the current balance sheet. Takes no parameters, returns nothing.</li>
  <li><b>make()</b>: Creates the current balance sheet based on the previously given instructions. Takes no parameters, returns nothing.</li> 
</ul>   
</details>

<details>
<summary>
file import/export functions
</summary>
<ul>
  <li><b>import_json(filename)</b>: Imports a .json file as balance sheet. Takes the filename as parameter, returns nothing.</li> 
  <li><b>export_json(filename)</b>: Exports the current balance sheet to a .json format. Takes the filename as parameter, returns nothing.</li> 
  <li><b>export_excel(filename)</b>: Exports the current balance sheet to an excel spreadsheet. Takes the filename as parameter, returns nothing.</li>  
  <li><b>export_text(filename)</b>: Exports the current balance sheet to a text file. Takes the filename as parameter, returns nothing.</li>  
</ul>   
</details>

<details>
<summary>
printing functions
</summary>
<ul>
  <li><b>print()</b>: Prints the current balance sheet to the standard output. Takes no parameters, returns nothing</li>
</ul>
</details>

---

### statement of cash flows
To create a statement of cash flows you must import the class and initiate it.
``` python
from fibooks import statement_of_cash_flows
my_company = statement_of_cash_flows('my company in 2021')
```


<details>
<summary>
statement of cash flows functions
</summary>
<ul>
  <li><b>add_operating_activity(field, value)</b>: Adds an operating activity to the statement of cash flows. Takes the fieldname and value as parameters, returns nothing.</li>
  <li><b>add_investing_activity(field, value)</b>: Adds an investing activity to the statement of cash flows. Takes the fieldname and value as parameters, returns nothing.</li> 
  <li><b>add_financing_activity(field, value)</b>: Adds an financing activity to the statement of cash flows. Takes the fieldname and value as parameters, returns nothing.</li>
  <li><b>delete_operating_activity(field)</b>: Deletes an operating activity to the statement of cash flows. Takes the fieldname as parameter, returns nothing.</li>
  <li><b>delete_investing_activity(field)</b>: Deletes an investing activity to the statement of cash flows. Takes the fieldname as parameter, returns nothing.</li> 
  <li><b>delete_financing_activity(field)</b>: Deletes an financing activity to the statement of cash flows. Takes the fieldname as parameter, returns nothing.</li> 
  <li><b>get_operating_cash()</b>: Gets the operating cash from the statement of cash flows. Takes no parameters, returns float value.</li>
  <li><b>get_investing_cash()</b>: Gets the investing cash from the statement of cash flows. Takes no parameters, returns float value.</li>
  <li><b>get_financing_cash()</b>: Gets the financing cash from the statement of cash flows. Takes no parameters, returns float value.</li>  
  <li><b>get_net_cash()</b>: Gets the net cash from the statement of cash flows. Takes no parameters, returns nothing.</li>
  <li><b>empty()</b>: Clears the current balance sheet. Takes no parameters, returns nothing.</li>
  <li><b>make()</b>: Creates the current balance sheet based on the previously given instructions. Takes no parameters, returns nothing.</li> 
</ul>   
</details>

<details>
<summary>
file import/export functions
</summary>
<ul>
  <li><b>import_json(filename)</b>: Imports a .json file as balance sheet. Takes the filename as parameter, returns nothing.</li> 
  <li><b>export_json(filename)</b>: Exports the current balance sheet to a .json format. Takes the filename as parameter, returns nothing.</li> 
  <li><b>export_excel(filename)</b>: Exports the current balance sheet to an excel spreadsheet. Takes the filename as parameter, returns nothing.</li>  
  <li><b>export_text(filename)</b>: Exports the current balance sheet to a text file. Takes the filename as parameter, returns nothing.</li>  
</ul>   
</details>

<details>
<summary>
printing functions
</summary>
<ul>
  <li><b>print()</b>: Prints the current balance sheet to the standard output. Takes no parameters, returns nothing</li>
</ul>
</details>

---

### statement of equity
This class will be added in the next update...

---

### compute
To use the built in computations you must import the class.
``` python
from fibooks import compute
```
<details>
<summary>
leverage ratios
</summary>
<ul>
  <li><b>debt_to_capital_ratio(balance_sheet)</b>: Calculates DtC-ratio. Takes a balance sheet as parameter, returns float value.</li>
  <li><b>debt_to_equity_ratio(balance_sheet)</b>: Calculates DtE-ratio. Takes a balance sheet as parameter, returns float value.</li>  
  <li><b>MB_ratio(MV_equity)</b>: Calculates the MB ratio. Takes a balance sheet and market value of equity as parameters, returns float value.</li>
</ul>
</details>

<details>
<summary>
liquidity ratios
</summary>
<ul>
  <li><b>current_ratio(balance_sheet)</b>: Calculates the current ratio. Takes a balance sheet as parameter, returns float value.</li>
  <li><b>quick_ratio(balance_sheet)</b>: Calculates the quick ratio. Takes a balance sheet as parameter, returns float value.</li>
  <li><b>cash_ratio(balance_sheet)</b>: Calculates the cash ratio. Takes a balance sheet as parameter, returns float value.</li>  
</ul>
</details>

<details>
<summary>
other
</summary>
<ul>
  <li><b>enterprise_value(MV_equity, balance_sheet)</b>: Calculates the enterprise value. Takes a balance sheet and market value of equity as parameters, returns float value</li>
  <li><b>MV_equity(stocks, stockprice)</b>: Calculates the market value of equity. Takes no. stocks and stockprice as parameters, returns float.</li>  
</ul>
</details>

## Support
[Donate](https://paypal.me/timokats)  
[Feedback](mailto:tpakats@gmail.com)  
[Pypi](https://pypi.org/project/fibooks/)
