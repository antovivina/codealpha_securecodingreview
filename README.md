# Secure Coding Review - Python Login Application

## Objective

This project demonstrates a secure coding review of a simple Python login application. The goal is to identify security vulnerabilities, assess their risks, and provide remediation recommendations.

## Application Reviewed

A basic Python login system containing intentionally vulnerable code.

## Review Method

Manual Code Inspection

## Vulnerabilities Identified

### 1. Hardcoded Credentials

**Severity:** High

**Description:**
The username and password are directly stored in the source code.

**Risk:**
Attackers who gain access to the code can view credentials.

**Recommendation:**
Store credentials securely using environment variables or a database.

### 2. SQL Injection

**Severity:** High

**Description:**
User input is directly concatenated into an SQL query.

**Risk:**
An attacker may manipulate database queries and gain unauthorized access.

**Recommendation:**
Use parameterized queries.

### 3. Lack of Input Validation

**Severity:** Medium

**Description:**
User input is accepted without validation.

**Risk:**
Unexpected or malicious input may affect application behavior.

**Recommendation:**
Validate and sanitize all user inputs.

## Conclusion

The code review identified multiple security vulnerabilities including hardcoded credentials, SQL injection, and insufficient input validation. Implementing secure coding practices would significantly improve the security of the application.
