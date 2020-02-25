"""task 6"""

import re

regexpression = r"^.*(\w{3,})(.*\1){4,}.*\?$"

print(re.search(regexpression,"none none none none none ?"))