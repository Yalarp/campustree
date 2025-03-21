from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
TREE_DATA_FILE = "trees.json"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def load_trees():
    if os.path.exists(TREE_DATA_FILE):
        with open(TREE_DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_trees(trees):
    with open(TREE_DATA_FILE, "w") as file:
        json.dump(trees, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_trees')
def get_trees():
    return jsonify(load_trees())

@app.route('/add_tree', methods=['POST'])
def add_tree():
    trees = load_trees()
    name = request.form['name']
    species = request.form['species']
    description = request.form['description']
    lat = float(request.form['lat'])
    lng = float(request.form['lng'])

    image = request.files['image']
    image_filename = f"{name.replace(' ', '_')}.jpg"
    image.save(os.path.join(UPLOAD_FOLDER, image_filename))

    new_tree = {
        "name": name,
        "species": species,
        "description": description,
        "lat": lat,
        "lng": lng,
        "image": image_filename
    }
    
    trees.append(new_tree)
    save_trees(trees)
    return jsonify(new_tree)

@app.route('/update_tree_location', methods=['POST'])
def update_tree_location():
    trees = load_trees()
    data = request.json
    for tree in trees:
        if tree["name"] == data["name"]:
            tree["lat"] = data["lat"]
            tree["lng"] = data["lng"]
            break
    save_trees(trees)
    return jsonify({"message": "Tree location updated!"})

@app.route('/delete_tree', methods=['POST'])
def delete_tree():
    trees = load_trees()
    data = request.json
    trees = [tree for tree in trees if tree["name"] != data["name"]]
    save_trees(trees)
    return jsonify({"message": "Tree deleted!"})

if __name__ == '__main__':
    app.run(debug=True)