from flask import Blueprint, render_template, redirect, url_for, flash
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################


@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)


@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = GroceryStoreForm()
    form_valid = form.validate_on_submit()

    if form_valid:
        store = GroceryStore(
            title=form.title.data,
            address=form.address.data
        )
        db.session.add(store)
        db.session.commit()
        flash('Store successfully created!')
        return redirect(url_for('main.store_detail', store_id=store.id))

    return render_template('new_store.html', form=form)


@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    form = GroceryItemForm()
    form_valid = form.validate_on_submit()

    if form_valid:
        item = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Item successfully created!')
        return redirect(url_for('main.item_detail', item_id=item.id))

    return render_template('new_item.html', form=form)


@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    form = GroceryStoreForm(obj=store)
    form_valid = form.validate_on_submit()

    if form_valid:
        store.title = form.title.data
        store.address = form.address.data
        db.session.add(store)
        db.session.commit()
        flash('Store successfully updated!')
        return redirect(url_for('main.store_detail', store_id=store.id, store=store))

    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store, form=form)


@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    form = GroceryItemForm(obj=item)
    form_valid = form.validate_on_submit()

    if form_valid:
        item.name = form.name.data
        item.price = form.price.data
        item.category = form.category.data
        item.photo_url = form.photo_url.data
        item.store = form.store.data
        db.session.add(item)
        db.session.commit()

        flash('Item was successfully updated!')
        return redirect(url_for('main.item_detail', item_id=item.id, item=item))

    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item, form = form)
