import requests
import json #JavaScript Object Notation (JSON) is a -standardized format- commonly used to -transfer data- as text that can be sent over a network.

def solicitar_pokemon():
    url_utilizada=f"https://pokeapi.co/api/v2/berry/{nombre_fruta}/"; #importar url con formato f"ej.com"
    response=requests.get(url_utilizada) #The get() method returns the value of the item with the specified key

    if response.status_code==200:
        data=response.json;

        nombre=data["name"];

        resultado=(f"El nombre de la fruta es: ¡{nombre!}");