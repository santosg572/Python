h = paste('Juan', 1:20, sep='')
m = paste('Lupita', 1:20, sep='')

nombres = c(h, m)

nombres = sample(nombres, 20)

print(nombres)

peso = round(rnorm(20, mean=57, sd=5))
edad = round(runif(20, min=57, max=70))

datos = data.frame(nombres, peso, edad)

print(datos)

write.csv(datos, 'datos.csv', row.names = FALSE)


