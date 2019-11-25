#https://github.com/britisharmy/aiofile
import asyncio
from aiofile import AIOFile, LineReader, Writer
async def main():

    async with AIOFile("file.csv", 'r') as afp:
        async for line in LineReader(afp):
            #print(line[:10])
            array = line.split(',')
            first_item = array[0]
            print(first_item)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
