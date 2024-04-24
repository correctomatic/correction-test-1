# Crear la imagen
./build.sh

# Lanzar
ERROR_PROBABILITY=<prob>
DELAY=<ms>
RESPONSE_SIZE=<bytes> (it doesn't truncate output, only adds bytes)

docker run --rm --mount type=bind,source=`pwd`/configuration,target=/tmp/exercise correction-test-1

docker container run -d --name mi_contenedor --mount type=bind,source="$(pwd)"/archivo.txt,target=/ruta/en/el/contenedor imagen_del_contenedor


docker run --rm -e DELAY=20 -e ERROR_PROBABILITY=0.5 -e RESPONSE_SIZE=400 correction-test-1

¿Cual es el formato que debería devolver el contenedor? JSON stringified

https://transform.tools/json-to-json-schema

SuccessResponse:
{
  sucess: true
  grade: XXXX,
  comments: [
    "...","..."
  ]
}

FailedResponse:
{
  success: false,
  error: ""
}





