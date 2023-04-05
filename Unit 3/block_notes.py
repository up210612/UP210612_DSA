def imprimir(x):
    if x>0:
        print(x)
        imprimir(x-1)

imprimir(5)

def jugar(intento=1): 
    respuesta = input("¿De qué color es una naranja? ") 
    if respuesta != "naranja": 
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo") 
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print ("\nPerdiste!" )
    else:
        print ("\nGanaste!" )

jugar()

