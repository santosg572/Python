#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:42:58 2021

@author: santosg
"""

import subprocess 
from subprocess import PIPE

def SacaDirSub(dir=''):
 #   dir = '/Users/santosg/Desktop/Libros_may1221/' 
    data = subprocess.Popen(['ls', '-1R', dir], stdout = subprocess.PIPE) 
    res = data.communicate() 
    res = str(res[0]) 
    res = res.split('\\n') 
    
    direc = []
    for ss in res: 
        if len(ss) > 0: 
            if ss[0] == '/': 
                ss= ss.replace('//','/') 
                ss = ss[:len(ss)-1] 
                dir = ss 
            else: 
                file = dir + '/' + ss
                direc.append(file)
    
    return direc

def SacaLista_Dir_Otro(dir='', direc='0'):
    '''
    saca lista de folders o archivos de un directorio a partir del valor 
    'direc'
    
    direc = 0 - lista folders
    direc = 1 - lista archivos
    
    dir - es un path de directorio terminando con '/'
    
    SALIDA - entrega una lista de nombres

    
    '''
    
#    print(dir)
    
    data = subprocess.Popen(['ls', '-1', dir], stdout = subprocess.PIPE) 
    res = data.communicate() 
    res = str(res[0]) 
    res = res.split('\\n') 
    
    tem = res[0]
    tem = tem[2:]

    
    res[0] = tem

#    print(res)

    nn = len(res)
    
    resultado=[]
    
    for pal in res:
        if len(pal) > 1:
            tem = dir+pal
 #           print(tem)
            rr = EsDirectorio(tem)
 
            if rr[0] == direc:
                resultado.append(tem)
         
#    print(resultado)
    return resultado
            
            

def EsDirectorio(dd=''):
    '''
    valida si 'dd' es un directorio
    salida:
        0 - si es un directorio
        1 - no es directorio

    '''

    si = subprocess.run(['bash','ss.sh', dd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return si.stdout

def CreaHTML(dir=''):
    file1 = open("lib.html","a")
    
    t1 = '''<!DOCTYPE html>
    <html lang="en">
    <head>
    <title>A simple HTML document</title>
    </head>
    <body>
    '''
    
    file1.writelines(t1)
    
    res = SacaDir(dir)
    
    linea = '<br>'
    
    k = 1
    for ss in res:
        ns = len(ss)
        ss1 = ss[ns-4:]
        if ss1 == '.pdf' or ss1 == '.PDF':
            t2 = '<a href="' + ss + '"> ' + ss + ' </a>' 
            t1 = '<p' + str(k) + '/p>'
            file1.write(t1)
            file1.write(t2)  
            file1.write(linea) 
            k = k+1

        
    t3 = ''' 
    <p>Hello World!<p>
    </body>
    </html>
    ''' 
    
    file1.writelines(t3)
    
    file1.close()

def CreaHTML_delista(lista='', filename='', prefijo='no'):
    print('CreaHTML_delista')
    print(lista)
    
    pref = {'pdf': ['.pdf', '.PDF'],'no':''}
    
    file1 = open(filename,"a")
    
    t1 = '''<!DOCTYPE html>
    <html lang="en">
    <head>
    <title>A simple HTML document</title>
    </head>
    <body>
    '''
    
    file1.writelines(t1)
    
    tem = pref[prefijo]
    
    linea = '<br>'
    
    k = 1
    for ss in lista:
        ns = len(ss)
        ss1 = ss[ns-4:]
        if ss1 in tem or len(tem) == 0:
            t2 = '<a href="' + ss + '"> ' + ss + ' </a>' 
            t1 = '<p' + str(k) + '/p>'
            file1.write(t1)
            file1.write(t2)  
            file1.write(linea) 
            k = k+1

        
    t3 = ''' 
    <p>Hello World!<p>
    </body>
    </html>
    ''' 
    
    file1.writelines(t3)
    
    file1.close()
