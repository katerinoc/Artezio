"""task 5"""

import re

regexpression = r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9_*%&]{8,12}'

print(re.search(regexpression, 'aJdfA4d0fl'))