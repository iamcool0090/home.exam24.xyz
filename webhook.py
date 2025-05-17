from fastapi import FastAPI, Request, BackgroundTasks
import subprocess

app = FastAPI()

def run_command():
    # Replace with your desired shell command
    subprocess.run(["echo", "GitHub push event received!"], check=True)

@app.post("/webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    print("Received payload:", payload)
    return "ok"


if "__name__" == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

