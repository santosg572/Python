datos <- read.csv('EXA_C08_S04_01.csv', header=T)
attach(datos)

print(names(datos))

#"FUNC" "SUBJ" "TIME"

y = FUNC
bloque = SUBJ
x = TIME

boxplot(y ~ as.factor(x))

res <- aov(y ~ as.factor(x) + as.factor(bloque))

print(summary(res))

print(TukeyHSD(res))




