import csv
from typing import NamedTuple,List,Dict,DefaultDict,Tuple,Optional
from datetime import datetime
from math import radians, sin, cos, asin, sqrt
from collections import namedtuple, Counter, defaultdict
import locale
import statistics

coordenadas=NamedTuple('coordenadas',[('latitud',float),('longitud',float)])

avistamiento=NamedTuple('avistamiento',[('fecha_hora',datetime),('ciudad',str),('estado',str),('forma',str),('duracion',int)
                                        ,('comentarios',str),('ubicación',coordenadas)])

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