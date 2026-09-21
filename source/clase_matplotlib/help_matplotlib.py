import matplotlib.pyplot as plt

#dd = dir(plt)

dd = ['bar', 'colormaps', 'draw', 'hist', 'errorbar','imsave', 'stem', 'plot', 'boxplot',  'imread', 'imshow', 'show', 'violinplot', 'time']

for ss in dd:
  print('&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&')
  print(help(eval('plt.'+ss)))



