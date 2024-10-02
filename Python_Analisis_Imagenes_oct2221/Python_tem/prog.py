import ana 

img = ana.LeeImg('img.jpg')

ana.DespliegaImg(img, 'original')

imgR = ana.GeneraRuido(img, .20)

ana.DespliegaImg(imgR, 'RUIDO')

imgF = ana.FiltroMediano(imgR)   

ana.DespliegaImg(imgF, 'FILTRADO')  

