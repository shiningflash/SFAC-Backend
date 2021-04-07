# SFAC-Backend


## Change Password API

```
PUT {{domain_url}}/api/account/change-password
```

```
curl --request PUT \
  --url http://localhost:8000/api/account/change-password \
  --header 'Authorization: Token d94ffca2c287885ca57c7265552019d6d01c25f31' \
  --header 'Content-Type: application/json' \
  --data '{
    "old_password": "dhfj766#@FGfsa",
    "new_password": "FRY5^^%75@@hgs"
}'
```

**Request**
```
{
    "old_password": "dhfj766#@FGfsa",
    "new_password": "FRY5^^%75@@hgs"
}
```
**Response**
```
"Password updated successfully"
```

## Reset Password Request API

```
POST {{domain_url}}/api/password_reset/
```

```
curl --request POST \
  --url http://localhost:8000/api/password_reset/ \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "yourname@g.bracu.ac.bd"
}'
```

A secret token will sent to your mail.

**Request**
```
{
	"email": "yourname@g.bracu.ac.bd"
}
```
**Response**
```
{
  "status": "OK"
}
```

## Reset Password Confirm API

```
POST {{domain_url}}/api/password_reset/confirm/
```

```
curl --request POST \
  --url http://localhost:8000/api/password_reset/confirm/ \
  --header 'Authorization: Token d94ffca2c287885ca555526f9b019d6d01c25f31' \
  --header 'Content-Type: application/json' \
  --data '{
    "token":"4fae77cc94a4c76cf87541165555de57575fe15eeba5d4b",
    "password":"HG565%@@#fsgQW"
}'
```

Use the `secret token` that sent to your mail.

**Request**
```
{
    "token":"your token that sent to your mail",
    "password":"your new password"
}

```
**Response**
1. for wrong token
```
{
  "status": "notfound"
}
```
2. for same or similar password as previous
```
{
  "password": [
    "The password is too similar to the last name."
  ]
}
```
3. correct token and new valid password
```
{
  "status": "OK"
}
```