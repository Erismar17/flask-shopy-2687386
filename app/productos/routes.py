from app.productos import productos
from flask import render_template
from .froms import NewProductForm

@productos.route('/create')
def crear():
    form = NewProductForm()
    return render_template('new.html',
                           form = form)