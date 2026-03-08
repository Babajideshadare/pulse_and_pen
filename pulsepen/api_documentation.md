## API Documentation
**Authentication**
The API uses Django REST Framework with:

Token Authentication
Session Authentication (for browser-based use)

**Default DRF settings:**
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

## To obtain an auth token:
POST /api/token/

## Request body:
{
  "username": "your-username",
  "password": "your-password"
}

## Response:
{
  "token": "your-api-token"
}

## Use the token:
Authorization: Token your-api-token

## BPEntry API
Endpoints:
GET /api/bp-entries/ – List the authenticated user’s BP entries
POST /api/bp-entries/ – Create a new BP entry
GET /api/bp-entries/<id>/ – Retrieve a single BP entry
PUT /api/bp-entries/<id>/ – Update an existing BP entry
PATCH /api/bp-entries/<id>/ – Partially update an existing BP entry
DELETE /api/bp-entries/<id>/ – Delete a BP entry

Example POST /api/bp-entries/ request body:

{
  "date": "2025-02-01",
  "time": "08:30:00",
  "systolic": 120,
  "diastolic": 80,
  "pulse": 70,
  "note": "Morning reading"
}


Example GET /api/bp-entries/ response:
[
  {
    "id": 1,
    "date": "2025-02-01",
    "time": "08:30:00",
    "systolic": 120,
    "diastolic": 80,
    "pulse": 70,
    "note": "Morning reading"
  }
]

## JournalEntry API
Endpoints:

GET /api/journal-entries/ – List the authenticated user’s journal entries
POST /api/journal-entries/ – Create a new journal entry
GET /api/journal-entries/<id>/ – Retrieve a journal entry
PUT /api/journal-entries/<id>/ – Update a journal entry
PATCH /api/journal-entries/<id>/ – Partially update a journal entry
DELETE /api/journal-entries/<id>/ – Delete a journal entry

Example POST /api/journal-entries/ request body:
{
  "date": "2025-02-01",
  "sleep_hours": 7.5,
  "sleep_quality": "Good",
  "exercise_type": "Walking",
  "exercise_duration": 30,
  "diet_notes": "Light dinner, no late snacks",
  "mood_stress_level": "Calm"
}
Example GET /api/journal-entries/ response:
[
  {
    "id": 1,
    "date": "2025-02-01",
    "sleep_hours": 7.5,
    "sleep_quality": "Good",
    "exercise_type": "Walking",
    "exercise_duration": 30,
    "diet_notes": "Light dinner, no late snacks",
    "mood_stress_level": "Calm"
  }
]