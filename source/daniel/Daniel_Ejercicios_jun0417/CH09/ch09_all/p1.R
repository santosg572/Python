tabla = read.csv('EXA_C09_S03_01.csv', header=T)
print(tabla)

attach(tt)

res = lm(Y~X)

print(res)

summary(res)

ym = mean(Y)

SCT = sum((Y-ym)^2)
print(SCT)

coe = res$coefficients

y0 = as.double(coe[1])
print(y0)
m = as.double(coe[2])
print(m)

yg = m*X+y0

SCR = sum((yg - ym)^2)

print(SCR)

r2 = SCR/SCT

print(r2)

SCres = sum((Y-yg)^2)

print(SCres)


CMR = SCR/1
CMres = SCres / (length(Y)-2)

RV = CMR / CMres

print(RV)

z = qf(0.95, 1, 107)

print(z)

