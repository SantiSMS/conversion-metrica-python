conversion_cm_a_pulgadas = 2.54 

# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms

medida_mueble_cms = float(input("Ingresar medida del mueble en cm: "))

# Paso 2: Convertir las medidas de centímetros a pulgadas

medida_mueble_pulgadas = medida_mueble_cms / conversion_cm_a_pulgadas

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario 

print("La medida de ", medida_mueble_cms, "en pulgadas es: ", medida_mueble_pulgadas)


