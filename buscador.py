# buscador.py
import time
from pokemontcgsdk import Card

def tokenizar_entrada(entrada: str):
    palabras = entrada.lower().split()
    name = ""
    subtype = ""
    sets = ""

    posibles_subtipos = [
        "ex", "gx", "v", "vmax", "vstar", "mega", "baby", "prime", "legend"
    ]

    for palabra in palabras:
        if palabra in posibles_subtipos:
            subtype = palabra
        else:
            name += palabra + " "

    return name.strip(), subtype, sets


def buscar_y_procesar(entrada: str):
    """Realiza la búsqueda en la API de Pokémon TCG."""
    name, subtype, sets = tokenizar_entrada(entrada)

    query = f"name:{name}"
    if subtype:
        query += f" subtypes:{subtype}"
    if sets:
        query += f" set.name:{sets}"

    start = time.time()
    cards = Card.where(q=query, orderBy='set.releaseDate', page=1, pageSize=10)
    end = time.time()

    resultados = []
    for card in cards:
        try:
            market_price = card.tcgplayer.prices.holofoil.market
            market_price_str = f"${market_price:.2f}"
        except Exception:
            market_price_str = "N/A"

        resultados.append(
            f"{card.name} ({card.set.name})\nID: {card.id}\n💰 Precio: {market_price_str}"
        )

    if not resultados:
        return f"❌ No encontré resultados para '{entrada}'."

    tiempo = f"⏱ {end - start:.2f} s"
    return f"🔍 Resultados para '{entrada}':\n\n" + "\n\n".join(resultados) + f"\n\n{tiempo}"

