#!/usr/bin/env python3
import yaml
def safe_load_all(fn): return yaml.safe_load_all(open(fn if fn.endswith('.yml') else fn+'.yml').read())
print(list(safe_load_all('data')))
