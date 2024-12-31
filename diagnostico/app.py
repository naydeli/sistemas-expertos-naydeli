from flask import Flask, request, render_template, jsonify
from diagnostico import DiagnosticoComputadora, Fact

app = Flask(__name__)

# Creamos una instancia del motor de reglas
engine = DiagnosticoComputadora()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosticar', methods=['POST'])
def diagnosticar():
    problema = request.form.get('problema')

    if problema:
        # Reiniciar el motor de reglas y declarar el problema
        engine.reset()
        engine.declare(Fact(problema=problema))
        engine.run()

        # Obtener la sugerencia generada por el motor de reglas
        sugerencia = engine.get_sugerencia()  # Método para obtener la sugerencia
        return jsonify({'sugerencia': sugerencia})
        
    else:
        return jsonify({'error': 'Problema no válido'})

if __name__ == '__main__':
    app.run(port=8080)
    
    