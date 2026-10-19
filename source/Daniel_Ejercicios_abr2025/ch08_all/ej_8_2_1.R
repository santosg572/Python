datos <- read.csv('EXA_C08_S02_01.csv', header=T)
print(names(datos))

attach(datos)

ven <- VEN[!is.na(VEN)]
squ <- SQU[!is.na(SQU)]
rrb <- RRB[!is.na(RRB)]
nrb <- NRB[!is.na(NRB)]

n1 = length(ven)
n2 = length(squ)
n3 = length(rrb)
n4 = length(nrb)

carne = c(ven, squ, rrb, nrb)
fac = as.factor(c(rep(1, n1), rep(2, n2),rep(3, n3),rep(4, n4)))

boxplot(carne ~ fac)

res <- aov(carne ~ fac)

print(summary(res))

print(TukeyHSD(res))

