import unittest
from flask import Flask, jsonify
from App.app import app


class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client using Flask's testing utilities
        self.app = app.test_client()

        # Enable Flask's testing mode
        app.testing = True

    def test_get_contacts_positive_case(self):
        response = self.app.get('/contacts')
        self.assertEqual(response.status_code, 200)
        contacts = response.get_json()
        self.assertIsInstance(contacts, list)

    def test_get_contacts_list_positive_case(self):
        response = self.app.get('/contacts-list')
        self.assertEqual(response.status_code, 201)
        contacts = response.get_json()
        self.assertIsInstance(contacts, list)
        self.assertEqual(contacts[0], {'id': 1, 'name': 'Komal', 'ph_no': 9876543210})
        self.assertEqual(contacts[0]['name'], 'Komal')
        self.assertEqual(contacts[1], {'id': 2, 'name': 'Sai', 'ph_no': 9876543211})
        self.assertEqual(contacts[1]['name'], 'Sai')
        self.assertEqual(contacts[2]['name'], 'Kiran')

    def test_get_contacts_list_negative(self):
        response = self.app.get('/contacts-list')
        self.assertNotEqual(response.status_code, 200)
        contacts = response.get_json()
        self.assertIsInstance(contacts, list)
        self.assertNotEqual(contacts[0], {'id': 2, 'name': 'Sai', 'ph_no': 9876543211})  # here we get an error while running the class but not while ruinning this def function because we have updated sai name with komal sai kiran in update method
        self.assertNotEqual(contacts[0]['name'], 'Sai')

    def test_add_contact(self):
        new_contact = {'name': 'Usha', 'ph_no': 9876543213}
        response = self.app.post('/add_contact', json=new_contact)
        self.assertEqual(response.status_code, 201)
        created_contact = response.get_json()
        self.assertIsInstance(created_contact, dict)
        self.assertEqual(created_contact, {'id': 4, 'name': 'Usha', 'ph_no': 9876543213})
        self.assertEqual(created_contact['name'], new_contact['name'])
        self.assertEqual(created_contact['ph_no'], 9876543213)
        self.assertEqual(created_contact['id'], 4)


    def test_update_contact(self):
        contact_id = 1
        updated_contact = {'name': 'Komal Sai Kiran'}
        response = self.app.put(f'/contacts/{contact_id}', json=updated_contact)
        self.assertEqual(response.status_code, 200)
        updated_contact_response = response.get_json()
        print(updated_contact_response)
        self.assertIsInstance( updated_contact_response, dict)
        self.assertEqual( updated_contact_response['name'], updated_contact['name'])
        #self.assertEqual( updated_contact_response['ph_no'], updated_contact['ph_no']) #it will be failed because we have updating only ph no but not updating phone number

    def test_delete_contact(self):
        contact_id = 1
        response = self.app.delete(f'/contacts/{contact_id}')
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        print(response_data)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['msg'], '1 contact  has been deleted')

