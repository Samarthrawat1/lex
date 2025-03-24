from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    # Might not follow the roadmap :p
    return r"Life's a journey, Clark. I don't want to go through it following a roadmap. -Lex Luthor"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
