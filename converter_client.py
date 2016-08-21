#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from converter import Converter
import sys
from sigma import KnowledgeMap

con = Converter()

new_map = con.convert(sys.argv[1])

print(new_map.to_string())