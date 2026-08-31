y = {'pesos':[45, 64, 70], 'edad': 65, 'nombres': ('Juan', 'Pedro')}

dd = dir(y)

for ss in dd:
  if ss[0] != '_':
    print('%%%%%%%%%%%%%%%%%%% ' + ss + ' %%%%%%%%%%%%%%%%%%%')
    print(help(eval('y.'+ss)))
    






