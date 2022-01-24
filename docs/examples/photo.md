## Create photos for user and landmark

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


## Read photos

read photos for a specific user

```
GET /photo/?user_id=<user_id>
```

```javascript
axios.get(url)

// returns
[
    {
        "url": "string",
        "id": 3,
        "uploaded_at": "2022-01-24T13:45:29.477201",
        "landmark_id": 2,
        "owner_id": "c301644d-7a4f-4294-adcf-6646d2735202"
    }
    ...
]
```

read all photos

```
GET /photo
```