from flask import Flask, request, jsonify
import sqlite3
 
app = Flask(__name__)
 
DATABASE = "database.db"
 
# -------------------------
# Database helper
# -------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
 
# -------------------------
# Create table
# -------------------------
# @app.before_first_request
def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
 
with app.app_context():
    create_table()

# -------------------------
# CREATE (POST)
# -------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    conn = get_db()
    conn.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "User created"}), 201
 
# -------------------------
# READ (GET all)
# -------------------------
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])
 
# -------------------------
# READ (GET one)
# -------------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    conn.close()
 
    if user is None:
        return jsonify({"error": "User not found"}), 404
 
    return jsonify(dict(user))
 
# -------------------------
# UPDATE (PUT)
# -------------------------
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    conn = get_db()
    conn.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (data["name"], data["email"], user_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated"})
 
# -------------------------
# DELETE (DELETE)
# -------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted"})
 
# -------------------------
# Run app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)