nombres = paste('juan',1:20, sep='')
altura = round(runif(20, min= 50, max = 70),2)
peso = round(rnorm(20, mean= 65, sd = 5),2)

datos <- data.frame(nombres, altura, peso)
write.csv(datos, 'altura_peso.csv')


