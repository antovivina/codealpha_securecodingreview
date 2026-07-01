# 🔐 Secure Coding Review Tool

## 📌 Overview

The Secure Coding Review Tool is a beginner-friendly cybersecurity project developed using Python, Flask, and HTML. It performs a basic static analysis of Python source code to identify common security vulnerabilities and displays the findings through a simple and interactive web interface.

Users can upload any Python (`.py`) file, and the application scans it for selected insecure coding practices, providing descriptions and remediation recommendations.


## ✨ Features

- Upload any Python (`.py`) file for analysis
- Detect common Python security vulnerabilities
- Display severity levels (Critical, High, Medium)
- Provide vulnerability descriptions
- Suggest remediation steps
- Simple and user-friendly web interface

## 🛡️ Vulnerabilities Detected

- Hardcoded Password
- Use of `eval()`
- Weak Exception Handling (`except:`)

 This tool performs basic pattern-based static analysis and is intended for learning and educational purposes.


## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Visual Studio Code

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Secure-Coding-Review-Tool.git
```

### 2. Navigate to the project folder

```bash
codealpha_secure_coding_review
```

### 3. Install the required package

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

### 6. Upload a Python (.py) file and click "Analyze".

---

## 📸 Project Screenshots

### Home Page

*<img width="1907" height="556" alt="image" src="https://github.com/user-attachments/assets/9c224621-d297-4cd9-aa09-bb3ba80edd31" />


### Security Report

<img width="1831" height="795" alt="image" src="https://github.com/user-attachments/assets/27dace16-898b-4b36-a06b-5badea6b1d87" />
<img width="1870" height="560" alt="image" src="https://github.com/user-attachments/assets/f4018744-15df-4e80-8163-9d4f912eaf4c" />


## 📄 Sample File

A sample vulnerable Python file (`sample.py`) is included in this repository to demonstrate the functionality of the tool.

## 🔒 Remediation Suggestions

The application provides recommendations for each detected vulnerability, such as:

- Avoid storing passwords directly in source code.
- Replace `eval()` with safer alternatives.
- Catch specific exceptions instead of using generic `except:`.
- Follow secure coding best practices.

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Secure Coding Review
- Basic Static Code Analysis
- Python Security Concepts
- Flask Web Development
- HTML & CSS Integration
- Secure Coding Best Practices

## 🚀 Future Enhancements

- Detect additional Python security vulnerabilities
- Generate downloadable security reports
- Add a security score
- Improve vulnerability classification
- Support multiple programming languages

---

## 👩‍💻 Author

Anto Vivina

Computer Science Engineering (Cyber Security)

Aspiring Cybersecurity Professional | Python Learner | Passionate about Secure Coding
