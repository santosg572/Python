vec_columna <- function(){
  y = seq(0,100,10)

  plot(c(0,100),c(0,100))

  points(c(0,0), c(0,100), type='l', lwd=2)
  points(c(10,10), c(0,100), type='l', lwd=2)

  for (yy in y){
    points(c(0, 10), c(yy,yy), type='l', lwd=2)
  }

  i = 9
  del1 = 5
  y=y[1:10]

  for (yy in y){
    ss = paste('a(',i,')')
    text(0+del1, yy+del1, ss)
    i = i-1
  }
}


vec_fila <- function(){
  x = seq(0,100,10)

  print(x)

  plot(c(0,100),c(0,100))

  points(c(0,100), c(0,0), type='l', lwd=2)
  points(c(0,100), c(10,10), type='l', lwd=2)

  for (xx in x){
    points(c(xx,xx), c(0,10), type='l', lwd=2)
  }

  i = 0
  del1 = 5
  x=x[1:10]

  for (xx in x){
    ss = paste('a(',i,')')
    text(xx+del1,0+del1, ss)
    i = i+1
  }
}

matriz <- function(){
  x = seq(0,100,10)

  plot(c(0,100),c(0,100))

  for (xx in x){
    points(c(xx,xx), c(0,100), type='l', lwd=2)
  }

  for (xx in x){
    points(c(0,100), c(xx,xx), type='l', lwd=2)
  }

  j = 0
  del1 = 5
  x=x[1:10]

  y1 = 90

i=0
  for (yy in x){
 
  j=0
  for (xx in x){
    ss = paste('a(',i,',',j,')', sep='')
    text(xx+del1,y1+del1, ss)
    j = j+1
  }
  y1 = y1 - 10
  i = i+1
  }
}

volumen <- function(){
  x = seq(0,100,10)
     
  plot(c(0,100),c(0,100))
    
  for (xx in x){
    points(c(xx,xx), c(0,100), type='l', lwd=2)
  }
  
  for (xx in x){
    points(c(0,100), c(xx,xx), type='l', lwd=2)
  }
  
  j = 0
  del1 = 5
  x=x[1:10]
  
  y1 = 90
   
k = 2

i=0
  for (yy in x){
     
  j=0
  for (xx in x){
    ss = paste('a(',i,',',j,',',k,')', sep='')
    text(xx+del1,y1+del1, ss, cex=.7)
    j = j+1
  }
  y1 = y1 - 10
  i = i+1
  }
} 


#vec_fila()
#vec_columna()
#matriz()
volumen()




