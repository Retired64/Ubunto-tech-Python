import subprocess

mensaje = "Gracias por formar parte de esta gran comunidad androide, espero logres tus metas y objetivos."
subprocess.run(['zenity', '--info', '--text', mensaje, '--ok-label=Salir'])
