from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory database)
contacts = [
    {'id': 1, 'name': 'Komal', 'ph_no': 9876543210},
    {'id': 2, 'name': 'Sai', 'ph_no': 9876543211},
    {'id': 3, 'name': 'Kiran', 'ph_no': 9876543212},
    ]


# GET method to retrieve all data
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts), 200


# GET method to retrieve all data
@app.route('/contacts-list', methods=['GET'])
def get_contacts_list():
    return jsonify(contacts), 201


# POST method to add a new contact
@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = {
        'id': len(contacts) + 1,
        'name': data.get('name'),
        'ph_no': data.get('ph_no'),
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201


# PUT method to update a specific contact
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.get_json()
    for item in contacts:
        if item['id'] == contact_id:
            item['name'] = data.get('name')
            item['ph_no'] = data.get('ph_no')
            return jsonify(item)
    return jsonify({'message': 'contact not found'}), 404


# DELETE method to delete a specific contact
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    for index, item in enumerate(contacts):
        if item['id'] == contact_id:
            del contacts[index]
            return jsonify({'status': "Success", 'id': contact_id, 'msg': f'{contact_id} contact has been deleted'}), 201


if __name__ == '__main__':
    app.run(debug=True)
