## Create user

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


## Signin user

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

