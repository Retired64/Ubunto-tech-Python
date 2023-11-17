import subprocess

# Mensaje principal
mensaje_principal = "Gracias por formar parte de esta gran comunidad androide, espero logres tus metas y objetivos."

# Opciones del submenú
sub_menu = [
    "Ver Texto 1",
    "Ver Texto 2"
]

# Mostrar ventana emergente con las opciones
resultado_menu = subprocess.run(['zenity', '--info', '--text', mensaje_principal, '--ok-label=Salir', '--extra-button=Ir al Submenú', '--title=Comunidad Android', '--extra-button=Salir', '--cancel-label=Salir', '--timeout=10', '--width=300', '--height=200'], capture_output=True, text=True, input='\n'.join(sub_menu))

# Verificar la selección del usuario en el submenú
if "Ir al Submenú" in resultado_menu.stdout:
    resultado_submenu = subprocess.run(['zenity', '--list', '--title=Submenú', '--column=Opciones', sub_menu[0], sub_menu[1]], capture_output=True, text=True)

    # Mostrar el texto de motivación según la opción seleccionada en el submenú
    if resultado_submenu.stdout.strip() == sub_menu[0]:
        texto_motivacion = "Texto de motivación 1: ¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!"
    elif resultado_submenu.stdout.strip() == sub_menu[1]:
        texto_motivacion = "Texto de motivación 2: ¡Tu actitud determina tu dirección!"

    subprocess.run(['zenity', '--info', '--text', texto_motivacion, '--ok-label=Ok'])
