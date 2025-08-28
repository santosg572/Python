ss = c('a', 'b')

mm = sample(ss, 1000, replace=T, prob=c(.4, .6))

pp = paste(mm, collapse="" )

print(pp)

