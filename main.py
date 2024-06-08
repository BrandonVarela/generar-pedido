

from flask import Flask, render_template, request, redirect, make_response, render_template_string
import json
import re
import os
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route("/")
def raiz():
    return render_template("inicio.html")


@app.route("/detalle-compra", methods=['POST'])
def suma():
    try:
        bola1=request.form['bola1']
        bolas2=request.form['bolas2']
        bolas2c=request.form['bolas2c']
        bolas3=request.form['bolas3']
        bolas4=request.form['bolas4']
        ensalada1=request.form['ensalada1']
        ensalada2=request.form['ensalada2']
        ensalada3=request.form['ensalada3']
        ensalada4=request.form['ensalada4']
        ensalada5=request.form['ensalada5']
        oblea=request.form['oblea']
        brownie=request.form['brownie']
        bnnsplit=request.form['bnnsplit']
        minibnn=request.form['minibnn']
        fresas=request.form['fresas']
        jleche=request.form['jleche']
        jagua=request.form['jagua']
        malteada=request.form['malteada']
        mlitro=request.form['mlitro']
        adbola=request.form['adbola']

        if bolas2== '': bolas2=0
        if bolas2c== '': bolas2c=0
        if bolas3== '': bolas3=0
        if bolas4== '': bolas4=0
        if ensalada1== '': ensalada1=0
        if ensalada2== '': ensalada2=0
        if ensalada3== '': ensalada3=0
        if ensalada4== '': ensalada4=0
        if ensalada5== '': ensalada5=0
        if oblea== '': oblea=0
        if brownie== '': brownie=0
        if bnnsplit== '': bnnsplit=0
        if minibnn== '': minibnn=0
        if fresas== '': fresas=0
        if jleche== '': jleche=0
        if jagua== '': jagua=0
        if malteada== '': malteada=0
        if mlitro== '': mlitro=0
        if adbola== '': adbola=0

        cant_art=[bola1, bolas2, bolas2c, bolas3, bolas4, ensalada1, ensalada2, ensalada3, ensalada4, ensalada5, oblea, brownie, bnnsplit, minibnn, fresas, jleche, jagua, malteada, mlitro, adbola]
        nombre_art=['Cono de 1 bola','Cono de 2 bolas', 'Canasta de 2 bolas', 'Canasta de 3 bolas', 'Canasta de 4 bolas', 'Ensalada de 3.000', 'Ensalada de 7.000', 'Ensalada de 8.500', 'Ensalada de 10.000', 'Ensalada de 10.000 + 1.000 para llevar','Oblea', 'Brownie con helado', 'Banana Split', 'Mini Banana', 'Fresas con Crema', 'Jugo en leche', 'Jugo en agua', 'Malteada', 'Helado medio-litro', 'Adición de bola de helado']
        precios=[1500, 2600, 2700, 3800, 5000, 3000, 7000, 8500, 10000, 11000, 2000, 5000, 7000, 2000, 3000, 3000, 2500, 6000, 3800, 1300]

        total = 0

        df = pd.DataFrame(columns=['Descripción','Cantidad','Precio unitario','Precio'])

        for i in range(len(precios)):
            if cant_art[i]!=0:
                total_art=int(cant_art[i])*precios[i]
                total=total+total_art
                df.at[i, 'Descripción'] = nombre_art[i]
                df.at[i, 'Cantidad'] = cant_art[i]
                df.at[i, 'Precio unitario'] = precios[i]
                df.at[i, 'Precio'] = int(cant_art[i])*precios[i]
        
        df['Precio unitario'] = df['Precio unitario'].apply(lambda x: f"{x:,}")
        df['Precio'] = df['Precio'].apply(lambda x: f"{x:,}")

        tabla_html=df.to_html(classes='table table-striped', index=False)

        detalle=f'Valor total:  {total:,}'

        return render_template("rpedido.html", message=detalle, table=tabla_html)
    except:
        return render_template("rpedido.html", message=f'Cantidades ingresadas incorrectamente. Recuerde que solo debe ingresar números sin puntos')


def main():
    app.run(host='localhost', port=9606, debug=True)
    

if __name__ == "__main__":
    main()