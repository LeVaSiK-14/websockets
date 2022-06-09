import websockets
import asyncio
import ssl
import certifi


ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())


async def listen():
    url = 'wss://127.0.0.1:7890'
    
    async with websockets.connect(url, ssl=ssl_context) as ws:
        
        await ws.send("Hello server")
        
        while True:
            msg = await ws.recv()
            print(msg)
            
asyncio.run(listen())