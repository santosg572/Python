
me_A = c(7,8,9,10,11)
me_B = c(9,9,9,9,12)
me_C = c(10,10,12,12,14)

edad <- rep(1:5, 3)

y = c(me_A, me_B, me_C)
metodo = rep(1:3, c(5,5,5))

boxplot(y~ as.factor(metodo))

res <- aov(y~ as.factor(metodo) + as.factor(edad))
 
 print(summary(res))
 
 print(TukeyHSD(res))