#LAS SIGUIENTES DEPENDENCIAS SON REMOVIDAS DEL ARCHIVO MAIN.PY
#SE DEBEN ELIMINAR EN DICHO ARCHIVO Y PEGARLOS EN ESTE
#LAS DEPENDENCIAS DE WTFORM SE ELIMINAN
from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from flask_bootstrap import Bootstrap

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#inicialiar el objeto sqlalchemy 
db = SQLAlchemy(app)
migrate = Migrate(app , db )

# registrar modulo
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#creamos la importación del modelo y sus clases.
from .models import Cliente, Producto, Venta, Detalle