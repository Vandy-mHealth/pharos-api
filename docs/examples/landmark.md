## Create landmark

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

if `network_measurements` or `photos` field is not provided, only the landmark will be created.

example response when user id does not exist

```json
{
  "detail": "User not found"
}
```

# Read landmarks

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

