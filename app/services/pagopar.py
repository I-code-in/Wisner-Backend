import json
from decouple import config as env
from requests import post  # type: ignore
from datetime import datetime
from fastapi import HTTPException
from app.schemas.orders import OrderIn
from app.schemas.pagopar import Transaccion, Comprador, ComprasItem
from utils.encode import generar_sha1


def iniciar_transaccion(order: OrderIn):
    ext_conv_url = str(env("PAGOPAR_SERVICE", ""))

    url = f"{ext_conv_url}/comercios/2.0/iniciar-transaccion"

    headers = {
        "Content-Type": "application/json",
    }

    token_privado = str(env("PAGOPAR_TOKEN_PRIVADO", ""))

    public_key = str(env("PAGOPAR_PUBLIC_KEY", ""))

    id_pedido = ""

    monto_total = 0

    token = generar_sha1([token_privado, id_pedido, monto_total])
    
    transaccion = Transaccion(
        token=token,
        comprador=generar_comprador(order),
        public_key=public_key,
        monto_total=monto_total,
        tipo_pedido="VENTA-COMERCIO",
        compras_items=generar_compras_items(order),
        fecha_maxima_pago=generar_fecha_maxima_pago(order),
        id_pedido_comercio=get_id_pedido_comercio(order),
        descripcion_resumen=generar_descripcion_resumen(order),
        forma_pago=9
    )

    data = json.load(transaccion)

    response = post(url, headers=headers, json=data)

    if response and response.status_code == 200:
        return response.json()
    
    else:
        print("Error en servicio externo: ", response.status_code, response.json())
        raise HTTPException(
            status_code=403,
            detail="Ha ocurrido un error al obtener la respuesta",
        )


def generar_comprador(order: OrderIn) -> Comprador:
    pass


def generar_compras_items(order: OrderIn) -> list[ComprasItem]:
    pass


def generar_fecha_maxima_pago(order: OrderIn) -> datetime:
    pass


def get_id_pedido_comercio(order: OrderIn) -> str:
    pass


def generar_descripcion_resumen(order: OrderIn) -> str:
    pass