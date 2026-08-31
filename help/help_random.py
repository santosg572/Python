import random

dd = dir(random)

#print(dd)


dd = ['betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

for ss in dd:
  if ss[0] != '_':
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ' + ss + ' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(help('random.'+ss))



