from fastapi import FastAPI, Request, BackgroundTasks
import subprocess
import os
import shutil

app = FastAPI()

def deploy_repo(clone_url):
    repo_dir = "/tmp/socialconnect"
    # Remove old repo if exists
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)
    # Clone the repo
    subprocess.run(["git", "clone", clone_url, repo_dir], check=True)
    # Build Docker image
    subprocess.run(["docker", "build", "-t", "socialconnect", "."], cwd=repo_dir, check=True)
    # Remove all running containers
    subprocess.run("docker rm -f $(docker ps -qa) || true", shell=True)
    # Run the new container
    subprocess.run(["docker", "run", "-d", "-p", "8001:8001", "socialconnect"], check=True)

@app.post("/webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    print("Received payload:", payload)
    # Get the clone_url from the payload
    clone_url = payload.get("repository", {}).get("clone_url")
    if clone_url:
        background_tasks.add_task(deploy_repo, clone_url)
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)