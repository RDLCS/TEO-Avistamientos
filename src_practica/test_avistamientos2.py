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

if __name__=='__main__':
    ovni=lee_avistamientos('data/ovnis.csv')
    #test_lee_avistamiento(ovni)
    #test_numero_avistamientos_fecha(ovni,datetime(2005,5,1).date())
    #test_formas_estado(ovni,{'nm','in','pa','wa'})
    #test_duracion_total(ovni,'in')
    #test_duracion_total(ovni,'nm')
    #test_duracion_total(ovni,'pa')
    #test_duracion_total(ovni,'wa')