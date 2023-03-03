import ecommerce.shipping
import ecommerce.tax
print(ecommerce.shipping.calc_shipping())
print(ecommerce.tax.calc_tax())

# ----------------------- OR -----------------------

from ecommerce import shipping, tax
print(shipping.calc_shipping())
print(tax.calc_tax())

# ----------------------- OR -----------------------

from ecommerce.shipping import calc_shipping, send_shipping
from ecommerce.tax import calc_tax
print(calc_shipping())
print(send_shipping())
print(calc_tax())
