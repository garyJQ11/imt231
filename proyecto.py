import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# Configuración del pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Función para detectar color amarillo
def detectar_color_amarillo(frame):
    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir el rango del color amarillo en HSV
    amarillo_bajo = np.array([20, 100, 100], np.uint8)
    amarillo_alto = np.array([30, 255, 255], np.uint8)
    #lower_green = np.array([25, 50, 50], np.uint8)
    #upper_green = np.array([75, 255, 255],np.uint8)
    
    # Crear una máscara con el rango del color amarillo
    mascara = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
    #mascara = cv2.inRange(hsv, lower_green, upper_green)
    
    # Filtrar la imagen para obtener solo las partes amarillas
    result = cv2.bitwise_and(frame, frame, mask=mascara)
    
    # Contar los píxeles amarillos en la imagen
    yellow_pixels = cv2.countNonZero(mascara)
    
    return yellow_pixels > 3000  # Umbral para considerar que el limón está presente

def detect_unripe_fruit(frame):
    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir los rangos de color para detectar frutas no maduras
    #lower_green = np.array([25, 50, 50], np.uint8)
    #upper_green = np.array([75, 255, 255],np.uint8)
    amarillo_bajo = np.array([20, 100, 100], np.uint8)
    amarillo_alto = np.array([30, 255, 255], np.uint8)
    
    # Crear una máscara para detectar los píxeles 
    mask = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
    
    
        
    return mask


# Inicialización de la cámara
cap = cv2.VideoCapture(0)  # Usar la cámara por defecto



while True:
    ret, frame = cap.read()
    mask = detect_unripe_fruit(frame)
    if not ret:
       print("Error al acceder a la cámara")
       break
        
        # Llamar a la función de detección de color
    if detectar_color_amarillo(frame):
       GPIO.output(23, GPIO.HIGH)  
       GPIO.output(24, GPIO.LOW)
       time.sleep(1)
            
    else:
       GPIO.output(23, GPIO.LOW)
       GPIO.output(24, GPIO.HIGH)
            
        
        # Mostrar la imagen en una ventana
        
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
        
        # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Limpiar los recursos
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()
