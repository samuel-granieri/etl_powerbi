from fastapi import APIRouter
from app.services.get_saldos import get_all_saldos
from app.services.get_pedidos_ordem_compra import get_all_pedidos_ordem_compra

router = APIRouter()

@router.get("/saldos")
def saldos():
    return get_all_saldos()

@router.get("/pedidos-ordem-compra")
def pedidos_ordem_compra():
    return get_all_pedidos_ordem_compra()