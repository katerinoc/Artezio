a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'


import xmltodict
import json
o = xmltodict.parse(a)
oi=json.dumps(o)
print(oi)

