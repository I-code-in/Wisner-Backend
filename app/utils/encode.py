import hashlib
from typing import Any, List


def generar_sha1(datos: List[Any]) -> str:
    
    datos_concatenados = "".join(map(str, datos))

    hash_sha1 = hashlib.sha1(datos_concatenados.encode()).hexdigest()

    return hash_sha1