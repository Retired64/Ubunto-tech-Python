Claro, aquí tienes otro ejemplo de un script utilizando `zenity` en Python para generar una entrada de texto y mostrarla en una ventana emergente:

```python
import subprocess

# Solicitar al usuario que ingrese un mensaje
entrada = subprocess.run(['zenity', '--entry', '--title=Ingrese un mensaje', '--text=Escribe tu mensaje:'], capture_output=True, text=True)

# Obtener el texto ingresado por el usuario
texto_ingresado = entrada.stdout.strip()

# Mostrar el texto en una ventana emergente
if texto_ingresado:
    subprocess.run(['zenity', '--info', '--text', f'El mensaje ingresado es:\n\n{texto_ingresado}', '--ok-label=Ok'])
else:
    subprocess.run(['zenity', '--error', '--text', 'No se ingresó ningún mensaje.', '--ok-label=Ok'])
```

Este script solicita al usuario que ingrese un mensaje en una ventana emergente y luego muestra el mensaje ingresado en otra ventana emergente. Si el usuario no ingresa ningún mensaje y presiona "Aceptar" sin ingresar texto, mostrará un mensaje de error.

Si necesitas más ejemplos o tienes alguna otra idea específica en mente para un script con `zenity`, estaré encantado de ayudarte a crearlo.

## EJEMPLO 2

Claro, aquí tienes un script que utiliza `zenity` para permitir al usuario seleccionar un archivo y luego muestra el nombre del archivo seleccionado en una ventana emergente:

```python
import subprocess

# Mostrar ventana para seleccionar un archivo
archivo_seleccionado = subprocess.run(['zenity', '--file-selection', '--title=Selecciona un archivo'], capture_output=True, text=True)

# Obtener la ruta del archivo seleccionado
ruta_archivo = archivo_seleccionado.stdout.strip()

# Extraer el nombre del archivo de la ruta
nombre_archivo = ruta_archivo.split('/')[-1] if ruta_archivo else None

# Mostrar el nombre del archivo en una ventana emergente
if nombre_archivo:
    subprocess.run(['zenity', '--info', '--text', f'Archivo seleccionado:\n\n{nombre_archivo}', '--ok-label=Ok'])
else:
    subprocess.run(['zenity', '--error', '--text', 'No se seleccionó ningún archivo.', '--ok-label=Ok'])
```

Este script muestra una ventana de selección de archivos usando `zenity`. Después de que el usuario selecciona un archivo, el script extrae el nombre del archivo de la ruta y lo muestra en una ventana emergente. Si el usuario cancela la selección, se mostrará un mensaje de error indicando que no se seleccionó ningún archivo.

### ejemplo 3

Claro, aquí tienes un ejemplo de un script que utiliza `zenity` para mostrar un diálogo de selección de color y luego muestra el color seleccionado en una ventana emergente:

```python
import subprocess

# Mostrar diálogo de selección de color
color_seleccionado = subprocess.run(['zenity', '--color-selection', '--title=Selecciona un color'], capture_output=True, text=True)

# Obtener el color hexadecimal seleccionado
color_hex = color_seleccionado.stdout.strip()

# Mostrar el color seleccionado en una ventana emergente
if color_hex:
    subprocess.run(['zenity', '--info', '--text', f'Color seleccionado:\n\n{color_hex}', '--ok-label=Ok'])
else:
    subprocess.run(['zenity', '--error', '--text', 'No se seleccionó ningún color.', '--ok-label=Ok'])
```

Este script abre un diálogo de selección de color utilizando `zenity`. Después de que el usuario elige un color, el script muestra el color seleccionado en formato hexadecimal en una ventana emergente. Si el usuario cancela la selección, se muestra un mensaje de error indicando que no se seleccionó ningún color.

## Ejemplo 4 

Por supuesto, aquí tienes un ejemplo más extenso que utiliza `zenity` para crear un gestor de tareas simple. Este script permite al usuario agregar, listar y eliminar tareas utilizando una ventana de diálogo:

```python
import subprocess

# Lista para almacenar las tareas
tareas = []

while True:
    # Mostrar menú de opciones
    opcion = subprocess.run(['zenity', '--list', '--title=Gestor de Tareas', '--column=Acción', 'Agregar Tarea', 'Listar Tareas', 'Eliminar Tarea', 'Salir'], capture_output=True, text=True)

    # Obtener la opción seleccionada por el usuario
    accion = opcion.stdout.strip()

    if accion == 'Agregar Tarea':
        # Solicitar al usuario que ingrese una tarea
        nueva_tarea = subprocess.run(['zenity', '--entry', '--title=Agregar Tarea', '--text=Ingrese la nueva tarea:'], capture_output=True, text=True)
        tarea = nueva_tarea.stdout.strip()
        
        if tarea:
            tareas.append(tarea)
            subprocess.run(['zenity', '--info', '--text', f'Tarea agregada: {tarea}', '--ok-label=Ok'])
        else:
            subprocess.run(['zenity', '--error', '--text', 'No se ingresó ninguna tarea.', '--ok-label=Ok'])

    elif accion == 'Listar Tareas':
        # Mostrar la lista de tareas
        if tareas:
            lista_tareas = '\n'.join(tareas)
            subprocess.run(['zenity', '--text-info', '--title=Lista de Tareas', '--width=400', '--height=300', '--editable', '--filename=-'], input=lista_tareas, capture_output=True)
        else:
            subprocess.run(['zenity', '--info', '--text', 'No hay tareas pendientes.', '--ok-label=Ok'])

    elif accion == 'Eliminar Tarea':
        if tareas:
            # Mostrar las tareas y permitir al usuario seleccionar una para eliminar
            tarea_eliminar = subprocess.run(['zenity', '--list', '--title=Eliminar Tarea', '--column=Tareas', *tareas], capture_output=True, text=True)

            if tarea_eliminar.stdout.strip() in tareas:
                tareas.remove(tarea_eliminar.stdout.strip())
                subprocess.run(['zenity', '--info', '--text', 'Tarea eliminada exitosamente.', '--ok-label=Ok'])
            else:
                subprocess.run(['zenity', '--error', '--text', 'No se seleccionó ninguna tarea.', '--ok-label=Ok'])
        else:
            subprocess.run(['zenity', '--info', '--text', 'No hay tareas pendientes para eliminar.', '--ok-label=Ok'])

    elif accion == 'Salir':
        break
```

Este script simula un gestor de tareas básico utilizando `zenity`. Permite al usuario agregar nuevas tareas, listar las tareas existentes, eliminar tareas seleccionadas y salir del programa.



Claro, aquí tienes un ejemplo básico de una aplicación con `zenity` y Python que permite agregar, listar y eliminar tareas. Esta aplicación utilizará un archivo de texto para guardar las tareas y mantenerlas entre ejecuciones:

```python
import subprocess

# Cargar las tareas desde un archivo de texto al inicio del script
try:
    with open('tareas.txt', 'r') as archivo:
        tareas = archivo.read().splitlines()
except FileNotFoundError:
    tareas = []  # Si el archivo no existe, crear una lista vacía de tareas

while True:
    # Mostrar menú de opciones
    opcion = subprocess.run(['zenity', '--list', '--title=Gestor de Tareas', '--column=Acción', 'Agregar Tarea', 'Listar Tareas', 'Eliminar Tarea', 'Salir'], capture_output=True, text=True)

    # Obtener la opción seleccionada por el usuario
    accion = opcion.stdout.strip()

    if accion == 'Agregar Tarea':
        # Solicitar al usuario que ingrese una tarea
        nueva_tarea = subprocess.run(['zenity', '--entry', '--title=Agregar Tarea', '--text=Ingrese la nueva tarea:'], capture_output=True, text=True)
        tarea = nueva_tarea.stdout.strip()
        
        if tarea:
            tareas.append(tarea)
            subprocess.run(['zenity', '--info', '--text', f'Tarea agregada: {tarea}', '--ok-label=Ok'])
        else:
            subprocess.run(['zenity', '--error', '--text', 'No se ingresó ninguna tarea.', '--ok-label=Ok'])

    elif accion == 'Listar Tareas':
        # Mostrar la lista de tareas
        if tareas:
            lista_tareas = '\n'.join(tareas)
            subprocess.run(['zenity', '--text-info', '--title=Lista de Tareas', '--width=400', '--height=300', '--editable', '--filename=-'], input=lista_tareas, capture_output=True)
        else:
            subprocess.run(['zenity', '--info', '--text', 'No hay tareas pendientes.', '--ok-label=Ok'])

    elif accion == 'Eliminar Tarea':
        if tareas:
            # Mostrar las tareas y permitir al usuario seleccionar una para eliminar
            tarea_eliminar = subprocess.run(['zenity', '--list', '--title=Eliminar Tarea', '--column=Tareas', *tareas], capture_output=True, text=True)

            if tarea_eliminar.stdout.strip() in tareas:
                tareas.remove(tarea_eliminar.stdout.strip())
                subprocess.run(['zenity', '--info', '--text', 'Tarea eliminada exitosamente.', '--ok-label=Ok'])
            else:
                subprocess.run(['zenity', '--error', '--text', 'No se seleccionó ninguna tarea.', '--ok-label=Ok'])
        else:
            subprocess.run(['zenity', '--info', '--text', 'No hay tareas pendientes para eliminar.', '--ok-label=Ok'])

    elif accion == 'Salir':
        # Guardar las tareas en un archivo de texto antes de salir
        with open('tareas.txt', 'w') as archivo:
            for tarea in tareas:
                archivo.write(tarea + '\n')
        break
```

Este script funcionará como una aplicación básica para gestionar tareas usando `zenity`. Al iniciar, cargará las tareas desde el archivo `tareas.txt`, permitirá agregar, listar y eliminar tareas, y finalmente, guardará las tareas actualizadas en el archivo antes de salir.

## EJEMPLO

¡Claro! Puedes crear un archivo `.desktop` que actúe como un acceso directo y permita ejecutar tu aplicación cuando se hace clic en él. Aquí te muestro cómo hacerlo:

1. **Crea un archivo `.desktop`:**

Abre un editor de texto y copia el siguiente contenido:

```plaintext
[Desktop Entry]
Name=Gestor de Tareas
Exec=/usr/bin/python3 /ruta/a/tu/directorio/gestor_tareas.py
Icon=gnome-panel-launcher
Type=Application
Categories=Utility;
```

Asegúrate de cambiar `/ruta/a/tu/directorio/gestor_tareas.py` por la ruta completa de tu script `gestor_tareas.py`.

2. **Guarda el archivo con extensión `.desktop`:**

Guarda este archivo con el nombre `tareas.desktop`. Puedes elegir el nombre que desees, pero asegúrate de que la extensión sea `.desktop`.

3. **Hazlo ejecutable:**

Si es necesario, otorga permisos de ejecución al archivo `.desktop` con el siguiente comando en la terminal:

```bash
chmod +x tareas.desktop
```

4. **Colócalo en tu escritorio:**

Ahora, simplemente mueve o copia este archivo `tareas.desktop` a tu escritorio o a cualquier otra ubicación conveniente.

Al hacer doble clic en este archivo `.desktop`, se ejecutará tu aplicación de gestión de tareas directamente.

Recuerda cambiar la ruta del ejecutable y la ruta al script `gestor_tareas.py` según sea necesario para que se corresponda con la ubicación real de tu archivo.

* Ejemplo de donde estan los `.desktop ` en ubuntu
```
cd /usr/share/applications
```
* crea el desktop
```
nano tareas.desktop
```
```plaintext
[Desktop Entry]
Name=Gestor de Tareas
Exec=/usr/bin/python3 /ruta/a/tu/directorio/gestor_tareas.py
Icon=gnome-panel-launcher
Type=Application
Categories=Utility;
```
### Guarda el archivo
* Ahora dale permisos
```bash
chmod +x tareas.desktop
```

