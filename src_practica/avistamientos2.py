import csv
from typing import NamedTuple,List,Dict,DefaultDict,Tuple,Optional,Set
from datetime import datetime,date,time,timedelta
from math import radians, sin, cos, asin, sqrt, pi
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

def avistamiento_por_fecha(av:List[avistamiento])->Dict[date,avistamiento]:
    dicc=dict()
    for a in av:
        if a.fecha_hora.date() not in dicc:
            dicc[a.fecha_hora.date()]=list()
        dicc[a.fecha_hora.date()].append(a)
    return dicc

def avistamiento_por_fecha2(av:List[avistamiento])->Dict[date,List[avistamiento]]:
    dicc=DefaultDict(list)
    for a in av:
        dicc[a.fecha_hora.date()].append(a)
    return dicc

def formas_por_mes(av:List[avistamiento])->Dict[str,set]:
    dicc=dict()
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    for a in av:
        mes=meses[a.fecha_hora.month-1]
        if mes not in dicc:
            dicc[mes]=set()
        dicc[mes].add(a.forma)
    return dicc

def formas_por_mes2(av:List[avistamiento])->Dict[str,set]:
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    dicc=DefaultDict(set)
    for a in av:
        mes=meses[a.fecha_hora.month-1]
        dicc[mes].add(a.forma)
    return dicc

def numeros_avistamientos_por_año(av:List[avistamiento])->Dict[int,int]:
    dicc=dict()
    for a in av:
        if a.fecha_hora.year not in dicc:
            dicc[a.fecha_hora.year]=0
        dicc[a.fecha_hora.year]+=1
    return dicc

def numeros_avistamientos_por_año2(av:List[avistamiento])->Dict[int,int]:
    return Counter(list(a.fecha_hora.year for a in av))

def numeros_avistamientos_por_año3(av:List[avistamiento])->Dict[int,int]:
    dicc=DefaultDict(int)
    for a in av:
        dicc[a.fecha_hora.year]+=1
    return dicc

def num_avistamientos_por_mes(av:List[avistamiento])->Dict[str,int]:
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    dicc=dict()
    for a in av:
        mes=meses[a.fecha_hora.month-1]
        if mes not in dicc:
            dicc[mes]=0
        dicc[mes]+=1
    return dicc

def num_avistamientos_por_mes2(av:List[avistamiento])->Dict[str,int]:
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    return Counter(list(meses[a.fecha_hora.month-1] for a in av))

def num_avistamientos_por_mes3(av:List[avistamiento])->Dict[str,int]:
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    dicc=DefaultDict(int)
    for a in av:
        mes=meses[a.fecha_hora.month-1]
        dicc[mes]+=1
    return dicc

def redondeo_coordenadas(coord:coordenadas)->coordenadas:
    r_latitud=round(coord[0])
    r_longitud=round(coord[1])
    return coordenadas(r_latitud,r_longitud)

def coordenadas_mas_avistamientos(av:List[avistamiento])->coordenadas:
    dicc=dict()
    for a in av:
        coord=redondeo_coordenadas(a.ubicacion)
        if coord not in dicc:
            dicc[coord]=0
        dicc[coord]+=1
    return max(dicc.keys(), key=dicc.get)

def coordenadas_mas_avistamientos2(av:List[avistamiento])->coordenadas:
    contador=Counter(redondeo_coordenadas(a.ubicacion) for a in av)
    return max(contador,key=contador.get)

def coordenadas_mas_avistamientos3(av:List[avistamiento])->coordenadas:
    dicc=DefaultDict(int)
    for a in av:
        coord=redondeo_coordenadas(a.ubicacion)
        dicc[coord]+=1
    return max(dicc,key=dicc.get)

def hora_mas_avistamientos(av:List[avistamiento])->int:
    dicc=dict()
    for a in av:
        if a.fecha_hora.hour not in dicc:
            dicc[a.fecha_hora.hour]=0
        dicc[a.fecha_hora.hour]+=1
    return max(dicc,key=dicc.get)

def hora_mas_avistamientos2(av:List[avistamiento])->int:
    contador=Counter(a.fecha_hora.hour for a in av)
    return max(contador,key=contador.get)

def longitud_media_comentarios(av:List[avistamiento])->float:
    lista=list(len(a.comentarios) for a in av)
    return sum(lista)/len(lista)

def longitud_media_comentarios_por_estado(av:List[avistamiento])->Dict[str,float]:
    dicc=DefaultDict(list)
    for a in av:
        dicc[a.estado].append(a)
    for c,v in dicc.items():
        dicc[c]=longitud_media_comentarios(v)
    return dicc

def porc_avistamientos_por_forma(av:List[avistamiento])->Dict[str,float]:
    total=len(av)
    dicc=dict()
    for a in av:
        if a.forma not in dicc:
            dicc[a.forma]=0
        dicc[a.forma]+=1
    for c,v in dicc.items():
        dicc[c]=(v/total)*100
    return dicc

def porc_avistamientos_por_forma2(av:List[avistamiento])->Dict[str,float]:
    contador=Counter(a.forma for a in av)
    total=len(av)
    for c,v in contador.items():
        contador[c]=(v/total)*100
    return contador

def avistamientos_mayor_duracion_por_estado(av:List[avistamiento],n:Optional[int]=3)->Dict[str,List[avistamiento]]:
    dicc=DefaultDict(list)
    for a in av:
        dicc[a.estado].append(a)
    for c,v in dicc.items():
        dicc[c]=sorted(v,key=lambda e:e.duracion,reverse=True)[:n]
    return dicc

def año_mas_avistamientos_forma(av:List[avistamiento])->Dict[str,int]:
    dicc=dict()
    for a in av:
        if a.forma not in dicc:
            dicc[a.forma]=list()
        dicc[a.forma].append(a.fecha_hora.year)
    for c,v in dicc.items():
        dicc[c]=max(contador_años(v),key=lambda e:e[1])[0]
    return dicc

def contador_años(años:List[int])->List[Tuple[int,int]]:
    dicc=dict()
    for a in años:
        if a not in dicc:
            dicc[a]=0
        dicc[a]+=1
    return dicc.items()

def año_mas_avistamientos_forma2(av:List[avistamiento])->Dict[str,int]:
    contador=DefaultDict(list)
    for a in av:
        contador[a.forma].append(a)
    for c,v in contador.items():
        nuevo_cont=Counter(j.fecha_hora.year for j in v)
        contador[c]=max(nuevo_cont,key=nuevo_cont.get)
    return contador

def estados_mas_avistamientos(av:List[avistamiento],n:Optional[int]=5)->List[Tuple[str,int]]:
    dicc=Counter(a.estado for a in av)
    return sorted(dicc.items(),key=lambda e:e[1],reverse=True)[:n]

def duracion_total_avistamientos_año(av:List[avistamiento],estado:str)->Dict[int,float]:
    dicc=dict()
    for a in av:
        if a.estado==estado:
            if a.fecha_hora.year not in dicc:
                dicc[a.fecha_hora.year]=0
            dicc[a.fecha_hora.year]+=a.duracion/3600
    return dicc

def duracion_total_avistamientos_año2(av:List[avistamiento],estado:str)->Dict[int,float]:
    dicc=DefaultDict(int)
    for a in av:
        if a.estado==estado:
            dicc[a.fecha_hora.year]+=a.duracion/3600
    return dicc

def avistamiento_mas_reciente_por_estado(av:List[avistamiento])->Dict[str,datetime]:
    dicc=DefaultDict(list)
    for a in av:
        dicc[a.estado].append(a.fecha_hora)
    for c,v in dicc.items():
        dicc[c]=max(v)
    return dicc