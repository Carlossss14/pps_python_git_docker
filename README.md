# pps_python_git_docker

# Ejercicio 12

# Despliegue con Docker que permite desplegar la API Flask y MongoDB con un solo comando.

1: Levantar la aplicación
 sudo docker-compose up --buil 

3: Ejemplo con curl
 curl -X POST http://127.0.0.1:5000/frotar/add \
     -H "Content-Type: application/json" \
     -d '{"frases": ["Nueva frase 1", "Nueva frase 2"]}'

3: Detener los contenedores
 sudo docker-compose down

4: Lo levantamos de nuevo
 sudo docker-compose up

5: La API estará disponible en:
 http://127.0.0.1:5000/
 http://127.0.0.1:5000/frotar/5

6: Detener los contenedores
 sudo docker-compose down
