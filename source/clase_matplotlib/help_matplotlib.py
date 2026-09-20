import matplotlib.pyplot as plt

#dd = dir(plt)

dd = ['stem', 'plot', 'boxplot',  'imread', 'imshow']

for ss in dd:
  print('&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&')
  print(help(eval('plt.'+ss)))



