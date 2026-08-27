import turtle

dd = dir(turtle)

for ss in dd:
  if ss[0] != '_':
    print(ss)

#    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ' + ss + ' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#    print(help('turtle.'+ss))




