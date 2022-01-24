# Routes

## create user

```
POST /user/create
```

example request

```js
axios.post(url, {
  "email": "user@example.com",
  "pin": 123456,
  "full_name": "jane doe"
})
```

example response

```json
{
  "email": "user@example.com",
  "pin": 123456,
  "full_name": "jane doe",
  "id": "c301644d-7a4f-4294-adcf-6646d2735202",
  "last_login": "2022-01-24T12:35:47.554672",
  "organization": null,
  "address": null,
  "landmarks": [],
  "photos": [],
  "network_measurements": []
}
```


## signin user

```
POST user/signin
```
example request

```js
axios.post(url, {
  "email": "user@example.com",
  "pin": 123456
})
```

example response

```json
{
  "email": "user@example.com",
  "pin": 123456,
  "full_name": "jane doe",
  "id": "c301644d-7a4f-4294-adcf-6646d2735202",
  "last_login": "2022-01-24T12:35:47.554672",
  "organization": null,
  "address": null,
  "landmarks": [],
  "photos": [],
  "network_measurements": []
}
```

example response when email doesn't exist

```json
// status_code = 400
{
  "detail": "Email not found"
}
```

example response when pin is wrong

```json
// status_code = 400
{
  "detail": "Wrong pin number"
}
```



## create landmark with network measurements and photos

```
POST /landmark/create?user_id=<user_id>
```

```js
axios.post(url, {
  "landmark": {
    "latitude": 0,
    "longitude": 0,
    "landmark_type": "string",
    "device_id": 0,
    "file_url": "string"
  },
  "network": {
    "ping_time": 0,
    "frequency": 0,
    "file_size": 0,
    "file_location": "string",
    "download_speed": 0,
    "download_latency": 0,
    "download_duration": 0,
    "upload_speed": 0,
    "upload_duration": 0,
    "gps_latitude": 0,
    "gps_longitude": 0,
    "device_id": 0
  },
  "photo": {
    "url": "string"
  }
})
```

example response

```json
{
  "latitude": 0,
  "longitude": 0,
  "landmark_type": "string",
  "device_id": 0,
  "file_url": "string",
  "id": 2,
  "timestamp": "2022-01-24T13:25:23.286296",
  "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202",
  "network_measurements": [
    {
      "ping_time": 0,
      "frequency": 0,
      "file_size": 0,
      "file_location": "string",
      "download_speed": 0,
      "download_latency": 0,
      "download_duration": 0,
      "upload_speed": 0,
      "upload_duration": 0,
      "gps_latitude": 0,
      "gps_longitude": 0,
      "device_id": 0,
      "id": 2,
      "timestamp": "2022-01-24T13:25:23.286967",
      "landmark_id": 2,
      "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
    }
  ],
  "photos": [
    {
      "url": "string",
      "id": 2,
      "uploaded_at": "2022-01-24T13:25:23.287614",
      "landmark_id": 2,
      "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
    }
  ]
}
```

example response when user id does not exist

```json
{
  "detail": "User not found"
}
```


## read all landmarks or for user

read all landmarks

```
GET /landmark
```


```js
axios.get(url)

// returns
[
  {
    "latitude": 0,
    "longitude": 0,
    "landmark_type": "string",
    "device_id": 0,
    "file_url": "string",
    "id": 1,
    "timestamp": "2022-01-24T13:24:43.930960",
    "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202",
    "network_measurements": [
      {
        "ping_time": 0,
        "frequency": 0,
        "file_size": 0,
        "file_location": "string",
        "download_speed": 0,
        "download_latency": 0,
        "download_duration": 0,
        "upload_speed": 0,
        "upload_duration": 0,
        "gps_latitude": 0,
        "gps_longitude": 0,
        "device_id": 0,
        "id": 1,
        "timestamp": "2022-01-24T13:24:43.931900",
        "landmark_id": 1,
        "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
      }
    ],
    "photos": [
      {
        "url": "string",
        "id": 1,
        "uploaded_at": "2022-01-24T13:24:43.932665",
        "landmark_id": 1,
        "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
      }
    ]
  },
  ...
]
```


get landmarks uploaded by a specific user

```
GET /landmark/?user_id=<user_id>
```



## create network measurements

create network measurements for a user and a landmark

```
POST /network/create/?user_id=<user_id>&landmark_id=<landmark_id>
```

example request

```js
axios.post(url, {
  "ping_time": 0,
  "frequency": 0,
  "file_size": 0,
  "file_location": "string",
  "download_speed": 0,
  "download_latency": 0,
  "download_duration": 0,
  "upload_speed": 0,
  "upload_duration": 0,
  "gps_latitude": 0,
  "gps_longitude": 0,
  "device_id": 0
})
```

example response

```json
{
  "ping_time": 0,
  "frequency": 0,
  "file_size": 0,
  "file_location": "string",
  "download_speed": 0,
  "download_latency": 0,
  "download_duration": 0,
  "upload_speed": 0,
  "upload_duration": 0,
  "gps_latitude": 0,
  "gps_longitude": 0,
  "device_id": 0,
  "id": 3,
  "timestamp": "2022-01-24T13:36:43.903816",
  "landmark_id": 2,
  "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
}

```

error when user does not exist

```json
{
  "detail": "User not found"
}
```

error when landmark does not exist

```json
{
  "detail": "Landmark not found"
}
```

## read all network measurements or for a user

read all network measurements

```
GET /network
```

```json
[
  {
    "ping_time": 0,
    "frequency": 0,
    "file_size": 0,
    "file_location": "string",
    "download_speed": 0,
    "download_latency": 0,
    "download_duration": 0,
    "upload_speed": 0,
    "upload_duration": 0,
    "gps_latitude": 0,
    "gps_longitude": 0,
    "device_id": 0,
    "id": 1,
    "timestamp": "2022-01-24T13:24:43.931900",
    "landmark_id": 1,
    "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
  },
  {
    "ping_time": 0,
    "frequency": 0,
    "file_size": 0,
    "file_location": "string",
    "download_speed": 0,
    "download_latency": 0,
    "download_duration": 0,
    "upload_speed": 0,
    "upload_duration": 0,
    "gps_latitude": 0,
    "gps_longitude": 0,
    "device_id": 0,
    "id": 2,
    "timestamp": "2022-01-24T13:25:23.286967",
    "landmark_id": 2,
    "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
  },
  ...
]
```

read all network measurements for a specific user

```
GET /network/?user_id=<user_id>
```

## create photos for user and landmark

```
POST /photo/?user_id=<user_id>
```

example request

```js
axios.get(url, {
  "url": "string"
})
```

example response

```json
{
  "url": "string",
  "id": 3,
  "uploaded_at": "2022-01-24T13:45:29.477201",
  "landmark_id": 2,
  "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
}
```

error when user does not exist

```json
{
  "detail": "User not found"
}
```

error when landmark does not exist

```json
{
  "detail": "Landmark not found"
}
```


# Schemas

`!` means the field is required during creation, fields without `!` can be added later via `PUT` request or automatically generated (like `UUID`)

## User

field | `POST` Request | database |
:-:| :-: | :-:|
id     | UUID | auto UUID (PK)
email | email-like string ! | string
pin | big integer ! (6 digits) | big integer
full_name | string ! | string
last_login | datetime | datetime
organization | string | string
address | string | string

## Landmark

field | `POST` Request | database |
:-:| :-: | :-:|
id | integer | auto integer (PK)
latitude | double ! | double
longitude | double ! | double
landmark_type | string ! | string
device_id | integer ! | integer
file_url | string ! | string
timestamp | datetime | auto datetime
owner_id | UUID | UUID (User FK)

## Network

field | `POST` Request | database |
:-:| :-: | :-:|
id | integer | auto integer (PK)
ping_time | double ! | double !
frequency | double ! | double
file_size | double !  | double
file_location | string !| string
download_speed | double ! | double
download_latency | double ! | double
download_duration | double ! | double
upload_speed | double ! | double
upload_duration | double ! | double
gps_latitude | double ! | double
gps_longitude | double ! | double
device_id | integer ! | integer
timestamp | datetime | auto datetime
owner_id | UUID | UUID (User FK)
landmark_id | integer  | integer (Landmark FK)

## Photo

field | `POST` Request | database |
:-:| :-: | :-:|
id | integer | auto integer (PK)
url | string ! | string
uploaded_at | datetime | auto datetime
landmark_id | integer | integer (Landmark FK)
owner_id | UUID | UUID (User FK)



