#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def my_abs(x):
	x = int(x)
	if x >= 0:
		return  x
	else:
		return -x
x = raw_input('plase input a num:')
print x,'的绝对值为', my_abs(x)

