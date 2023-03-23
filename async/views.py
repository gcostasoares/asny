import asyncio

async def contador():
    await asyncio.sleep(1)
    print('A contagem comecou')
    for num in range(1,15):
        await asyncio.sleep(1)
        tempo = num
        print(num)

async def http_call_async():
    asyncio.ensure_future(contador()) 
    await asyncio.sleep(1)
    print("olá Ebac!. A primeira funcao deu início")
    await asyncio.sleep(9)
    print("A primeira funcao está pronta")



loop = asyncio.get_event_loop()
loop.run_until_complete(http_call_async())


