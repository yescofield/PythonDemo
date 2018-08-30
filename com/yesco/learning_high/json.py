#!usr/bin/python
# -*- coding:UTF-8 -*-

import demjson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json1 = demjson.encode(data)

print json1

print demjson.decode(json1)

