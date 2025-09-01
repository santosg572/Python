pp = c('A', 'B')

ss = sample(pp, 5000, replace=T, prob=c(.4, .6))

ss = paste(ss, collapse='')

print(ss)


