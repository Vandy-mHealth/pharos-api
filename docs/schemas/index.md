
There are two types of schema involved in Pharos API

- **request/schema**: controls the required input/output when submitting `GET` , `POST`, `PUT` requests

- **database schema**: controls the data is actually stored inside the database

For example, a user entity has the following schema

field | `POST` Request | database |
:-:| :-: | :-:|
id     |  | auto UUID (PK) !
email | email-like string ! | string !
pin | big integer ! (6 digits) | big integer !
full_name | string ! | string !
created_at | datetime | datetime
organization | string | string
address | string | string

`field` indicates both the request json key and database column name.

The second column is the `request/response` schema. A field marked with `!` means it is required during creation

The third column is the `database` schema. A field marked with `!` means it cannot be null in the database.

In summary, the required request to create a user looks like


```js
axios.post(url, {
  "email": "user@example.com",
  "pin": 123456,
  "full_name": "jane doe"
})
```

and the returned response (from the database) will be


```json
{
  "email": "user@example.com",
  "pin": 123456,
  "full_name": "jane doe",
  "id": "c301644d-7a4f-4294-adcf-6646d2735202",
  "created_at": "2022-01-24T12:35:47.554672",
  "organization": null,
  "address": null,
  "landmarks": [],
  "photos": [],
  "network_measurements": []
}
```