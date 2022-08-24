- Document status: **ACTIVE**
- Owner: Julian Franco

## Overview

This spec describes the API endpoint for getting feeds given a given user, source and section. i.e. Julian, nytimes.com, Technology 

### User story

As a content aggregator user, I want to get feeds by user, source and section.

### UI usage

This API endpoint will be exposed to the frontend API to get feeds.

### Back end usage

## Endpoint details

### HTTP Request

Headers:

```http
GET /api/get_feeds
Content-Type: application/json
Cookie: <auth_cookie>
```

Query parameters:

- `user_id` (required) - Specify the user
- `source` (required) - The source we want to get
- `section` (required) - The section we want to get

### HTTP Response

#### `200`: Successful add source query

#### `401`: This will be returned if the Auth0 token authentication fails.
