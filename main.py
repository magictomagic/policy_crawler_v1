import json
from logging.handlers import RotatingFileHandler
from fastapi.responses import Response

import uvicorn
import yaml
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from application.check import test111, test_on_get, show_atom3

my_host = "127.0.0.1"
my_port = 8000

app = FastAPI()
db_config = None
with open("infrastructure/config/local_db_config.yaml", "r") as file:
    db_config = yaml.safe_load(file)
register_tortoise(app,
                  config=db_config,
                  add_exception_handlers=True,
                  generate_schemas=True)
log_config = None
with open('infrastructure/config/log_conf.yaml', 'r') as f:
    log_config = yaml.safe_load(f)


@app.get("/fetchfzggw")
async def get_fzggw_info():
    await test111()
    return {"msg": "ok"}


@app.get("/fetchtest")
async def get_fzggw_info():
    await test_on_get()
    return {"msg": "ok"}


@app.get("/feed")
async def root():
    atom_string = await show_atom3()
    return Response(content=atom_string, media_type="application/atom+xml; charset=utf-8")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    module_name = __name__.split(".")[0]
    app_name = "app"

    uvicorn.run(f"{module_name}:{app_name}", host=my_host, port=my_port, reload=True, log_config=log_config)
