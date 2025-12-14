from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# ---------- DATABASE ----------
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

# ---------- SQL INJECTION (VULNERABLE) ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        conn = get_db()
        query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
        result = conn.execute(query).fetchone()
        conn.close()

        if result:
            return "✅ Login Successful (SQLi Vulnerable)"
        else:
            return "❌ Login Failed"

    return render_template("login.html")

# ---------- XSS (VULNERABLE) ----------
@app.route("/search")
def search():
    query = request.args.get("q")
    return render_template("search.html", query=query)

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
