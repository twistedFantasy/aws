## Amazon S3
1. Create new bucket with aws s3api
```
$ aws s3api create-bucket --bucket test-bucket --region us-east-1 --profile amazon-cli
{
    "Location": "/test-bucket"
}
```
2. Create `cors.json` file with next content:
```
{
  "CORSRules": [
    {
      "AllowedOrigins": ["*"],
      "AllowedMethods": ["HEAD", "GET"]
    },
    {
      "AllowedOrigins": ["http://reporting.test.com"],
      "AllowedMethods": ["PUT", "POST", "DELETE"]
    }
  ]
}
```
3. Update CORS configuration from `cors.json` file
```
$ aws s3api put-bucket-cors --bucket test-bucket --cors-configuration file://cors.json --profile amazon-cli
```

### Useful Resources
* [Amazon S3](https://aws.amazon.com/s3/)
* [Amazon CLI: S3](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
