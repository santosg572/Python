x1=0
x2=100
del = 10

xx = seq(x1, x2, del)

print(xx)

plot(c(x1,x2), c(x1, x2))

for (x in xx){
  print(x)
  points(c(x,x), c(x1,x2), type='l')
}

for (x in xx){
  points(c(x1,x2), c(x,x), type='l')
}

j=0


for (x in xx){
  i=9
  for (y in xx){
    k=0
    aa = paste('a(',i,',',j,',',k,')', sep='')
    text(x+5,y+5,aa, cex=.7)
    i = i-1
  }
  j=j+1
}
