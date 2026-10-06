from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
	return jsonify({
	    "mensaje": "Bienvenidos a la materia de redes",
	    "curso": "Programacion de redes"
})

@app.route("/alumnos")
def alumnos():
	return jsonify([
  {
	"id": 1,
	"nombre": "Ana"
},
{
	"id": 2,
	"nombre": "Carlos"
	}
])

if __name__ == "__main__":
	app.run(debug=True)