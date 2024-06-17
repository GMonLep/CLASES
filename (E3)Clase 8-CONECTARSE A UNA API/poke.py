import tkinter as tk
#Tkinter es una biblioteca estándar de Python que se utiliza para crear interfaces gráficas de usuario (GUI, por sus siglas en inglés). Proporciona una forma sencilla de crear ventanas, botones, cuadros de texto y otros elementos de interfaz gráfica.

#la parte de 'as tk' sirve para darle un "acronimo"

import requests #para las solicitudes http a la API

from io import BytesIO #manejar datos binarios
from PIL import Image, ImageTk

def buscar_pokemon():
    nombre_pokemon=entry_pokemon.get().lower(); #obtenemos el nombre del pokemon
    url=f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}";

    response=requests.get(url); #realizamos una solicitud get con la url

    if response.status_code==200:
        data=response.json();

        nombre=data["name"];
        numero=data["id"];
        tipos=[tipo["type"]["name"] for tipo in data ["types"]];
        


        resultado=f"Nombre: {nombre}\nNúmero: {numero}\nTipo(s): {','.join(tipos)}\nHabilidad: ";


        imagen_url=data["sprites"]["front_default"];
        response_imagen=requests.get(imagen_url); #realizamos get a la imagen
        image=Image.open(BytesIO(response_imagen.content));
        imagen=image.resize((300,300),Image.Resampling.LANCZOS);
        foto=ImageTk.PhotoImage(imagen); #convertimos para trabajar con tkinter
        label_imagen.config(image=foto);#configura label para mostrar la foto
        label_imagen.image=foto; #guarda una referencia a la imagen paa evitar que sea eliminada for recolector de basura
    else:
        resultado="No se encontró el pokemoncillo, sigue cazando."
        label_imagen.config(image=None);
    label_resultado.config(text=resultado);

window=tk.Tk();#creo la ventana principal
window.title("BUSCADOR DE POKEMONES");

label_pokemon=tk.Label(window,text=("Ingresa el nombre del pokemon"));
label_pokemon.pack();

entry_pokemon=tk.Entry(window);
entry_pokemon.pack();

button_buscar=tk.Button(window, text="¡Busca!", command=buscar_pokemon);
button_buscar.pack()

label_resultado=tk.Label(window,text="");#creamos una etiqueta vacia para mostar el resultado por ventana
label_resultado.pack()

label_imagen=tk.Label(window);
label_imagen.pack();

window.mainloop();

