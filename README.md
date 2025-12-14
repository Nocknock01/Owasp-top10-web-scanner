# OWASP Top 10 Web Scanner (Python + Flask)

A **beginner-friendly, hands-on cybersecurity project** that demonstrates common **OWASP Top 10 web application vulnerabilities** using a vulnerable Flask application. This project is built for **learning, practice, and GitHub portfolio showcase**.

> ⚠️ **Disclaimer:** This project is strictly for **educational purposes only**. Do NOT test these techniques on real or unauthorized systems.

---

## 🚀 Features

* Vulnerable Flask web application
* Demonstrates real-world OWASP Top 10 issues
* Easy to run on Windows using VS Code
* Ideal for **cybersecurity students & interns**

---

## 🔍 Vulnerabilities Demonstrated

* **SQL Injection (SQLi)** – Authentication bypass
* **Cross-Site Scripting (XSS)** – Reflected XSS
* **Broken Authentication** – Weak login logic
* **Security Misconfiguration** – Debug mode enabled

Each vulnerability can be tested manually via browser inputs.

---

## 🛠 Tech Stack

* **Language:** Python 3
* **Framework:** Flask
* **Environment:** Virtualenv (.venv)
* **OS Tested:** Windows

---

 📁 Project Structure

owasp-top10-web-scanner/
│
├── app.py               # Vulnerable Flask application
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates (if added)
├── .gitignore
└── README.md


## ⚙️ Setup & Run (Windows)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Nocknock01/Owasp-top10-web-scanner.git
cd Owasp-top10-web-scanner
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Sample Tests

### 🔴 SQL Injection Test

Input in login fields:

```
' OR '1'='1
```

➡ Authentication bypass (vulnerable behavior)

---

### 🔴 XSS Test

```
<script>alert(1)</script>
```

➡ JavaScript executes in browser

---

## 🛡️ Learning Outcomes

* Understand OWASP Top 10 vulnerabilities
* Learn how attackers exploit web apps
* Practice secure coding awareness
* Improve penetration testing fundamentals

---

## 📌 Future Improvements

* Add secure (fixed) implementation
* Add database-backed authentication
* Add PoC documentation
* Add screenshots & demo videos

---

## 👨‍💻 Author

Srujan M V
B.Tech – Cyber Security & Cyber Forensics

---

⭐ If this project helped you, consider starring the repository!


