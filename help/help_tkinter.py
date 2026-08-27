from tkinter import *
from tkinter import ttk

dd = dir(ttk)

for ss in dd:
  if ss[0] != '_':
     print(ss)
#     print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ' + ss + ' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#     print(help('turtle.'+ss))




