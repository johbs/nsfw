from fastapi import FastAPI
from nsfw_detector import predict
import os
import uvicorn
from random import randint
from urllib.error import HTTPError
from urllib.request import urlretrieve

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
    try:
        urlretrieve(url, file_name)
    except FileNotFoundError as err:
        print(err)   # something wrong with local path
        return False
    except HTTPError as err:
        print(err)  # something wrong with url
        return False

    return file_name
