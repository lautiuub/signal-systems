import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 2: Ejercicios Practicos
    ## Hablar en Python

    Resuelve cada ejercicio en la celda indicada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Clasificar frecuencias

    Escribi un condicional que clasifique una frecuencia en las siguientes categorias:

    | Rango (Hz) | Categoria |
    |-----------|-----------|
    | 20 - 60 | Sub-bass |
    | 60 - 250 | Bass |
    | 250 - 4000 | Mid |
    | 4000 - 12000 | Treble |
    | 12000 - 20000 | Ultra-treble |

    Proba con `freq = 880` y con `freq = 35`. Imprimi el resultado.
    """)
    return


@app.cell
def _():
    freq = 35

    #escribo condiciones para la frecuencia freq y su clasificacion

    if 20 <= freq < 60:
        categoria = "Sub-bass"
    elif 60 <= freq < 250:
        categoria = "Bass"
    elif 250 <= freq < 4000:
        categoria = "Mid"
    elif 4000<= freq < 12000:
        categoria = "Treble"
    else: 
        categoria = "Ultra-treble"

    print(f"Frecuencia: {freq} Hz -> categoria: {categoria}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Primeros 10 armonicos

    Dado un `fundamental = 220` Hz (A3), crea un bucle `for` que genere e imprima los primeros **10 armonicos**.

    Recordatorio: el armonico N tiene frecuencia = fundamental * N.

    Formato de salida: `"Armonico 1: 220 Hz"`
    """)
    return


@app.cell
def _():
    #fundamental

    fundamental = 220

    #genero secuencia de numeros enteros consecutivos, algo asi como una lista con los numeros enteros del 1 al 10(inclusives) ->range(1,11)

    for n in range(1,11,1):
        arm_n = fundamental * n
        print(f"Armonico {n}: {arm_n} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Amplitudes a dB (list comprehension)

    Dada la lista `amplitudes = [1.0, 0.707, 0.5, 0.25, 0.1, 0.01]`, crea una list comprehension que convierta cada valor a dB usando la formula:

    $$dB = 20 \times \log_{10}(amplitud)$$

    Necesitas importar `math` y usar `math.log10()`.

    Imprimi cada par (lineal, dB) con formato.
    """)
    return


@app.cell
def _():
    import math

    amplitudes = [1.0, 0.707, 0.5, 0.25, 0.1, 0.01]

    #creo list comprehension que me convierta las amplitudes de db

    ampdb = [20 * math.log10(a) for a in amplitudes]

    print(f"Lineal -> dB: ")
    for l, dB in zip(amplitudes,ampdb):
        print(f"Lineal: {l:5.2f} -> dB: {dB:6.1f}")
    return (math,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Diccionario de bandas de octava

    Crea un diccionario que mapee las frecuencias centrales de las bandas de octava estandar a su **ancho de banda**. El ancho de banda de una banda de octava es: `bw = fc * (sqrt(2) - 1/sqrt(2))` donde `fc` es la frecuencia central.

    Frecuencias centrales: `[125, 250, 500, 1000, 2000, 4000, 8000]`

    Imprimi el diccionario con formato: `"125 Hz: BW = XX.X Hz"`
    """)
    return


@app.cell
def _(math):
    fc = [125, 250, 500, 1000, 2000, 4000, 8000]

    #creo list comprehension que contenga ancho de banda asociado a frec central

    ancho_banda = [frecc * (math.sqrt(2) - 1/math.sqrt(2)) for frecc in fc]

    #indico el formato en que presento resultados, y presento resultados

    print(f"Frecuencia (Hz): BW (Hz):")
    for f,bw in zip(fc,ancho_banda):
        print(f"{f} Hz: BW = {bw:2.1f} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Filtrar archivos de audio por metadata

    Dada la siguiente lista de diccionarios:

    ```python
    archivos = [
        {"nombre": "voz.wav", "sr": 44100, "bits": 16, "duracion": 30.0},
        {"nombre": "guitarra.wav", "sr": 22050, "bits": 16, "duracion": 120.0},
        {"nombre": "master.wav", "sr": 96000, "bits": 32, "duracion": 240.0},
        {"nombre": "borrador.wav", "sr": 8000, "bits": 8, "duracion": 5.0},
        {"nombre": "drums.wav", "sr": 48000, "bits": 24, "duracion": 60.0},
    ]
    ```

    Usando list comprehension, filtra los archivos que tengan `sr >= 44100`.
    Imprimi los nombres de los archivos que pasan el filtro.
    """)
    return


@app.cell
def _():
    archivos = [
        {"nombre": "voz.wav", "sr": 44100, "bits": 16, "duracion": 30.0},
        {"nombre": "guitarra.wav", "sr": 22050, "bits": 16, "duracion": 120.0},
        {"nombre": "master.wav", "sr": 96000, "bits": 32, "duracion": 240.0},
        {"nombre": "borrador.wav", "sr": 8000, "bits": 8, "duracion": 5.0},
        {"nombre": "drums.wav", "sr": 48000, "bits": 24, "duracion": 60.0},
    ]

    #creo list comprehension para realizar filtrado

    arch_nomb = [ar["nombre"] for ar in archivos if ar["sr"] >= 44100]

    #imprimo

    print(arch_nomb)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Tabla frecuencia x armonico

    Usando bucles anidados, crea una tabla donde:
    - Las filas son frecuencias fundamentales: `[100, 200, 440]`
    - Las columnas son numeros de armonico: `[1, 2, 3, 4, 5]`
    - Cada celda muestra `fundamental * armonico`

    Formato de salida (con alineacion):
    ```
         |     x1     x2     x3     x4     x5
    -----|------------------------------------
     100 |    100    200    300    400    500
     200 |    200    400    600    800   1000
     440 |    440    880   1320   1760   2200
    ```
    """)
    return


@app.cell
def _():
    fundamentales = [100, 200, 440]
    columnas = [1, 2, 3, 4, 5]

    print(f"     |", end="")
    for col in columnas:
        print(f"{'x'+str(col):>6}", end="")
    print()
    print("-----|" + "-"*(6*len(columnas)))

    #creo las 3 filas con las 3 fundamentales
    for fund in fundamentales:
        print(f"{fund:>4} |", end=" ")

        #creo las columnas de las fundamentales(son multiplos de las mismas)

        for col in columnas:
            print(f"{fund*col:>5}", end=" ")
        print()


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Track listing con enumerate

    Dada la lista:
    ```python
    album = ["Speak to Me", "Breathe", "On the Run", "Time",
             "The Great Gig in the Sky", "Money", "Us and Them",
             "Any Colour You Like", "Brain Damage", "Eclipse"]
    ```

    Usa `enumerate` para imprimir un listado numerado empezando en 1:
    ```
    01. Speak to Me
    02. Breathe
    ...
    ```
    """)
    return


@app.cell
def _():
    album = ["Speak to Me", "Breathe", "On the Run", "Time",
             "The Great Gig in the Sky", "Money", "Us and Them",
             "Any Colour You Like", "Brain Damage", "Eclipse"]

    #enumerate recorre el album dandole un numero a cada track, y cada track tiene su "valor". Entonces se obtiene algo similar a 1. Valor 1 ...

    for numero, cancion in enumerate(album, start = 1):
        print(f"{numero:02d}. {cancion}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Stereo pairs con zip

    Dadas las muestras del canal izquierdo y derecho:
    ```python
    left =  [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4]
    right = [0.3, -0.1, 0.6, -0.4, 0.1, -0.7, 0.3]
    ```

    Usa `zip` para:
    1. Crear una lista de tuplas `stereo_pairs` con los pares (L, R)
    2. Calcular la senal mono (promedio de L y R) para cada muestra
    3. Imprimi cada muestra: `"Muestra 0: L=+0.50, R=+0.30, Mono=+0.40"`
    """)
    return


@app.cell
def _():
    left =  [0.5, -0.3, 0.8, -0.6, 0.2, -0.9, 0.4]
    right = [0.3, -0.1, 0.6, -0.4, 0.1, -0.7, 0.3]

    #creo lista de tuplas con los pares (L,R)

    stereo_pairs = list(zip(left, right))

    for i, (l, r) in enumerate(stereo_pairs):
        mono = (l+r)/2
        print(f"Muestra {i}: L = {l:+}, R = {r:+}, Mono = {mono:+.2f}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Operaciones con sets

    Dados los sample rates soportados por dos interfaces de audio:
    ```python
    interface_a = {44100, 48000, 88200, 96000, 176400, 192000}
    interface_b = {44100, 48000, 96000}
    ```

    Calcula e imprimi:
    1. Sample rates soportados por **ambas** interfaces
    2. Sample rates soportados por **al menos una** interfaz
    3. Sample rates que tiene la interfaz A pero **no** la B
    4. Si los SR de la interfaz B son un **subconjunto** de los de la A
    """)
    return


@app.cell
def _():
    interface_a = {44100, 48000, 88200, 96000, 176400, 192000}
    interface_b = {44100, 48000, 96000}

    sr_ambas = interface_a & interface_b
    sr_una = interface_a | interface_b
    sr_a = interface_a - interface_b
    es_subconjunto = interface_b <= interface_a

    print(f"SR soportados por ambas interfaces: {sr_ambas}")
    print(f"SR soportados por al menos una interfaz: {sr_una}")
    print(f"SR que tienen interfaz A pero no la B: {sr_a}")
    print(f"Son los SR de la interfaz B un subconjunto de los de la A?: {es_subconjunto}")


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Dict comprehension - Notas y frecuencias

    Crea un diccionario usando **dictionary comprehension** que mapee los nombres de las notas de A3 a A5 a sus frecuencias.

    Datos de entrada:
    ```python
    nombres_notas = ["A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5"]
    midi_base = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81]
    ```

    Formula MIDI a Hz: `f = 440 * 2**((midi - 69) / 12)`

    El diccionario debe ser: `{"A3": 220.0, "B3": 246.94, ...}`
    """)
    return


@app.cell
def _():
    nombres_notas = ["A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5"]
    midi_base = [57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81]

    dicc = {nn : 440 * 2**((m - 69) / 12) for nn, m in zip(nombres_notas, midi_base)}

    for nota, freq in dicc.items():
        print(f"{nota} : {freq:.2f} Hz")
  

    return


if __name__ == "__main__":
    app.run()
