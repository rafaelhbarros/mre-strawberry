#### Django things

python manage.py migrate
python manage.py createsuperuser

Go to admin and add recording

#### Query:

```
mutation recording($input: SetRecordingInput!) {
  createRecordingStreamingInfo(input: $input) {
    expirationDate
    isExpired
    isError
    recordingStreamingUrl
  }
}
```

#### Input:

```
{
  "input": {
    "RecordId": "83b1eb06-1245-4953-b679-b79dab709c64"
  }
}
```

#### Running:

daphne -b 0.0.0.0 -p 8000 mre.asgi:application


