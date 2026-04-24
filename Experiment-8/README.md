# Experiment 9: Token Based Authentication using Flask

## Student Details

**Name:** Aaryan Singh
**Roll Number:** 23BCC70008
**Course:** Cloud Computing / Backend Experiment

---

## Objective

To implement token-based authentication using Python Flask APIs and test them using Postman.
The project demonstrates different authentication methods including Authorization Header, Custom Header, and JWT Bearer Token.

---

## Technologies Used

* Python
* Flask
* PyJWT
* Gunicorn
* Postman
* Render (for deployment)

---

## API Endpoints

### 1. Authorization Header Authentication

Endpoint:

```
/auth-header
```

Method:

```
GET
```

Description:
Authenticates a user using **Basic Authorization Header** (username and password).

---

### 2. Custom Header Authentication

Endpoint:

```
/custom-header
```

Method:

```
GET
```

Description:
Authenticates a user using custom headers:

```
X-Username
X-Password
```

---

### 3. JWT Login

Endpoint:

```
/login
```

Method:

```
POST
```

Request Body:

```
{
 "username": "admin",
 "password": "1234"
}
```

Description:
Generates a **JWT token** after successful login.

---

### 4. JWT Protected Route

Endpoint:

```
/jwt-protected
```

Method:

```
GET
```

Header:

```
Authorization: Bearer TOKEN
```

Description:
Access protected resources using a valid JWT token.

---

## Deployment

The application is deployed on **Render Cloud Platform**.

Demo URL:

```
https://exp-9-23bcc70008.onrender.com
```

---

## Testing

All APIs were tested using **Postman**.

---

## Conclusion

This experiment demonstrates the implementation of token-based authentication in a Flask backend application.
The APIs support different authentication mechanisms and are successfully deployed on Render.

---
