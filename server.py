from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve files from the "assets" folder
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/video", StaticFiles(directory="./video"), name="video")


@app.get("/")
async def main():
    return FileResponse('index.html')

@app.get("/open")
async def main():
    return 'open response'

@app.get("/close")
async def main():
    return 'close response'
