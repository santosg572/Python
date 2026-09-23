rm(list = ls())

tabla = read.csv('EXA_C09_S03_01.csv', header=T)
print(tabla)

attach(tabla)
plot(X,Y)

res = lm(Y~X)


print(summary(res))

ym = mean(Y)
xm = mean(X)
np = length(X)

b1 = sum((X-xm) * (Y-ym)) / sum((X-xm)^2)

cat('b1 = ', b1, '\n')

b0 = ym - b1 * xm

cat('b0 = ', b0, '\n')

abline(res)

SSE = sum((Y-b0-b1*X)^2)
s2yx = SSE/(np-2)
sumx2 = sum((X-xm)^2)
sd_b0 = sqrt(s2yx * sum(X*X)/(np * sumx2))

cat ('desviacion estandard de b0: ', sd_b0, '\n')

sd_b1 = sqrt(s2yx / sumx2)

cat ('desviacion estandard de b1: ', sd_b1, '\n')

cat ('t-ratio de b0: ', b0/sd_b0, '\n')

cat ('t-ratio de b10: ', b1/sd_b1, '\n')

SS_regresion = sum((b0+b1*X-ym)^2)

cat ('SS_regresion: ', SS_regresion, '\n')

SS_Error = sum((Y - b0-b1*X)^2)

cat ('SS_Error: ', SS_Error, '\n')

SS_Total = sum((Y - ym)^2)

cat ('SS_Total: ', SS_Total, '\n')

MSR = SS_regresion / 1
MSE = SS_Error / (np-2)

cat ('MSR: ', MSR, '\n')
cat ('MSE: ', MSE, '\n')

F = MSR/MSE

cat ('F: ', F, '\n')

#--------------------------------------

# Example 9.4.1

# H0: b1 = 0

alfa = .05

F_critico = qf(1-alfa/2, 1, np-2)

cat ('F critico: ', F_critico, '\n')

#--------------------------------------------------

# Estimando el coeficiente de determinacion poblacional

r2t = 1 - sum((Y-b0-b1*X)^2) / (np-2) / (sum((Y-ym)^2)/(np-1))

cat ('R-sq(sdj): ', r2t, '\n')

#------------------------------------------------------

# Ejemplo 9.4.2


# Hipotesis: b1 = 0

cat ('b1: ', b1, '\n')
cat ('sd_b1: ', sd_b1, '\n')
te = b1/sd_b1
cat ('t : ', te, '\n')
cat ('valor critico: ', qt(1-alfa/2, np-2), '\n')

cat ('p-value: ', pt(te, np-1), '\n')

#----------------------------------------------------

# probando las suposiciones de regresion












