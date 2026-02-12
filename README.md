# pps_python_git_docker

# Bayeta de la Fortuna – Python + Flask + Docker

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


# Con Docker contenedor

1:Construir la imagen
 docker build -t bayeta-fortuna:latest .

2:Corre este comando
 sudo docker build -t bayeta-fortuna:latest .

3: Corre este comando
 sudo docker run --rm -p 5000:5000 bayeta-fortuna:latest

4: La aplicación estará disponible en:
  http://127.0.0.1:5000/
  http://127.0.0.1:5000/frotar/3
