# https://docs.python.org/3/library/json.html
import json

print(json.dumps({'chave': 'valor', 'idade': 23}, sort_keys=True, indent=4))

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
