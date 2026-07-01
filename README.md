# TPI_AySO - Trabajo Práctico de Virtualización y Scripting

**Alumnos:** Pablo Iván Bárcena  
**Materia:** Arquitectura y sistemas operativos
**Enlace a video:** https://www.youtube.com/watch?v=TzJl33h3yZc

---

### Contenido

- **`/programa/conversor_de_numeros.py`**  
  Programa en Python que convierte números decimales a binario, octal y hexadecimal.

- **`/scripts/guardar.sh`**  
  Script en Bash que ejecuta el programa Python, muestra su salida en pantalla y la guarda en un archivo de texto con fecha y hora.

- **`Informe TPI.pdf`**  
  Informe completo del trabajo práctico, con introducción, marco teórico, caso práctico, resultados y conclusiones.

---

##  Cómo ejecutar el script

1. **Asegurarse de que el programa Python esté en la ruta correcta:**  
   El script `guardar.sh` espera encontrar el archivo `conversor_de_numeros.py` en la carpeta `programa/`.

2. **Dar permisos de ejecución al script:**  
   ```bash
   chmod +x scripts/guardar.sh
Ejecutar el script desde la terminal:

bash
./scripts/guardar.sh
Interactuar con el programa:

Elegir una opción del 1 al 3 para convertir.

Ingresar un número entero positivo.

Elegir la opción 4 para salir.

Resultado:
Al finalizar, se generará un archivo en la misma carpeta con el nombre resultado_YYYY-MM-DD_HH-MM-SS.txt, conteniendo todo el registro de la sesión.

Requisitos
Python 3 (para ejecutar el programa).

Bash (para ejecutar el script).

VirtualBox (para el entorno virtualizado, opcional).

Nota
Este trabajo fue desarrollado y probado en un entorno Linux Mint dentro de una máquina virtual con VirtualBox, utilizando una carpeta compartida entre el host (Windows) y el invitado (Linux) para la transferencia de archivos.

