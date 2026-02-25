# password-strength-breach-checker
# 🔐 Password Strength & Breach Checker

A Python-based cybersecurity tool that analyzes password strength and checks whether a password has been exposed in known data breaches using the Have I Been Pwned API.

---

## 🚀 Features

✅ Password Strength Analysis  
- Checks length  
- Detects lowercase, uppercase, digits, symbols  
- Provides score (0–6)  
- Gives verdict: Weak / Medium / Strong / Very Strong  
- Provides improvement suggestions  

✅ Breach Detection (Online)  
- Uses SHA-1 hashing  
- Implements k-Anonymity model  
- Checks password against Have I Been Pwned database  
- Tells how many times the password appeared in breaches  

---

## 🛠 Technologies Used

- Python 3
- hashlib
- requests
- Have I Been Pwned API (Pwned Passwords)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/password-strength-breach-checker.git

Navigate into the folder:

cd password-strength-breach-checker

Install required dependency:

pip install requests
▶️ How to Run
python filename.py

(Replace filename.py with your actual Python file name)

🔍 How It Works
Step 1: Strength Analysis

Evaluates password length

Checks character diversity

Assigns a score and verdict

Step 2: Breach Check

Converts password into SHA-1 hash

Sends only first 5 characters of hash to API (secure method)

Compares returned suffixes

Displays breach count if found

🛡 Security Note

The actual password is NEVER sent to the API.

Only a partial hash prefix is transmitted (k-anonymity model).

Safe and privacy-friendly implementation.

📸 Sample Output
Score: 5 / 6
Verdict: Strong
❌ WARNING: This password has appeared in 12,345 data breaches!
🎯 Project Purpose

This project demonstrates:

Cybersecurity awareness

API integration

Secure hashing

Real-world breach intelligence usage

Defensive security programming

📚 Future Improvements

Add GUI version

Add password entropy calculator

Export report to PDF

Add offline breach dataset support

Add colored terminal output

👨‍💻 Author

Madan Kumar Ray
B.Tech CSE-Cybersecurity

⭐ If you like this project

Give it a star ⭐ on GitHub!


---

# 📌 Extra (Optional but Recommended)

Add a `.gitignore` file:


pycache/
*.pyc
.env


---

If you want, I can also:

- 🔥 Make a professional GitHub description line
- 📄 Create a LinkedIn project description
- 🧠 Add this to your cybersecurity portfolio
- 🎓 Write a mini project report for submission

Tell me what you need next 👌
