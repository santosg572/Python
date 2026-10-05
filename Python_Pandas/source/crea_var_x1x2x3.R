nombres = paste('juan',1:20, sep='')
x1 = round(rnorm(20, mean= 55, sd = 7),2)
x2 = round(rnorm(20, mean= 58, sd = 5),2)
x3 = round(rnorm(20, mean= 60, sd = 4),2)

print(nombres)
print(x1)
print(x2)
print(x3)

datos <- data.frame(nombres, x1, x2, x3)
write.csv(datos, 'x1x2x3.csv')


