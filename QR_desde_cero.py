# Para crear codigos QR en python necesitamos una libreria qrcode :https://github.com/lincolnloop/python-qrcode 
# y pillow para trabajar con las imagenes :https://pillow.readthedocs.io/en/stable/handbook/overview.html

# Instalacion de paquetes(si no los tenemos)

# En el terminal usamos el comando :  "pip install qrcode" 
# Tambien en el terminal con el comando: "pip install pillow"


#importamos la libreria qr code
import qrcode

#vamos a crear una variable que contrenda en nuestro caso la url de github 
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

#vamos a crear el QR para ello debemos definir algunos parametros 
# version es el tamaño 
# box_size es la cantidad de pixeles que hay relacionados al QR
# border la relacion del borde con nuestro QR

qr = qrcode.QRCode(version=1,box_size=10,border=5)

# Agregamos al informacion (en vez de link podriamos agregar directamente el link

qr.add_data(link)

#creamos el QR  en el parametro fill podemos elegir el tipo de los pixeles

qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")

# y lo guardamos elegimos el nombre 
img.save("rickrool.png")
