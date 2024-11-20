import asyncio
from pythonping import ping

async def pingserver():
	print("pingserver Started...")
  #put 5s sleep so that other function executes within this time interval , adjust accordingly
  #if other function takes time then increase it.
	await asyncio.sleep(5)
  # ping the server, it might take time so switch to another function to do rest of job
	ping('172.10.2.1', count=1,timeout=10, verbose=True)
	print("pingserver Ended...")


async def connecttoserver():
	print("connecttoserver started..")
	await asyncio.sleep(3)
	print("connecttoserver Ended")


async def serveroperations():
	print("serveroperations started..")
	await asyncio.sleep(1)
	print("serveroperations Ended")


async def main():
	L = await asyncio.gather(
		pingserver(),
		connecttoserver(),
		serveroperations(),
	)
	print("Main Ended..")


asyncio.run(main())

