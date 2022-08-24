- Document status: **ACTIVE**
- Owner: Julian Franco

## Overview

This spec describes the API endpoint for adding a source of websites for a given user. i.e. ESPN, CNN, TESLA

### User story

As a content aggregator user, I want to add a new source in the database.

### UI usage

This API endpoint will be exposed to the frontend API to add a new source.

### Back end usage

## Endpoint details

### HTTP Request

Headers:

```http
POST /api/add_source
Content-Type: application/json
Cookie: <auth_cookie>
```

Query parameters:

- `user_id` (required) - Specify the user
- `source` (required) - The new source we want to add

### HTTP Response

#### `200`: Successful add source query

#### `401`: This will be returned if the Auth0 token authentication fails.
