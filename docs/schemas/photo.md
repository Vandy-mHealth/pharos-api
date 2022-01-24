field | `POST` Request | database |
:-:| :-: | :-:|
id | | auto integer (PK) !
url | string ! | string !
uploaded_at | datetime | auto datetime !
landmark_id | integer | integer (Landmark FK) !
owner_id | UUID | UUID (User FK) !
