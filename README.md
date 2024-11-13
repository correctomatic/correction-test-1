# Correction test - 1

This is a container for testing the correction process for the correctomatic. It expects a single text file with this format:

```sh
ERROR_PROBABILITY=0.1
DELAY=2000
RESPONSE_SIZE=400
RESPONSE_TYPE=separator
```

It will return a success response after after ~`DELAY` milliseconds. The response will have a size of at least `RESPONSE_SIZE`. The container will return an error response with a probability of `ERROR_PROBABILITY`.

All the parameters are optional, it will take this as default:
```sh
ERROR_PROBABILITY=0.1
DELAY=2000
RESPONSE_SIZE=400
RESPONSE_TYPE=json
```

The container will return the output in the expected correctomatic format:

SuccessResponse:
```json
{
  sucess: true
  grade: XXXX,
  comments: [
    "DELAY: 2000",
    "ERROR_PROBABILITY: 0.1",
    "****....****"
  ]
}
```

FailedResponse:
```json
{
  success: false,
  error: "Error introduced with probability..."
}
```

It `RESPONSE_TYPE` is not `json` (i.e, `separator`), the json will be returned between the two separator lines that are defined in the correctomatic:
```
some garbage
here before the response
-----BEGIN CORRECTOMATIC RESPONSE-----
{"success": true, "grade": 100, "comments": ["DELAY: 2000", "ERROR_PROBABILITY: 0.1", "**********************************************************************************************************************************************************************************************************************************************************************************************************************"]}
-----END CORRECTOMATIC RESPONSE-----
more garbage here
```

The container also accepts `correctomatic_param_1` and `correctomatic_param_2` environment variable that will be included in the response as a new comment if they are set. For example:
```sh
```json
{
  sucess: true
  grade: XXXX,
  comments: [
    "DELAY: 2000",
    "ERROR_PROBABILITY: 0.1",
    "correctomatic_param_1: test-1",
    "correctomatic_param_2: test-2",
    "****....****"
  ]
}
```


## Build the image

You can build the image running `build.sh` or just using docker build command:
```sh
docker build --file ./Dockerfile --tag "correction-test-1" .
```

It will create an image with the tag `correction-test-1`.

## Test the container

You can launch the container witouth the correctomatic system. Just bind a file with the expected format:

```sh
docker run --rm \
  -v "`pwd`/exercise_example:/tmp/exercise" \
  -e "correctomatic_param_1=param1" \
  correction-test-1
```
