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
    # Clase 1: Ejercicios Practicos
    ## El Punto de Partida

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Total de muestras

    Calcula el **numero total de muestras** para un audio de **3 segundos** grabado a **48000 Hz**.
    Guarda el resultado en una variable llamada `total_muestras` e imprimi el resultado.
    """)
    return


@app.cell
def _():
    duracion = 3
    sample_rate = 48000
    total_muestras = duracion * sample_rate
    print(total_muestras)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Tamano de archivo WAV

    Calcula el **tamano en MB** de un archivo WAV con las siguientes caracteristicas:
    - Estereo (2 canales)
    - Bit depth: 16 bits
    - Sample rate: 44100 Hz
    - Duracion: 5 segundos

    Formula: `tamano_bytes = sample_rate * duracion * canales * (bit_depth / 8)`

    Guarda el resultado en `tamano_mb` e imprimi con 2 decimales.
    """)
    return


@app.cell
def _():
    canales = 2
    bit_depth = 16 
    duracion2 = 5
    sample_rate2 = 44100
    tamano_bytes = sample_rate2 * duracion2 * canales * (bit_depth/8)
    tamano_mb = tamano_bytes/(10**6)
    print(f"{tamano_mb: .2f} MB")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Convertir segundos a mm:ss

    Dada una duracion en segundos (`duracion_seg = 197`), convertila al formato **mm:ss** usando los operadores `//` y `%`.

    El resultado debe ser un string como `"3:17"`.
    """)
    return


@app.cell
def _():
    #total:
    duracion_segundos = 197

    #minutos del total(cantidad exacta de 60 segundos en 197 segundos)
    minutos = duracion_segundos // 60

    #segundos del total(lo que sobra de calcular la cantidad exacta de 60 segundos en 197 segundos)
    segundos = duracion_segundos % 60

    print(f"{minutos}:{segundos}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Extraer extension de archivo

    Dado el nombre de archivo `nombre = "mi_cancion_final_v2.wav"`, extraer:
    1. La **extension** (sin el punto): `"wav"`
    2. El **nombre sin extension**: `"mi_cancion_final_v2"`

    Usa metodos de strings (`.split()`, slicing, etc.).
    """)
    return


@app.cell
def _():
    archivo = "mi_cancion_final_v2.wav"
    parte = archivo.split(".")
    extension = parte[1]
    nombre = parte[0]
    print(extension)
    print(nombre)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Frecuencia de una nota MIDI

    La formula para convertir un numero de nota MIDI a frecuencia en Hz es:

    $$f = 440 \times 2^{(midi - 69) / 12}$$

    Calcula la frecuencia de las siguientes notas MIDI:
    - **60** (Do central / Middle C)
    - **69** (La 440 / A4)
    - **72** (Do una octava arriba / C5)

    Imprimi cada resultado con 2 decimales.
    """)
    return


@app.cell
def _():
    #notas midi
    C4 = 60
    A4 = 69
    C5 = 72

    #convertir a frecuencias
    fC4 = 440 * (2 ** ((C4 - 69)/12))
    fA4 = 440 * (2 ** ((A4 - 69)/12))
    fC5 = 440 * (2 ** ((C5 - 69)/12))

    #imprimir
    print(f"Do central(60) : {fC4 : .2f} Hz\nLa 440(69) : {fA4 : .2f} Hz\nDo una octava arriba(72) : {fC5 : .2f} Hz")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: f-string descriptivo

    Crea las siguientes variables:
    - `titulo = "Bohemian Rhapsody"`
    - `artista = "Queen"`
    - `duracion_seg = 354`
    - `sample_rate = 44100`
    - `bit_depth = 24`

    Usando f-strings, crea un string `info` que muestre:
    ```
    Pista: Bohemian Rhapsody - Queen
    Duracion: 5:54
    Formato: 44,100 Hz / 24 bits
    Total muestras: 15,609,400
    ```
    Imprimi el resultado.
    """)
    return


@app.cell
def _():
    titulo = "Bohemian Rhapsody"
    artista = "Queen"
    duracion_seg = 354
    sample_rate3 = 44100
    bit_depth3 = 24

    #convierto duracion en segundos a formato mm:ss

    minutos2 = duracion_seg // 60
    segundos2 = duracion_seg % 60




    info = f"Pista: {titulo} - {artista} \nDuracion: {minutos2}:{segundos2} \nFormato: {sample_rate3:,} Hz / {bit_depth3} bits\nTotal muestras: {duracion_seg * sample_rate3:,}"

    print(info)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Logica booleana para calidad de audio

    Crea las variables:
    - `sr = 48000` (sample rate)
    - `bits = 24` (bit depth)
    - `canales = 2` (numero de canales)

    Determina (como booleanos):
    1. `es_profesional`: el sample rate es >= 44100 **Y** el bit depth es >= 16
    2. `es_hd`: el sample rate es >= 96000 **O** el bit depth es >= 24
    3. `es_surround`: el numero de canales es > 2
    4. `calidad_ok`: es profesional **Y NO** es surround (estereo profesional)

    Imprimi cada resultado.
    """)
    return


@app.cell
def _():
    sr = 48000 
    bits = 24
    canales2 = 2

    es_profesional = sr >= 44100 and bits >= 16
    es_hd = sr >= 96000 or bits >= 24
    es_surround = canales2 > 2
    calidad_ok = es_profesional and not es_surround

    print(f"Es profesional: {es_profesional}\nEs hd: {es_hd}\nEs sourround: {es_surround}\nCalidad ok: {calidad_ok }")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Frecuencia de Nyquist

    La **frecuencia de Nyquist** es la maxima frecuencia que se puede representar con un sample rate dado.
    Se calcula como: `f_nyquist = sample_rate / 2`

    Para los siguientes sample rates, calcula e imprimi la frecuencia de Nyquist:
    - 22050 Hz
    - 44100 Hz
    - 48000 Hz
    - 96000 Hz
    - 192000 Hz

    Imprimi en formato: `"SR: 44100 Hz -> Nyquist: 22050.0 Hz"`
    """)
    return


@app.cell
def _():
    #creo una lista con los valores de frecuencia que quiero calcular
    lista = [22050, 44100, 48000, 96000, 192000]

    #creo bucle for para que pase por todos los elementos de la lista y me devuelva cada frecuencia de Niquist
    for sr1 in lista:
        f_ny = sr1 / 2
        print(f"SR: {sr1} Hz -> Nyquist: {f_ny} Hz")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio BONUS: Calculadora de latencia

    La **latencia** de un buffer de audio se calcula como:

    $$latencia_{ms} = \frac{buffer\_size}{sample\_rate} \times 1000$$

    Calcula la latencia para las siguientes combinaciones:
    - Buffer: 64, SR: 44100
    - Buffer: 128, SR: 44100
    - Buffer: 256, SR: 48000
    - Buffer: 512, SR: 96000

    Imprimi cada resultado con 2 decimales en formato:
    `"Buffer: 64 @ 44100 Hz -> Latencia: X.XX ms"`
    """)
    return


@app.cell
def _():
    #creo lista para cada valor de buffer y sr

    buffer = [64,128,256,512]
    sr2 = [44100,44100,48000,96000]

    #creo bucle for para calcular la latencia de las combinaciones

    for buf, s in zip(buffer, sr2): 
        latencia_ms = (buf / s) * 1000
        print(f"Buffer: {buf} @ {s} Hz -> Latencia: {latencia_ms:.2f} ms")
    return


if __name__ == "__main__":
    app.run()
