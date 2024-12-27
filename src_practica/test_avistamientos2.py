from avistamientos2 import*

def test_lee_avistamiento(av:List[avistamiento])->None:
    print(av[:3])

def test_numero_avistamientos_fecha(av:List[avistamiento],fecha:datetime)->None:
    lista=numero_avistamientos_fecha(av,fecha)
    fecha_texto=datetime.strftime(fecha,'%d/%m/%Y')
    print(f"El día {fecha_texto} se produjeron {len(lista)} avistamientos.")

def test_formas_estado(av:List[avistamiento],estados:set)->None:
    numero=formas_estados(av,estados)
    texto=', '.join(estados)
    print(f"Número de formas distintas observadas en los estados {texto}: {numero}")

def test_duracion_total(av:List[avistamiento],estado:str)->None:
    duracion=duracion_total(av,estado)
    print(f"Duración total de los avistamientos en {estado}: {duracion} segundos.")

def test_avistamientos_cercanos_ubicacion(av:List[avistamiento],ubicacion:coordenadas)->None:
    radio=0.5
    conjunto=avistamientos_cercanos_ubicacion(av,ubicacion,radio)
    print(f"Avistamientos cercanos a {ubicacion}:")
    for num,conj in enumerate(conjunto):
        print(f"{num+1}. {conj}")

def test_avistamiento_mayor_duracion(av:List[avistamiento],forma:str)->None:
    final=avistamiento_mayor_duracion2(av,forma)
    print(f"Avistamiento de forma {forma} de mayor duracion: {final}")

def test_avistamiento_cercano_mayor_duracion(av:List[avistamiento],ubicacion:coordenadas)->None:
    radio=0.5
    final=avistamiento_cercano_mayor_duracion2(av,radio,ubicacion)
    print(f"Duración del avistamiento más largo en un entorno de radio {radio} sobre las coordenadas {ubicacion}: {final[0]}")
    print(f"Comentario: {final[1]}")

def test_avistamiento_fechas(av:List[avistamiento],fecha1:date,fecha2:date)->None:
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    dia1=fecha1.day
    dia2=fecha2.day
    mes1=meses[fecha1.month-1]
    mes2=meses[fecha2.month-1]
    año1=fecha1.year
    año2=fecha2.year
    print(f"Mostrando los avistamientos desde el {dia1} de {mes1} del {año1} hasta el {dia2} de {mes2} del {año2}:")
    for p in avistamiento_fechas(av,fecha1,fecha2):
        print(p)
    print(f"Total: {len(avistamiento_fechas(av,fecha1,fecha2))} avistamientos.")
    print(f"Avistmaientos hasta el {dia1} de {mes1} del {año1}: {len(avistamiento_fechas(av,fecha2=fecha1))}")
    print(f"Avistamientos desde el {dia2} de {mes2} del {año2}: {len(avistamiento_fechas(av,fecha2))}")

def test_comentario_mas_largo(av:List[avistamiento],palabra:str,año:int)->None:
    print(f"El avistamiento con el comentario más largo del {año} incluyendo la palabra \"{palabra}\" es:")
    print(comentario_mas_largo2(av,palabra,año))

def test_media_dias_entre_avistamientos(av:List[avistamiento],año:int)->None:
    print(f"La media de dias entre dos avistamientos consecutivos es: {media_dias_entre_avistamientos(av)}")
    print(f"La media de dias entre dos avistamientos consecutivos del año {año} es: {media_dias_entre_avistamientos(av,año)}")

def test_avistamiento_por_fecha(av:List[avistamiento],fecha1:date,fecha2:date)->None:
    dicc=avistamiento_por_fecha2(av)
    fecha1_str=datetime.strftime(fecha1, '%Y-%m-%d')
    fecha2_str=datetime.strftime(fecha2, '%Y-%m-%d')
    print("Avistamientos por fecha:")
    print(f"{fecha1_str}: {dicc[fecha1]}")
    print(f"{fecha2_str}: {dicc[fecha2]}")

def test_formas_por_mes(av:List[avistamiento],mes1:str,mes2:str,mes3:str)->None:
    dicc=formas_por_mes2(av)
    print("Formas por mes:")
    print(f"{mes1} ({len(dicc[mes1])} formas distintas): {dicc[mes1]}")
    print(f"{mes2} ({len(dicc[mes2])} formas distintas): {dicc[mes2]}")
    print(f"{mes3} ({len(dicc[mes3])} formas distintas): {dicc[mes3]}")

def test_numero_avistamientos_por_año(av:List[avistamiento])->None:
    dicc=numeros_avistamientos_por_año2(av)
    print("Numero de avistamientos por año:")
    for c,v in dicc.items():
        print(f"{c}: {v}")

def test_num_avistamientos_por_mes(av:List[avistamiento],mes1:str,mes2:str,mes3:str)->None:
    dicc=num_avistamientos_por_mes2(av)
    print("Número de avistamientos por mes:")
    print(f"{mes1}: {dicc[mes1]}")
    print(f"{mes2}: {dicc[mes2]}")
    print(f"{mes3}: {dicc[mes3]}")

def test_coordenadas_mas_avistamientos(av:List[avistamiento])->None:
    coord=coordenadas_mas_avistamientos2(av)
    print(f"Coordenadas enteras de la región en la que se observaron más avistamientos: {coord}")

def test_hora_mas_avistamientos(av:List[avistamiento])->None:
    hora=hora_mas_avistamientos2(av)
    print(f"Hora en la que se han observado más avistamientos: {hora}")

def test_longitud_media_comentarios_por_estado(av:List[avistamiento],estado1:str,estado2:str,estado3:str,estado4:str)->None:
    dicc=longitud_media_comentarios_por_estado(av)
    print(f"Mostrando la media del tamaño de los comentarios de los avistamientos de los estados {estado1}, {estado2}, {estado3}, {estado4}")
    print(f"{estado1}: {dicc[estado1]}")
    print(f"{estado2}: {dicc[estado2]}")
    print(f"{estado3}: {dicc[estado3]}")
    print(f"{estado4}: {dicc[estado4]}")

def test_porc_avistamientos_por_forma(av:List[avistamiento],f1:str,f2:str,f3:str,f4:str)->None:
    dicc=porc_avistamientos_por_forma2(av)
    print(f"Porcentajes de avistamientos de las formas {f1}, {f2}, {f3} y {f4}:")
    print(f"{f1}: {dicc[f1]:.2f}%")
    print(f"{f2}: {dicc[f2]:.2f}%")
    print(f"{f3}: {dicc[f3]:.2f}%")
    print(f"{f4}: {dicc[f4]:.2f}%")

def test_avistamiento_mayor_duracion_por_estado(av:List[avistamiento],est1:str,est2:str,n:Optional[int]=3)->None:
    dicc=avistamientos_mayor_duracion_por_estado(av,n)
    print(f"Mostrando los {n} avistamientos de mayor duración de los estados {est1} y {est2} ")
    print(f"\t{est1}")
    for p in dicc[est1]:
        print(f"\t\t{p}")
    print(f"\t{est2}")
    for j in dicc[est2]:
        print(f"\t\t{j}")

def test_año_mas_avistamientos_forma(av:List[avistamiento],forma:str)->None:
    dicc=año_mas_avistamientos_forma2(av)
    print(f"Año con más avistamientos de tipo {forma}: {dicc[forma]}")

def test_estados_mas_avistamientos(av:List[avistamiento],n:Optional[int]=5)->None:
    estados=estados_mas_avistamientos(av,n)
    print(f"Estados con más avistamientos, de mayor a menor nº de avistamientos: {estados}")

def test_duracion_total_avistamientos_año(av:List[avistamiento],estado:str)->None:
    dicc=duracion_total_avistamientos_año2(av,estado)
    print(f"Mostrando la duración total de los avistamientos entre 2000 y 2002 en el estado {estado}:")
    print(f"Año 2000: {dicc[2000]} horas")
    print(f"Año 2001: {dicc[2001]} horas")
    print(f"Año 2002: {dicc[2002]} horas")

def test_avistamiento_mas_reciente_por_estado(av:List[avistamiento],e1:str,e2:str)->None:
    dicc=avistamiento_mas_reciente_por_estado(av)
    print(f"Fecha del último avistamiento en {e1}: {dicc[e1]}")
    print(f"Fecha del último avistamiento en {e2}: {dicc[e2]}")

if __name__=='__main__':
    ovni=lee_avistamientos('data/ovnis.csv')
    #test_lee_avistamiento(ovni)
    #test_numero_avistamientos_fecha(ovni,date(2005,5,1))
    #test_formas_estado(ovni,{'nm','in','pa','wa'})
    #test_duracion_total(ovni,'in')
    #test_duracion_total(ovni,'nm')
    #test_duracion_total(ovni,'pa')
    #test_duracion_total(ovni,'wa')
    #test_avistamientos_cercanos_ubicacion(ovni,coordenadas(40.1933333, -85.3863889))
    #test_avistamiento_mayor_duracion(ovni,'circle')
    #test_avistamiento_cercano_mayor_duracion(ovni,coordenadas(40.1933333, -85.3863889))
    #test_avistamiento_fechas(ovni,date(2005,5,1),date(2005,5,1))
    #test_comentario_mas_largo(ovni,'ufo',2005)
    #test_media_dias_entre_avistamientos(ovni,1979)
    #test_avistamiento_por_fecha(ovni,date(1986,9,18),date(1986,7,20))
    #test_formas_por_mes(ovni,'Enero','Julio','Noviembre')
    #test_numero_avistamientos_por_año(ovni)
    #test_num_avistamientos_por_mes(ovni,'Enero','Febrero','Marzo')
    #test_coordenadas_mas_avistamientos(ovni)
    #test_hora_mas_avistamientos(ovni)
    #test_longitud_media_comentarios_por_estado(ovni,'in','nm', 'pa', 'wa')
    #test_porc_avistamientos_por_forma(ovni,'changing', 'chevron', 'cigar', 'circle')
    #test_avistamiento_mayor_duracion_por_estado(ovni,'in','nm')
    #test_año_mas_avistamientos_forma(ovni,'circle')
    #test_estados_mas_avistamientos(ovni)
    #test_duracion_total_avistamientos_año(ovni,'ca')
    test_avistamiento_mas_reciente_por_estado(ovni,'in','nm')