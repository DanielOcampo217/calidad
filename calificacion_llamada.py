#------------ Apertura y cierre
nombre = ['mi nombre', 'me llamo', 'me presentos']
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
            
#---------------- Buscar coincidencias en validación------------------------
for palabra in confirmar:
    if palabra in texto:
        puntuacion_total += 20
        break
    
#---------------- Buscar coincidencias en Ofrecimiento----------------------
for palabra in ofrecimiento:
    if palabra in texto:
        puntuacion_total += 15
        break

#---------------- Buscar coincidencias en ID--------------------------------
for palabra in id:
    if palabra in texto:
        puntuacion_total += 15
        break

#---------------- Buscar coincidencias Registro-----------------------------
for palabra in registro:
    if palabra in texto:
        puntuacion_total += 5
        break
    
#---------------- Buscar coincidencias aviso-----------------------------
for palabra in aviso:
    if palabra in texto:
        puntuacion_total += 10
        break



if puntuacion_total > 0:
    print("El agente obtuvo una calificacion en calidad de: ", puntuacion_total)
else:
    print("No se encontraron palabras clave de apertur y cierre.")