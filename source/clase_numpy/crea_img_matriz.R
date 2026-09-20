del = 10
x0 = 0
y0 = 0
nx = 5
ny = 5
cc=.8

file='img_'
fil = paste(file, nx,'_', ny,'.png', sep='')
print(fil)

png(fil)
plot(c(x0, x0+10*del), c(y0, y0+10*del))

for (x in seq(x0, x0+nx*del, del)){
  points(c(x,x), c(y0, y0+ny*del), type='l')
}

for (y in seq(y0, y0+ny*del, del)){
  points(c(x0, x0+nx*del), c(y,y), type='l')
}

x0 = 5
y0 = 5

i = 0
for (x in seq(x0, x0+(nx-1)*del, del)){
  j=0
  for (y in seq(y0, y0+(ny-1)*del, del)){
    text(x,y, paste('a(',ny-j-1,',', i,')', sep=''), cex=cc)
    j = j+1
  }
  i = i+1
}

dev.off()

