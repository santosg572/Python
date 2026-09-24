import matplotlib.pyplot as plt

dd = dir(plt)

for ss in dd:
  cc = ss[0]
  if not cc.isupper():
    if not (cc == '_'):
      print('&&&&&&&&&&&&&&&&&&&&&&& ' + ss )
      print(help(eval('plt.'+ss)))



