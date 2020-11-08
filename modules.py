# Modules are files containing a set of functions to include in your app. There are core python modules, modules you can install using the pip package manager (including Django)
#as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

#pip module
from camelcase import CamelCase


# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

print(timestamp)