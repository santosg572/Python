import seaborn as sns

dd = dir(sns)

for ss in dd:
  ss = ss.replace('\n','')
  if not(ss[0] == '_' or ss[0].isupper()):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ' + ss)
    help(eval('sns.'+ss))

 

