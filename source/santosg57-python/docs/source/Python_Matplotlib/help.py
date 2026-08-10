import matplotlib.pyplot as plt

dd = dir(plt)

for ss in dd:
  if ss[0] != '_':
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&' )
    print(help(eval('plt.'+ss)))



