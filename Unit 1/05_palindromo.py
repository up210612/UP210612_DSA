palabra = input("Ingrese oración ")
palabra = palabra.upper() 
palabraN = ""
for letra in palabra:                            
    if letra not in (" "):    
        palabraN += letra   

if(palabraN==palabraN[::-1]):  
      print("Es un palindromo")  
else:  
      print("No es un palindromo") 