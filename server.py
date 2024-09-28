from fastapi import FastAPI 
import uvicorn 
import socketio

#Crea una aplicación en FastAPI
app = FastAPI()

#Crear una instancia del servidor de SocketIO
sio = socketio.AsyncServer(async_mode='asgi')

# Combinar FastAPI y SocketAPI en la misma aplicacion 
app.mount("/ws", socketio.ASGIApp(sio,app))

#Definir una ruta basica en FastAPI 
@app.get("/")
async def read_root():
    return{"messager": "Servidor de chat tiempo real"}

#Cliente se conecta
@sio.event
async def connect(sid, environ):
    print(f'Cliente conectado: {sid}')
    await sio.emit("message", "Bienvenido al servidor", room=sid)
    
#Resivir o enviar los mensajes 
@sio.event
async def message(sid,data):
    print(f'Mensaje recibido de {sid}: {data}')
    await sio.emit('message', data) #Enviar el mensaje a todos los clientes conectados 
    
#Desconexiones
@sio.event
async def disconnect(sid):
    print(f'Cliente desconectado: {sid}')
 
 #ejecutar el servidor    
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)