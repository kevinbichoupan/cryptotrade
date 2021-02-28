import websockets
import asyncio
import json
import time

async def coinbaseWebsocket():
	uri = "wss://ws-feed.pro.coinbase.com"	





	subscribeMessage = {
		"type" : "subscribe"
		,"product_ids" : ['BTC-USD']
		,"channels" : ["heartbeat", "ticker"]
	}
	subscribeJSON = json.dumps(subscribeMessage)


	async with websockets.connect(uri) as websocket:
		await websocket.send(subscribeJSON)
		print("Subscribe message sent")

		response = await websocket.recv()
		print(response)
		
		time.sleep(10)	
		response = await websocket.recv()
		print(response)

		time.sleep(10)	
		response = await websocket.recv()
		print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(coinbaseWebsocket())
loop.close()












"""
async def coinbaseWebsocket(websocket, path):
	name = await websocket.recv()
	print(f"< {name}")

	greeting = f"Hello {name}!"

	await websocket.send(greeting)
	print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

"""
