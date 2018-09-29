from bson.objectid import ObjectId
from flask import Blueprint, render_template, flash, redirect

users = Blueprint('user', __name__)
@users.route('/users')
def get_users():
    usuarios = [u for u in db.usuarios.find()]
    return render_template('user.html', qtd=len(usuarios), usuarios=usuarios)

@users.route('/users/edit/<uid>', methods=['GET', 'POST'])
def edit_users(uid):
    query = {'_id' : ObjectId(uid)}
    if request.method == 'GET':
        usuario = db.usuarios.find_one(query)
        return render_template('edit_user.html', usuario=usuario)
    else:
        db.usuarios.update(query, request.form)
        flash('Usuarios {0} removido com sucesso!'.format(request.form['nome']), 'success')
        return redirect('/users')

@users.route('/users/delete/<uid>') 
def delete_users(uid):
    #db.usuarios.remove({'_id' : ObjectId(uid)})
    flash('Usuarios {0} removido com sucesso!'.format(uid), 'success')
    return redirect('/users')