## Create network measurements

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

# Read network measurements

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