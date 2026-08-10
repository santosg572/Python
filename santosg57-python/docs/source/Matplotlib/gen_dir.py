import matplotlib.pyplot as pld

dd = dir(pld)

for ss in dd:
  print('........................ ' + ss + ' .......................')
  help(eval('pld.'+ss))



