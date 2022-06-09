import websockets
import asyncio


PORT = 7890
HOST = 'localhost'
print(f"Server listening on port {PORT} ...")

connected = set()

async def echo(websocket, path):
    print('A client just connected...')
    connected.add(websocket)
    
    try:
        async for message in websocket:
            print("Recieved message from client: " + message)
            for conn in connected:
                if conn != websocket:
                    await conn.send(f"Someone said: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print("A clien just disconnected!")
    finally:
        connected.remove(websocket)
        
start_server = websockets.serve(echo, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()