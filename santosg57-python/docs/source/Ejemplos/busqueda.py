ss = 'abbaaabbbaaabaababaabbbbbaabaa'
ns = len(ss)
i = 0

ban = 1
suma = 0
pa = 'aa'
npa = len(pa)
while ban == 1:
    i = ss.find(pa,i)
    if i < 0:
        ban = 0
    else:
        i = i+npa
        if i < len(ss):
          print(i)
          if ss[i] == 'b':
              suma = suma +1
#              print(suma)
              print(i)
          else:
              i = ss.find('b',i)
        else:
            ban = 0

print(suma)


