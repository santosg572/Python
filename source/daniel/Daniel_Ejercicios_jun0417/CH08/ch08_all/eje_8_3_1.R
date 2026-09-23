A = c(7,8,9,10,11)
B = c(9,9,9,9,12)
C = c(10,10,12,12,14)

met <- c(A,B,C)
x <- rep(1:3, c(5,5,5))

bloques <- rep(1:5, 3)

boxplot(met ~ as.factor(x))

res <- aov(met ~ as.factor(x) + as.factor(bloques))

print(summary(res))

print(TukeyHSD(res))




