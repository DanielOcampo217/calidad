#------------ Apertura y cierre
nombre = ['mi nombre', 'me llamo', 'me presento']
donde_llama = ["izzi"]
para_que_llama = ['renovar', 'plazo', 'doce meses', 'un año mas']
beneficio = ['agradecimiento', 'permanencia', 'continua', 'seguir con nosotros']

#------------ Validación
confirmar = ["titular", 'contacto', 'parentesco']

#------------ Ofrecimiento
ofrecimiento = ['paquete', 'se le mantiene', 'seguira pagando', 'congela', 'permanece igual']

#------------ ID
id = ['ine', 'elector', 'pasaporte', 'cedula', 'cartilla', 'licencia', 'ims', 'iste', 'semin', 'inamap']

#------------ Registro 
registro = ['folio', 'orden']

#------------ Aviso de privacidad
aviso = ['grabada', 'monitoreada', 'fines', 'calidad', 'protegidos', 'izipuntocom']

texto = input("Ingresa el texto a validar: ")
puntuacion_total = 0

#----------------Apertura y cierre------------------------------------
# Buscar coincidencias en la lista de nombres
for palabra in nombre:
    if palabra in texto:
        puntuacion_total += 8.75
        break

# Buscar coincidencias en la lista de lugares de llamada
for palabra in donde_llama:
    if palabra in texto:
        puntuacion_total += 8.75
        break

# Buscar coincidencias en la lista de razones de llamada
for palabra in para_que_llama:
    if palabra in texto:
        puntuacion_total += 8.75
        break

# Buscar coincidencias en la lista de beneficios
for palabra in beneficio:
    if palabra in texto:
        puntuacion_total += 8.75
        break
        
suma1 = puntuacion_total
#---------------- Buscar coincidencias en validación------------------------
for palabra in confirmar:
    if palabra in texto:
        puntuacion_total += 20
        break

suma2 = puntuacion_total - suma1
#---------------- Buscar coincidencias en Ofrecimiento----------------------
for palabra in ofrecimiento:
    if palabra in texto:
        puntuacion_total += 15
        break

suma3 = puntuacion_total - suma1 - suma2
#---------------- Buscar coincidencias en ID--------------------------------
for palabra in id:
    if palabra in texto:
        puntuacion_total += 15
        break

suma4 = puntuacion_total - suma1 - suma2 - suma3
#---------------- Buscar coincidencias Registro-----------------------------
for palabra in registro:
    if palabra in texto:
        puntuacion_total += 5
        break
    
suma5 = puntuacion_total - suma1 - suma2 - suma3 - suma4
#---------------- Buscar coincidencias aviso-----------------------------
for palabra in aviso:
    if palabra in texto:
        puntuacion_total += 10
        break

suma6 = puntuacion_total - suma1 - suma2 - suma3 - suma4 - suma5


if puntuacion_total > 0:
    print("En APERTURA Y CIERRE obtuvo una puntuación de: ", suma1)
    print("En VALIDACÓN obtuvo una puntuación de: ", suma2)
    print("En OFRECIMIENTO obtuvo una puntuación de: ", suma3)
    print("En ID obtuvo una calificación de: ", suma4)
    print("En REGISTRO obtuvo una puntuación de: ", suma5)
    print("En AVISO obtuvo una puntuación de: ", suma6)
    print("El agente obtuvo una calificacion en calidad de: ", puntuacion_total)
else:
    print("No se encontraron palabras clave de apertur y cierre.")