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
#### income statement
#### statement of equity
#### statement of cash flows
#### compute

### Support
---
[Donate](https://paypal.me/timokats)  
[Feedback](mailto:tpakats@gmail.com)
