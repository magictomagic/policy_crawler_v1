from fastapi import APIRouter
from fastapi.responses import Response

from application.check import test111, test_on_get, show_atom3

router_checker = APIRouter()


@router_checker.get("/fetchfzggw")
async def get_fzggw_info():
    await test111()
    return {"msg": "ok"}


@router_checker.get("/fetchtest")
async def get_fzggw_info():
    await test_on_get()
    return {"msg": "ok"}


@router_checker.get("/feed")
async def root():
    atom_string = await show_atom3()
    return Response(content=atom_string, media_type="application/atom+xml; charset=utf-8")


@router_checker.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
