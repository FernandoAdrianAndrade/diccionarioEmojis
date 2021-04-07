''' Nota: este proceso solo esta funcionando para la pagina usada debido a la estructura en la que esta guardada, 
es un trabajo sencillo que ayuda a hacer web scrapping de la pagina https://es.piliapp.com/twitter-symbols/ '''

import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

pagina = requests.get('https://es.piliapp.com/twitter-symbols/') #Obtenemos la pagina web con emojis

sopa = BeautifulSoup(pagina.text, 'html.parser') #Creamos el objeto de beautifulSoup

emojis = sopa.find_all(class_= 'emojis') #Buscamos todos los que tengan la clase emoji en esa pagina.

#Asignamos aqui solo los que tienen emojis de una categoria en especial.

emojis_persona = emojis[1] 
emojis_animales = emojis[2]
emojis_comida = emojis[3]
emojis_actividades = emojis[4]
emojis_viajes = emojis[5]
emojis_objetos = emojis[6]
emojis_simbolos = emojis[7]
emojis_banderas = emojis[8]

def sacar_codigos(texto_de_donde_sacar):
    emojis_codigo = re.findall('class="emoji \w+-?\w+-?\w+-?\w+-?\w+-?\w+-?\w+', str(texto_de_donde_sacar)) #Encontramos con expresiones regulares las cadenas de clase, esta es la buena
    emojis_codigo_puro=[]   #En esta lista solo iremos guardando todos los codigos
    for codigo in emojis_codigo:    #Este ciclo ira recorriendo todas las cadenas y extrayendo solo los codigos
        emojis_codigo_puro.append(str(re.sub('class="emoji emoji','',codigo)))   #Aqui estamos extrayendo los codigos y metiendolos a la lista
    
    return emojis_codigo_puro   #Cuando acabo le regresamos los puros codigos




def escribir_codigos(nombre_documento,texto_de_donde_sacar2):   #Esta funcion solo escribira los archivos.
   
    escritor=pd.ExcelWriter('diccionarioEmojis.xlsx')
    df=pd.DataFrame()
    df['codigo'] = sacar_codigos(texto_de_donde_sacar=texto_de_donde_sacar2)
    df.to_excel(excel_writer=escritor,sheet_name=nombre_documento, index=False)


escribir_codigos('personas',emojis_persona)
escribir_codigos('animales',emojis_animales)
escribir_codigos('comida',emojis_comida)
escribir_codigos('actividades',emojis_actividades)
escribir_codigos('viajes',emojis_viajes)
escribir_codigos('objetos',emojis_objetos)
escribir_codigos('simbolos',emojis_simbolos)
escribir_codigos('banderas',emojis_banderas)




'''
Por favor ignora todo esto que esta comentado, eran maneras distintas de realizar el mismo proceso.



def sacar_codigos(texto_de_donde_sacar, numero_hoja):
    emojis_codigo = re.findall('class="emoji \w+"', str(texto_de_donde_sacar)) #Encontramos con expresiones regulares las cadenas de clase.


    df = pd.DataFrame()
    codigos_personas=[]
    imagenes_personas=[]

    for codigo in emojis_codigo: #Aqui solo estamos obteniendo los codigos 
        codigos_personas.append(re.sub('"','',re.sub('emoji','',re.sub('class="emoji ','',str(codigo)))))




    df['codigo'] = codigos_personas

    df.to_excel(encoding='UTF-16',excel_writer='/Users/fernandoandrade/Desktop/DiccionarioEmojis/personas.xlsx',sheet_name='Hoja'+str(numero_hoja), index=False)


sacar_codigos(emojis_persona,1)

'''



'''

emojis_codigo = re.findall('class="emoji \w+"', str(emojis_persona)) #Encontramos con expresiones regulares las cadenas de clase.


df = pd.DataFrame()
codigos_personas=[]
imagenes_personas=[]

for codigo in emojis_persona_codigo: #Aqui solo estamos obteniendo los codigos 
    codigos_personas.append(re.sub('"','',re.sub('emoji','',re.sub('class="emoji ','',str(codigo)))))




df['codigo'] = codigos_personas

df.to_excel(encoding='UTF-16',excel_writer='/Users/fernandoandrade/Desktop/DiccionarioEmojis/personas.xlsx',sheet_name='Sheet1', index=False)
'''