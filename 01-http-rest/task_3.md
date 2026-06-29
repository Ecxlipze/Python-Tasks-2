# Task 3 - Inspecting a Public REST API

## Objective
To understand how different HTTP methods work by testing a public REST API using Postman.

## Public API Used
```
https://jsonplaceholder.typicode.com/posts
```
Tool Used
* Postman

## 1. GET Request

### Method
```
GET
```
### Endpoint
```
/posts
```
### Request Body
None
### Response Status
```
200 OK
```
### Response Format
JSON Array
### Observation

* Retrieved all posts from the server.
* No request body was required.
* The server returned a successful response in JSON format.

## 2. POST Request

### Method
```
POST
```
### Endpoint
```
/posts
```
### Request Body

```json
{
    "title": "Learning Django",
    "body": "My first POST request",
    "userId": 1
}
```
### Response Status
```
201 Created
```
### Response Format

```json
{
    "title": "Learning Django",
    "body": "My first POST request",
    "userId": 1,
    "id": 101
}
```
### Observation

* A new resource was created.
* The server returned the created object with a generated ID.
* POST is used to create new resources.

## 3. PUT Request

### Method
```
PUT
```
### Endpoint
```
/posts/1
```
### Request Body
```json
{
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}
```
### Response Status
```
200 OK
```
### Observation

* The existing resource was completely replaced with the new data.
* PUT updates the entire resource.

## 4. PATCH Request

### Method
```
PATCH
```
### Endpoint
```
/posts/1
```
### Request Body

```json
{
    "title": "Only Title Changed"
}
```
### Response Status
```
200 OK
```
### Observation

* Only the specified field was updated.
* Other fields remained unchanged.
* PATCH is used for partial updates.

## 5. DELETE Request

### Method
```
DELETE
```
### Endpoint
```
/posts/1
```
### Request Body
None
### Response Status
```
200 OK
```
### Response Body
```
{}
```
### Observation

* The delete request was accepted successfully.
* JSONPlaceholder simulates deletion, so the resource is not permanently removed from the database.
