datos <- read.csv('EXA_C08_S02_01.csv', header=T)

print(names(datos))

attach(datos)

#"VEN" "SQU" "RRB" "NRB"

v1 <- VEN[!is.na(VEN)]
v2 <- SQU[!is.na(SQU)]
v3 <- RRB[!is.na(RRB)]
v4 <- NRB[!is.na(NRB)]

y = c(v1, v2, v3, v4)
x = c(rep(1, length(v1)), rep(2, length(v2)),rep(3, length(v3)),rep(4, length(v4)))

boxplot(y ~ as.factor(x))

res <- aov(y ~ as.factor(x))

print(summary(res))

print(TukeyHSD(res))

 



