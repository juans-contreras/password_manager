from flask import Flask,render_template 

app=Flask(__name__)

@app.route('/')  # defino la ruta en este caso al no tener nada es la raiz
# luego defino que hace esta ruta
def index():
    #return 'lol  Mundo'  # note que podemos devolver texto plano
    #definimos un diccionario el cual le mandaremos a la plantilla para usarlo, note que en esta puede retornar todo tipo de datos

    #definimos una lista para devolver dentro del diccionario
    num=[1,2,3,4,5,6,7,8,9,0]
    user='admin'
    data={
        'titulo': 'index',
        'mensaje': 'holiwis',
        'Usuario': user,
        'lista': num,
        'long':len(num),

    }
    return render_template('index.html', dicc=data) #envia el diccionario 


#como se depura
if __name__=='__main__':
    app.run(debug=True)

