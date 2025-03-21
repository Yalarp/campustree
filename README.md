# Campus Tree Mapper

Campus Tree Mapper is a web application that allows users to map and explore trees on a campus. Users can add new trees, update their locations, search for trees by name or species, and delete trees from the map. The application uses Flask for the backend and Leaflet.js for the interactive map.

## Features

- Add new trees with name, species, description, and image.
- Update the location of existing trees by dragging markers on the map.
- Search for trees by name, species, or description.
- Delete trees from the map.
- Switch between standard and satellite map views.
- Fly to a random tree location with the "Excite Me" button.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/campus-tree-mapper.git
cd campus-tree-mapper
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to use the application.

## File Structure

```
campus-tree-mapper/
│
├─ static/
│  ├─ uploads/
│  ├─ style.css
│  ├─ oaktree.jpeg
│  ├─ sdfd.jpg
│
├─ templates/
│  ├─ index.html
│
├─ app.py
├─ README.md
├─ requirements.txt
├─ trees.json
├─ templates.zip
```

- `static/uploads/`: Directory to store uploaded tree images.
- `static/style.css`: CSS file for styling the application.
- `static/oaktree.jpeg` and `static/sdfd.jpg`: Example tree images.
- `templates/index.html`: HTML template for the main page.
- `app.py`: Flask application file.
- `README.md`: This README file.
- `requirements.txt`: List of required Python packages.
- `trees.json`: JSON file to store tree data.
- `templates.zip`: ZIP file containing the HTML template (optional).

## Usage

1. Open the application in your browser.
2. Use the form to add new trees to the map. Provide the tree name, species, description, and upload an image.
3. Click on the map to select the location for the new tree.
4. Use the search bar to find trees by name, species, or description.
5. Drag tree markers to update their locations.
6. Click the "Excite Me" button to fly to a random tree location.
7. Click on a tree marker to view its details and delete it if needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Leaflet.js for the interactive map.
- Flask for the backend.
- Font Awesome for icons.