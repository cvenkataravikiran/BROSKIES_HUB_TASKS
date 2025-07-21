from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get("id")
    if not user_id or user_id in users:
        return jsonify({"error": "Invalid or duplicate user ID"}), 400

    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User created", "user": users[user_id]}), 201

# Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "email": data.get("email", users[user_id]["email"])
    })
    return jsonify({"message": "User updated", "user": users[user_id]})

# Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted_user})
    return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
