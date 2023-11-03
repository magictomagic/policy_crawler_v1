import uvicorn
import yaml
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from interface.manually_trigger import router_checker

app = FastAPI()
app.include_router(router_checker)
my_host = "127.0.0.1"
my_port = 8000
with open("infrastructure/config/local_db_config.yaml", "r") as file:
    db_config = yaml.safe_load(file)
register_tortoise(app,
                  config=db_config,
                  add_exception_handlers=True,
                  generate_schemas=True)

if __name__ == "__main__":
    module_name = __name__.split(".")[0]
    with open('infrastructure/config/log_conf.yaml', 'r') as f:
        log_config = yaml.safe_load(f)
    uvicorn.run(f"{module_name}:app",
                host=my_host, port=my_port,
                reload=True,
                log_config=log_config)
