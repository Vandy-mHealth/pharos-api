field | `POST` Request | database |
:-:| :-: | :-:|
id | | auto integer (PK) !
latitude | double ! | double !
longitude | double ! | double !
landmark_type | string ! | string !
device_id | integer ! | integer !
file_url | string ! | string !
timestamp | datetime | auto datetime
owner_id | UUID | UUID (User FK) !
