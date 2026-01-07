---
type: note
status: done
tags: ['tech/backend']
sources:
- "[[Backend Basics Course]]"
authors:
-
---

**Codewords:** Client, Server, Client-Server Model, HTTP/S, Request, Response, Status Codes, API, REST, JSON.

## 1. How the Internet works

When you open a browser and go to a website like `google.com`, your computer (the **client**) sends a request over the internet to one of Google's computers (the **server**). The server then processes this request and sends back a response, which contains the webpage content that your browser displays. This interaction is known as the **Client-Server Model**.

It's the fundamental architecture of the web.

This communication happens using a set of rules, or a protocol, called **HTTP** (HyperText Transfer Protocol), or its secure version **HTTPS**.

### HTTP Requests and Responses

Think of HTTP as the language clients and servers use to talk to each other.

An **HTTP Request** sent by a client has a few key parts:

The server sends back an **HTTP Response**:

## 2. What is an API?

An **API (Application Programming Interface)** is a set of rules and tools that allows different software applications to communicate with each other. It's like a menu in a restaurant. The menu provides a list of dishes you can order, along with a description of each dish. You (the client) don't need to know how the kitchen (the server) prepares the food. You just need to place an order from the menu.

**REST (Representational State Transfer)** is a popular architectural style for designing APIs. RESTful APIs use standard HTTP methods (`GET`, `POST`, etc.) to work with resources.

### Working with APIs in Python
 
Python's `requests` library is a simple and popular way to interact with APIs. You might need to install it first:

```bash
pip install requests
```

Let's get some data from a public API. We'll use the JSONPlaceholder API, which provides fake data for testing.

```python
import requests

# 1. We chose the Cat Facts API
# 2. Make a GET request
response = requests.get("https://cat-fact.herokuapp.com/facts")

# 3. Check status and print
if response.status_code == 200:
 facts = response.json()
 # 4. Print the first fact's text
 if facts:
 print("A random cat fact:")
 print(facts[0]['text'])
else:
 print(f"Error: {response.status_code}")
```

### What is JSON?
**JSON (JavaScript Object Notation)** is a lightweight format for storing and transporting data. It's easy for humans to read and write and easy for machines to parse and generate. When you get data from an API, it's very often in JSON format. Python dictionaries and lists map directly to JSON objects and arrays, which makes working with JSON in Python very intuitive.

**Practice Problem: Public APIs**

1. Find a public API from [this list](https://github.com/public-apis/public-apis) that doesn't require authentication.
2. Write a Python script using the `requests` library to make a `GET` request to one of its endpoints.
3. Check the status code of the response. If it's successful, print the first item from the list of results you get back.
4. Modify your script to fetch data about a specific resource if the API supports it (e.g., using an ID in the URL like `.../posts/5`).

---

**Key Questions:**

1. What is the client-server model?
?
- It's the fundamental architecture of the web where a **client** (like your browser) requests information or services from a **server**, which stores data and provides those services.

2. What are the four most common HTTP methods and what are they used for?
?
- **GET:** To retrieve data.
- **POST:** To create new data.
- **PUT:** To update existing data.
- **DELETE:** To remove data.

3. What's the difference between a 2xx, 4xx, and 5xx HTTP status code?
?
- **2xx:** The request was successful.
- **4xx:** There was an error on the client's side (e.g., requesting a non-existent page).
- **5xx:** There was an error on the server's side.

4. What is an API?
?
- An API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information.

5. What is JSON and why is it commonly used with APIs?
?
- JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format. It's popular for APIs because it's easy for humans to read and for machines to parse, and it maps well to data structures in most programming languages (like dictionaries and lists in Python). 