# Routes

## User

create user

```
POST /user/create
```

sign in user

```
POST /user/signin
```

## Landmark

create landmark for user

```
POST /landmark/?user_id=<user_id>
```

read landmarks for user

```
GET /landmark?user_id=<user_id>
```

read all landmarks

```
GET /landmark
```

## Network Measurements

create network measurements for user and landmark id

```
POST /network/?user_id=<user_id>&landmark_id=<landmark_id>
```

read network measurements for user

```
GET /network?user_id=<user_id>
```

read all landmarks

```
GET /network
```

## Photo

create photo for user and landmark id

```
POST /photo/?user_id=<user_id>&landmark_id=<landmark_id>
```

read photos for user

```
GET /photo?user_id=<user_id>
```

read all photos

```
GET /photo
```
