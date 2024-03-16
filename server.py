from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve files from the "assets" folder
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def main():
    return FileResponse('index.html')
