import ecommerce.sales.sales
import ecommerce.sales.sales as s
from ecommerce.sales.sales import checkout, vat

ecommerce.sales.checkout()
s.checkout()
checkout() 

# Path: Modules/sales.py
import sys
print(sys.path)

from ecommerce.sales import sales
from ecommerce.sales.sales import checkout, vat
