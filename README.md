# fibooks 1.0.3
fibooks is a python library for financial statement analysis. This library (for now) supports 3 of the 4 main financial statements (balance sheet, income statement and statement of cashflows) and offers a set of formulas and ratios. 
### Getting Started
---
fibooks can be installed using the *Python package manager*, also known as pip. If you use PyCharm (or any other IDE) then please follow their package installation guidelines. Do note that fibooks was developed using Python 3 so that's the version this package is optimized for regardless of your environment.
``` shell
pip3 install fibooks
```
Once your download is completed you can test whether fibooks has been installed sucessfully. If the following code outputs the current version then you're good to go, if not then please check your installation. If fibooks still refuses to work please let me know through the feedback form down below.
``` python
from fibooks import info

info.get_version()
```
### Documentation
---
#### balance sheet
To create a balance sheet you must import the class and initiate it. The only parameter that this class takes is the name of the balance sheet you want to make.

``` python
from fibooks import balance_sheet
my_company = balance_sheet('my company in 2021')
```
The balance sheet class has the following attributes:
<details>
<summary>
balance sheet functions
</summary>
<ul>
  <li>check_identity(): Checks balance sheet identity. Takes no parameters, returns boolean value</li>
  <li>get_assets(): Gets the total value of assets. Takes no parameters, returns rounded float value.</li> 
  <li>get_current_assets(): Gets the total value of assets. Takes no parameters, returns rounded float value.</li>  
  <li>get_longterm_assets(): Gets the total value of longterm assets. Takes no parameters, returns rounded float value.</li>  
  <li>get_equity(): Gets the total value of equity. Takes no parameters, returns rounded float value.</li>  
  <li>get_liabilities(): Gets the total value of liabilities. Takes no parameters, returns rounded float value.</li>    
  <li>get_current_liabilities(): Gets the total value of current liabilities. Takes no parameters, returns rounded float value. </li>
  <li>get_longterm_assets(): Gets the total value of longterm liabilities. Takes no parameters, returns rounded float value.</li>
  <li>get_field(field): Gets the value of a specific. Takes fieldname as parameter, returns field value.</li>
  <li>add_current_asset(field, value): Adds current asset to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li>add_longterm_asset(field, value): Adds longterm asset to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li>add_current_liability(field, value): Adds current liability to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li>add_longterm_liability(field, value): Adds longterm liability to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li>add_equity(field, value): Adds equity to the balance sheet. Takes fieldname and value as parameter, returns nothing.</li>
  <li>delete_current_asset(field): deletes current asset to the balance sheet. Takes fieldname as parameter, returns nothing.</li>
  <li>delete_longterm_asset(field): deletes longterm asset to the balance sheet. Takes fieldname as parameter, returns nothing.</li>
  <li>empty(): Clears the current balance sheet. Takes no parameters, returns nothing.</li>
  <li>make(): Creates the current balance sheet based on the previously given instructions. Takes no parameters, returns nothing.</li>
</ul>
</details>  
  
<details>
<summary>
file import/export functions
</summary>
<h1>test</h1>
    
</details>
<details>
<summary>
printing functions
</summary>
<h1>test</h1>
</details>

#### income statement
#### statement of equity
#### statement of cash flows
#### compute

### Support
---
[Donate](https://paypal.me/timokats)  
[Feedback](mailto:tpakats@gmail.com)
