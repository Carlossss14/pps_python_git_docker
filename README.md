# pps_python_git_docker

#  Bayeta de la Fortuna – Python + Flask + Docker + MongoDB

# Ejercicio 8 local

1: Instalamos esta versión de Pyhton 
 sudo apt install python3.8-venv

2: Crear el entorno virtual:
 python3 -m venv venv

3: Ahora lo activamos
 source venv/bin/activate

4: Instalar dependencia
 pip install -r requirements.txt

5: Ejecutar la aplicación
 python3 app.py

6: La aplicación se encuentra
 http://127.0.0.1:5000/
 http://127.0.0.1:5000/frotar/3


# Despliegue con Docker

1:Crear red Docker
 sudo docker network create bayeta-net

2:Levantar MongoDB
 sudo docker run -d --name mongo-bayeta --network bayeta-net mongo

3: Construir la imagen de la API
 sudo docker build -t bayeta-fortuna:latest . 

4: Ejecutar la API conectada a MongoDB
 sudo docker run --rm -p 5000:5000 --network bayeta-net bayeta-fortuna

5: La API estará disponible en:
http://127.0.0.1:5000/

