# coding: utf-8
"""
Использование графического модуля graph.py.
GR_LOOPS - циклы с кругами
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def row ( y ):
  x = 30
  for i in range(4):
    circle(x, y, 20)
    x += 30
    
y = 40
for k in range(3):
  row(y)
  y += 30

run()