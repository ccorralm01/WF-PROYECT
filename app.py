from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

# Ruta para obtener la información del ítem
@app.route('/item/<item_name>')
def get_item_info(item_name):
    # Configuración de la URL base, idioma y plataforma
    base_url = "https://api.warframe.market/v1"
    headers = {
        "Accept": "application/json",
        "Language": "es",
        "Platform": "pc"
    }

    # Hacer la solicitud GET
    response = requests.get(f"{base_url}/items/{item_name}/orders", headers=headers)

    # Verificar el estado de la respuesta y procesar la información del ítem
    if response.status_code == 200:
        item_info = response.json()

        # Renderizar la plantilla HTML con el JSON completo formateado
        return render_template('item_info.html', item_info=item_info)
    else:
        return jsonify({'error': f"Error: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
