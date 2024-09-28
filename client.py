import socketio

#Crear una instancia del Cliente
sio = socketio.Client()

#Conectarse al servidor 
@sio.event
def connect():
    print('Conectado al servidor')
    
#recibir mensajes del servidor 
@sio.event('message')
def on_messager(data):
    print(f"Mensaje recibido")

#Desconectarse del servidor 
@sio.event
def disconnect():
    print('Desconectado del servidor')

#Conectarse al servidor 
sio.connect('http://127.0.0.1:8000')

#enviar un mensaje 
sio.emit('message','Hola desde el Cliente')

#mantener la conexion abierta 
sio.wait()
