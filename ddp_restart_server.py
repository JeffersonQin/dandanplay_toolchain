import uvicorn
import os
from fastapi import FastAPI

run_host = "0.0.0.0"
run_port = 4832
api_token = "your-token"

app = FastAPI()

@app.get('/' + api_token)
def restart():
	os.system("cmd.exe /c ddp_restart.bat")
	return "succeeded"

if __name__ == "__main__":
	uvicorn.run(app, host=run_host, port=run_port, debug=False)