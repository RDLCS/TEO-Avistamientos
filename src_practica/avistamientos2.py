import csv
from typing import NamedTuple,List,Dict,DefaultDict,Tuple,Optional,Set
from datetime import datetime,date,time,timedelta
from math import radians, sin, cos, asin, sqrt,pi
from collections import namedtuple, Counter, defaultdict
import locale
import statistics

coordenadas=NamedTuple('coordenadas',[('latitud',float),('longitud',float)])

avistamiento=NamedTuple('avistamiento',[('fecha_hora',datetime),('ciudad',str),('estado',str),('forma',str),('duracion',int)
                                        ,('comentarios',str),('ubicacion',coordenadas)])

def lee_avistamientos(ruta:str)->List[avistamiento]:
    lista=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        iter=csv.reader(f)
        next(iter)
        for fecha_hora,ciudad,estado,forma,duracion,comentarios,latitud,longitud in iter:
            fecha_hora=datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ubicacion=coordenadas(float(latitud),float(longitud))
            duracion=int(duracion)
            lista.append(avistamiento(fecha_hora,ciudad,estado,forma,duracion,comentarios,ubicacion))
    return lista

def numero_avistamientos_fecha(av:List[avistamiento],fecha:datetime)->List[avistamiento]:
    lista=list()
    for a in av:
        fecha2=a.fecha_hora.date()
        if fecha==fecha2:
            lista.append(a)
    return lista

def numero_avistamientos_fecha2(av:List[avistamiento],fecha:datetime)->List[avistamiento]:
    lista=list(a for a in av if a.fecha_hora.date()==fecha)
    return lista

def formas_estados(av:List[avistamiento],estados:set)->int:
    conjunto=set()
    for a in av:
        if a.estado in estados:
            conjunto.add(a.forma)
    return len(conjunto)

def formas_estados2(av:List[avistamiento],estados:set)->int:
    conjunto=set(a.forma for a in av if a.estado in estados)
    return len(conjunto)

def duracion_total(av:List[avistamiento],estado:str)->int:
    suma=0
    for a in av:
        if a.estado==estado:
            suma+=a.duracion
    return suma

def duracion_total2(av:List[avistamiento],estado:str)->int:
    suma=list(a.duracion for a in av if a.estado==estado)
    return sum(suma)

def conversion_radianes(coord:coordenadas)->coordenadas:
    latitud=coord[0]*pi/180
    longitud=coord[1]*pi/180
    return coordenadas(latitud,longitud)

def calcular_distancia(coord1:coordenadas,coord2:coordenadas)->float:
    coord1=conversion_radianes(coord1)
    coord2=conversion_radianes(coord2)
    inc_lat=coord2.latitud-coord1.latitud
    inc_long=coord2.longitud-coord1.longitud
    a=(sin(inc_lat/2)**2) + (cos(coord1.latitud)*cos(coord2.latitud)*(sin(inc_long/2)**2))
    distancia=2*6371*asin(sqrt(a))
    return distancia

def avistamientos_cercanos_ubicacion(av:List[avistamiento],ubicacion:coordenadas,radio:float)->Set[avistamiento]:
    conjunto=set()
    for a in av:
        distancia=calcular_distancia(ubicacion,a.ubicacion)
        if distancia<=radio:
            conjunto.add(a)
    return conjunto

def avistamientos_cercanos_ubicacion2(av:List[avistamiento],ubicacion:coordenadas,radio:float)->Set[avistamiento]:
    return set(a for a in av if radio>=calcular_distancia(ubicacion,a.ubicacion))

def avistamiento_mayor_duracion(av:List[avistamiento],forma:str)->avistamiento:
    lista=list()
    for a in av:
        if a.forma==forma:
            lista.append(a)
    return max(lista, key=lambda e:e.duracion)

def avistamiento_mayor_duracion2(av:List[avistamiento],forma:str)->avistamiento:
    return max(list(a for a in av if a.forma==forma), key=lambda e:e.duracion)

def avistamiento_cercano_mayor_duracion(av:List[avistamiento],radio:float,ubicacion:coordenadas)->Tuple[int,str]:
    conj=avistamientos_cercanos_ubicacion2(av,ubicacion,radio)
    maximo=max(conj,key=lambda e:e.duracion)
    return (maximo.duracion,maximo.comentarios)

def avistamiento_cercano_mayor_duracion2(av:List[avistamiento],radio:float,ubicacion:coordenadas)->Tuple[int,str]:
    maximo=max(avistamientos_cercanos_ubicacion2(av,ubicacion,radio),key=lambda e:e.duracion)
    return (maximo.duracion,maximo.comentarios)

def avistamiento_fechas(av:List[avistamiento],fecha1:Optional[date]=None,fecha2:Optional[date]=None)->List[avistamiento]:
    return sorted(list(a for a in av if (fecha1==None or a.fecha_hora.date()>=fecha1) and 
                       (fecha2==None or a.fecha_hora.date()<=fecha2)),key=lambda e:e.fecha_hora, reverse=True)

def comentario_mas_largo(av:List[avistamiento],palabra:str,año:int)->avistamiento:
    lista=list()
    for a in av:
        if (palabra in a.comentarios) and (a.fecha_hora.year==año):
            lista.append(a)
    return max(lista, key=lambda e:len(e.comentarios))

def comentario_mas_largo2(av:List[avistamiento],palabra:str,año:int)->avistamiento:
    return max(list(a for a in av if palabra in a.comentarios and a.fecha_hora.year==año),key=lambda e:len(e.comentarios))

def media_dias_entre_avistamientos(av:List[avistamiento],año:Optional[int]=None)->float:
    lista=list()
    dias=list()
    for a in av:
        if año==None or a.fecha_hora.year==año:
            lista.append(a)
    ordenada=sorted(lista, key=lambda e:e.fecha_hora)
    for d1,d2 in zip(ordenada[0:],ordenada[1:]):
        diferencia=(d2.fecha_hora.date()-d1.fecha_hora.date()).days
        dias.append(diferencia)
    return sum(dias)/len(dias)