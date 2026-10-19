datos <- read.csv("EXA_C08_S04_01.csv", header=T)

print(datos)

attach(datos)

y = FUNC
trat = TIME
sub = SUBJ

boxplot(y ~ as.factor(trat))

res <- aov(y ~ as.factor(trat)+as.factor(sub))

print(summary(res))

print(TukeyHSD(res))