#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) != 2:
  print('Missing arg')
  sys.exit()

file_path = sys.argv[1]

cpu = CPU()

cpu.load(file_path)
cpu.run()