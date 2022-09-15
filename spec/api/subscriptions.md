- Document status: **ACTIVE**
- Owner: Julian Franco

## Overview

This spec describes the API endpoint for adding a source of websites for a given user. i.e. ESPN, CNN, TESLA

### User story

As a content aggregator user, I want to add a new source to my subscription list.

### UI usage

This API endpoint will be exposed to the frontend API to add a new source.

## Endpoint details

### HTTP Request

Headers:

```http
POST /api/subscriptions
Content-Type: application/json
Cookie: <auth_cookie>
```

Body parameters:

```json
{
  "user_id": "string",
  "source_id": "string",
  "section_id": "string"
}
```

- `user_id`: `String` (required) - The user id associated with the user who wants to add the new source. i.e. John
- `source_id`: `String` (required) - The new source, or in other words, the domain name we want to add. i.e. nytimes.com
- `section_id`: `String` (required) - The new section, or in other words, the path name we want to add. i.e. technology

### HTTP Response

#### `200`: Successful source set up

Request successfully processed, and a new source was created.

The `data` field returns the following object:

```json
{
  "data": {
    "user_id": "string", 
    "source_id": "string", 
    "section_id": "string"
  },
  "articles": [
    {
      "title": "string", 
      "content": "string", 
      "metadata": "json"
    }
  ],
  "errors": []
}
```

#### `400`: The format of the request is not valid

This error has to do with the following:

- The HTTP request headers are wrong
- The json data is missing or cannot be parsed
- The json data is missing required fields

The response contains an `errors` array of error objects.

```json
{
  "errors": []
}
```

#### `401`: This will be returned if the Auth0 token authentication fails.

Returned if the authentication fails

### `422`: Endpoint-specific errors

#### `endpoint/user_not_found`

This error occurs when the `user_id` field in the request does not map to an existing user

```json
{
  "code": "endpoint/user_not_found",
  "data": { "user_id": "{user_id}" },
  "message": "User not found."
}
``` 

#### `endpoint/duplicate_combination`

This error occurs when the combination user-source already exists in the database

```json
{
  "code": "endpoint/duplicate_combination",
  "data": { "user_id": "{user_id}", "source_id": "{source_id}", "section_id": "{section_id}" },
  "message": "Combination of user id and source already submitted to the database"
}
```



