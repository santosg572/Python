x = 1:12
y = x + round(rnorm(12, mean=0, sd=2), 2)

print(c(x,y))

plot(x,y)


