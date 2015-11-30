# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

@auth.requires_login()
def index():
    itens = db(db.item.created_by == auth.user.id).select()
    recipies = db(db.recipe.created_by == auth.user.id).select()

    return locals()

def edit_item():
    item_id = request.args(0) or redirect(URL(c='garden', f='index'))
    form = crud.update(db.item, item_id, next=URL(c='garden', f='index'))
    return locals()

def add_item():
    form = crud.create(db.item, next=URL(c='garden', f='index'))
    return locals()

def detail():
    item_id = request.args(0) or redirect(UR(c='default', f='index'))
    item = db(db.item.id == item_id).select()

    return locals()

def add_recipe():
    form = crud.create(db.recipe, next=URL(c='garden', f='index'), messages=T("Recipie add successfully"))
    return locals()

def add_recipe_list():
    itens = db(db.item.id > 0).select(orderby=db.item.item_name)

    return locals()