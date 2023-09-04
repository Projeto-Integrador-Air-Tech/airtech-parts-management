import jwt
from flask import request, abort, make_response, jsonify
class PartsManipulation():

    def __init__(self, app):
        self.app = app
        app.route('/registration', methods=['POST'])(self.registration_parts)
        # app.route('/modification', methods=['PUT'])(self.get_alocation)
        # app.route('/alocation', methods=['POST'])(self.get_alocation)


    def registration_parts(self):
        data_pats = request.form
        print(data_pats)

        required_fields = ['parts_name', 'parts_description', 'aircraft_id', 'price', 'supplier','quantity' ]
        
        for field in required_fields:
            if field not in data_pats or not data_pats[field]:
                return jsonify({'message': f'Required field cannot be empty: {field}'}), 400
        
        # Convertendo os campos para os tipos apropriados
        try:
            aircraft_id = int(data_pats['aircraft_id'])
            quantity = int(data_pats['quantity'])
            price = float(data_pats['price'])
        except (ValueError, TypeError) as e:
            field_name = str(e).split(":")[1].strip()
            return jsonify({'wrong fields': f"this field: {field_name} is type {type(data_pats[field_name])}, you passed an invalid value"}), 400
        
        # Continue com o processamento, uma vez que todos os campos obrigatórios estão presentes, não vazios e as conversões de tipo foram bem-sucedidas
        # ...

        return abort(make_response(jsonify(data_pats), 200))



