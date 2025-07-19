# Importar
from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')
        text_top = request.form.get("textTop")
        text_bottom = request.form.get("textBottom")
        text_bottom_y = request.form.get("textBottom_y")
        text_top_y = request.form.get("textTop_y")
        selected_color = request.form.get("color-selector")
        # Asignación #2. Recepción del texto
        

        # Assignment #3. Receiving the text's positioning
       

        # Asignación #3. Recepción del posicionamiento del texto
        

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 
                               text_top = text_top , text_bottom = text_bottom,
                               text_bottom_y = text_bottom_y,
                               text_top_y = text_top_y, selected_color = selected_color

                               # Asignación #2. Visualización del texto
                               

                               #  Asignación #3. Visualización del color
                               
                               
                               # Asignación #3. Visualización de la posición del texto


                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)



@app.route("/coleccion")
def coleccion():
    image_folder = 'static/img'
    image_files = [img for img in os.listdir(image_folder)
                   if img.endswith(('.png', '.jpg', '.jpeg'))]
    return render_template("coleccion.html", images=image_files)

app.run(debug=True)
