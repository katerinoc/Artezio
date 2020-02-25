"""task 4"""

import re


regexpression = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
print(re.findall(regexpression, "2020-02-24T14:03:09 right now"))
