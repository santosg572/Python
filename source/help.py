import tkinter as tk

#root = tk.Tk()

dd = dir(tk)

for ss in dd:
  if ss[0] != '_':
    print("%%%%%%%%%%%%%%%%%%%%% " + ss + " %%%%%%%%%%%%%%%%%%%%%")
    print(help(eval('tk.'+ss)))




