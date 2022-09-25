- Document status: **ACTIVE**
- Owner: Julian Franco

## Overview

This spec describes the API endpoint for getting feeds given a given user, source and section. i.e. Julian, nytimes.com, Technology 

### User story

As a content aggregator user, I want to get feeds by user, source and section.

### UI usage

This API endpoint will be exposed to the frontend API to get feeds.

## Endpoint details

### HTTP Request

Headers:

```http
GET /api/get_feeds/user/:user_id/source/:source_id/section/:section_id
Content-Type: application/json
Cookie: <auth_cookie>
```

Query parameters:

- `user_id`: `String` (required) - The user id associated with the user who wants to add the new source. i.e. John
- `source_id`: `String` (required) - The new source, or in other words, the id of the domain name we want to add. Example of a source is nytimes.com
- `section_id`: `String` (required) - The section id we want to get from the source. Example of a section is technology. Therefore, source + section will result in nytimes.com/technology

### HTTP Response

#### `200`: Successful get feed query

```json
{
  "data": {
    "user_id": "user123",
    "source_id": "source123",
    "section_id": "section123", 
    "articles": [
      {
        "title": "title", 
        "content": "content", 
        "metadata": {}
      }
    ]
  },
  "metadata": {},
  "errors": []
}
```

#### `401`

Returned if the Auth0 token authentication fails.

#### `404` 

Feeds not found for this specific user

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

#### `endpoint/source_not_found`

This error occurs when the `source_id` field in the request does not map to an existing source

```json
{
  "code": "endpoint/source_not_found",
  "data": { "source_id": "{source_id}" },
  "message": "Source not found."
}
```  

#### `endpoint/section_not_found`

This error occurs when the `section_id` field in the request does not map to an existing section

```json
{
  "code": "endpoint/section_not_found",
  "data": { "section_id": "{section_id}" },
  "message": "Section not found."
}
``` 