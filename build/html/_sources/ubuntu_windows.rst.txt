Pasos para instalar Ubuntu con WSL
==================================

1. Activar WSL:

	• Abre PowerShell como Administrador.
	• Ejecuta el siguiente comando para instalar WSL y Ubuntu de forma automática:

**powershell**

.. code:: Bash

   wsl --install -d Ubuntu

2. Reiniciar el equipo:

	• Si Windows te lo solicita al terminar el comando, reinicia tu computadora.

3. Configurar Ubuntu:

	• Tras el reinicio, se abrirá una ventana de consola de Ubuntu.
	• Introduce un **nombre de usuario** y una **contraseña** para tu cuenta de Linux (por seguridad, mientras escribes la contraseña no se mostrarán los caracteres).


**Install Python**

1. Update the APT package index:

.. code:: Bash

   sudo apt update

2. Install Python:

.. code:: Bash

   sudo apt install python3 -y

3. Verify the installed version:

.. code:: Bash

    python3 --version


**Install pip**

pip is the standard package manager for Python, used to install and manage packages from the Python 
Package Index.

1. Install pip:

.. code:: Bash
  
   sudo apt install python3-pip -y

2. Verify the installed version:

.. code:: Bash

   pip3 --version

**Test the Python Interpreter**

The interactive shell confirms the interpreter is installed and responding correctly.

.. code:: Bash

   python3
   >>> print("Hello, Python!")
   Hello, Python!
   >>> import sys; print(sys.version)
   >>> exit()

**Solución a ModuleNotFoundError: No module named 'Tkinter'**

.. code:: Bash

   sudo apt-get install python3-tk


