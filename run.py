from fastapi import FastAPI
from nsfw_detector import predict
import os
import uvicorn
from random import randint
import aiohttp
import aiofiles


app = FastAPI()
model = predict.load_model('nsfw_detector2/nsfw_model.h5')
PORT = 8000

@app.get("/")
async def detect_nsfw(url: str):
    if not url:
        return {"ERROR": "URL PARAMETER EMPTY"}
    image = await download_image(url)
    if not image:
from fastapi import FastAPI
from nsfw_detector import predict
import os
import uvicorn
from random import randint
import aiohttp
import aiofiles


app = FastAPI()
model = predict.load_model('nsfw_detector/nsfw_model.h5')
PORT = 8000

@app.get("/")
async def detect_nsfw(url: str):
    if not url:
        return {"ERROR": "URL PARAMETER EMPTY"}
    image = await download_image(url)
    if not image:
        return {"ERROR": "IMAGE SIZE TOO LARGE OR INCORRECT URL"}
    results = predict.classify(model, image)
    os.remove(image)
    hentai = results['data']['hentai']
    sexy = results['data']['sexy']
    porn = results['data']['porn']
    drawings = results['data']['drawings']
    neutral = results['data']['neutral']
    if neutral >= 25:
        results['data']['is_nsfw'] = False
        return results
    elif (sexy + porn + hentai) >= 70:
        results['data']['is_nsfw'] = True
        return results
    elif drawings >= 40:
        results['data']['is_nsfw'] = False
        return results
    else:
        results['data']['is_nsfw'] = False
        return results

if __name__ == "__main__":
        uvicorn.run("run:app", host="0.0.0.0", port=PORT, log_level="info")

async def download_image(url):
    file_name = f"{randint(6969, 6999)}.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(file_name, mode='wb')
                await f.write(await resp.read())
                await f.close()
            else:
                return False
    return file_name
