datos <- read.csv('EXA_C09_S03_01.csv', header=T)

print(names(datos))

attach(datos)

plot(X, Y, pch=16)

res <- lm(Y ~ X, data=datos)

print(summary(res))

abline(res)



