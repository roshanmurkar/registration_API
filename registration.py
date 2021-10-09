
from flask import Flask, request, jsonify

from database_query import DBQuery

db_query = DBQuery
app = Flask(__name__)

class EmptyData(Exception):...
    #raise when user data is empty


@app.route('/details',methods=['GET'])
def get_details():
    """
    this function display all the users username and password
    :return: json file of all details
    """
    output = db_query.select_all()
    return jsonify(output)

@app.route('/registration',methods=['POST'])
def new_user():
    """
    this function create new registration of new user
    :return: response of registration process
    """
    user_data = request.get_json()
    try:
        if len(user_data['name']) == 0:
            raise EmptyData
        output = db_query.select_all()
        for user in output:
            if user[0] == user_data['name'] and user[1] == user_data['password']:
                return jsonify({"response": "user is already registered"},user_data)
        db_query.insert_data(user_data['name'], user_data['password'])
        if True:
            return jsonify({"response": "registration is successful"},user_data)
    except EmptyData:
        return jsonify({"response":"Empty data is not allowed"},user_data)
    except Exception:
        return jsonify({"response":"different exception faced"},user_data)


@app.route('/delete/registration',methods=['POST'])
def delete_user():
    """
    this function delete existing user from database
    :return: response of delete process
    """
    user_data = request.get_json()
    output = db_query.select_all()
    for user in output:
        if user[0]==user_data['name'] and user[1]==user_data['password']:
            db_query.delete_data(user_data['name'])
            if True:
                return jsonify({"message": "Deleted successful"},user_data)
    return jsonify({'response': "No user found"},user_data)

@app.route('/login',methods=['POST'])
def user_login():
    """
    This function will check user name and password with entries present in database
    :return: response of login process
    """
    user_data = request.get_json()
    output = db_query.select_all()
    for user in output:
        if user[0]==user_data['name'] and user[1]==user_data['password']:
            return jsonify({"message": "User login successful"},user_data)
    return jsonify({'response': "Invalid data"},user_data)

if __name__ == '__main__':
    app.run(debug=True)



