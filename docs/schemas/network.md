field | `POST` Request | database |
:-:| :-: | :-:|
id |  | auto integer (PK)
ping_time | double ! | double !
frequency | double ! | double !
file_size | double !  | double !
file_location | string !| string !
download_speed | double ! | double !
download_latency | double ! | double !
download_duration | double ! | double !
upload_speed | double ! | double !
upload_duration | double ! | double !
gps_latitude | double ! | double !
gps_longitude | double ! | double !
device_id | integer ! | integer !
timestamp | datetime | auto datetime !
owner_id | UUID | UUID (User FK) !
landmark_id | integer  | integer (Landmark FK) !
