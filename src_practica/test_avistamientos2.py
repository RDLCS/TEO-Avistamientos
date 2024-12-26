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