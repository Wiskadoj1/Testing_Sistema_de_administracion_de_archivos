# Sistema de Administración de Archivos — SIGAD

Proyecto desarrollado por el equipo **R.O.M.** como parte del desarrollo y validación de una aplicación web para la gestión documental de una institución académica.

## Descripción del sistema

**SIGAD** es un sistema web de administración de archivos que permite registrar, consultar, organizar y dar seguimiento a documentos institucionales. El sistema está orientado a mejorar la gestión de documentos dentro de una institución académica mediante el uso de roles, filtros de búsqueda, carga de documentos y visualización organizada de la información.

El sistema permite trabajar con usuarios de tipo **Administrador** y **Trabajador**, mostrando permisos y funciones distintas de acuerdo con el rol asignado.

## Objetivo del sistema

Facilitar la administración de documentos institucionales mediante una plataforma web que permita subir, buscar, visualizar, editar y eliminar registros de archivos de manera organizada y segura.

## Funcionalidad principal

El sistema permite:

- Iniciar sesión con credenciales válidas.
- Validar accesos incorrectos mediante mensajes de error.
- Mostrar un panel principal según el rol del usuario.
- Consultar información del perfil del usuario.
- Subir documentos al sistema.
- Buscar archivos registrados.
- Consultar ayuda dentro de la aplicación.
- Cambiar entre tema claro y tema oscuro.
- Cerrar sesión.
- Administrar documentos de acuerdo con los permisos del usuario.

## Equipo de desarrollo

| Integrante | Rol dentro del proyecto |
|---|---|
| Antonio Garcia Braulio Gerardo | Project Manager |
| Bravo Vilchis Nicolás | Arquitecto de Software |
| García Novoa Mario | Programador Frontend |
| Okamoto Resendiz Rodrigo Alexis | Analista de Requerimientos |
| Romero Vargas Rodrigo Manuel | Programador Backend |
| Serrepe Ramírez Julio Alejandro | Tester QA |

## Tecnologías utilizadas

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend y base de datos

- Supabase
- PostgreSQL
- Supabase Auth
- Supabase Storage

### Testing automatizado

- Python
- Selenium WebDriver
- Pytest

### Herramientas de apoyo

- GitHub
- Visual Studio Code
- Google Chrome
- ChromeDriver

## Repositorio del proyecto

Repositorio de testing:

```text
https://github.com/Wiskadoj1/Testing_Sistema_de_administracion_de_archivos
```

## URL del sistema probado

URL utilizada por los scripts de prueba:

```text
https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html
```

## Instalación del entorno de pruebas

Para ejecutar las pruebas automatizadas es necesario contar con:

- Python instalado.
- Google Chrome instalado.
- ChromeDriver compatible con la versión del navegador.
- Selenium y Pytest instalados.

### 1. Clonar el repositorio

```bash
git clone https://github.com/Wiskadoj1/Testing_Sistema_de_administracion_de_archivos.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd Testing_Sistema_de_administracion_de_archivos
```

### 3. Instalar dependencias

```bash
pip install selenium pytest
```

## Ejecutar el sistema

El sistema se ejecuta desde el navegador mediante la URL publicada:

```text
https://wiskadoj1.github.io/Sistema-de-administraci-n-de-archivos/index.html
```

También puede ejecutarse localmente abriendo el archivo `index.html` del proyecto principal, siempre que se cuente con la configuración correspondiente de Supabase.

## Ejecutar las pruebas automatizadas

Desde la terminal, dentro de la carpeta donde se encuentran los scripts de prueba, se pueden ejecutar los archivos de forma individual.

### Prueba de interacción con navegador y motor de búsqueda

```bash
python ejemplo_0.py
```

Este script abre Google, realiza una búsqueda y valida la interacción básica con el navegador.

### Prueba de carga del sistema

```bash
python ejemplo_1_carga.py
```

Este script abre la URL del sistema y valida que la página cargue correctamente.

### Prueba de login con credenciales válidas

```bash
python ejemplo_2_login_correcto.py
```

Este script ingresa credenciales válidas en el formulario de inicio de sesión y verifica el acceso al sistema.

### Prueba de login con credenciales inválidas

```bash
python ejemplo3_login_incorrecto.py
```

Este script ingresa credenciales incorrectas, valida el mensaje de error y genera una evidencia de la prueba.

### Ejecución con Pytest

```bash
pytest ejemplo4_pytest.py
```

Este script organiza los casos de prueba mediante una estructura basada en Pytest.

## Casos de prueba automatizados

| Archivo | Propósito |
|---|---|
| `ejemplo_0.py` | Interacción con navegador y motor de búsqueda |
| `ejemplo_1_carga.py` | Validación de carga del sistema |
| `ejemplo_2_login_correcto.py` | Autenticación con credenciales válidas |
| `ejemplo3_login_incorrecto.py` | Autenticación con credenciales inválidas y generación de evidencia |
| `ejemplo4_pytest.py` | Organización de pruebas mediante Pytest |

## Credenciales de prueba

### Administrador

```text
Usuario: admin@rom.com
Contraseña: Adminrom1
```

### Credenciales inválidas utilizadas en pruebas

```text
Usuario: correoPrueba@rom.com
Contraseña: 123
```

## Evidencias

Las evidencias generadas por las pruebas automatizadas se almacenan en la carpeta:

```text
evidencias/
```

Ejemplos de evidencias generadas:

```text
evidencias/login_incorrecto.png
evidencias/test_fallido.png
```

Las capturas se generan cuando una prueba requiere comprobar un resultado visual o cuando ocurre un fallo durante la validación.

## Estructura del proyecto de pruebas

```text
Testing_Sistema_de_administracion_de_archivos/
│
├── README.md
├── .gitignore
├── ejemplo_0.py
├── ejemplo_1_carga.py
├── ejemplo_2_login_correcto.py
├── ejemplo3_login_incorrecto.py
├── ejemplo4_pytest.py
│
└── evidencias/
    ├── login_incorrecto.png
    └── test_fallido.png
```

## Archivos que no deben subirse al repositorio

Los siguientes archivos y carpetas no deben subirse al repositorio porque son generados automáticamente por Python, Pytest o el editor de código:

```text
__pycache__/
.pytest_cache/
*.pyc
CACHEDIR.TAG
nodeids
settings.json
```

Se recomienda agregarlos al archivo `.gitignore`.

## Contenido recomendado para `.gitignore`

```gitignore
__pycache__/
.pytest_cache/
*.pyc
.vscode/
evidencias/*.tmp
```

## Descripción de las pruebas

### 1. Interacción con navegador

El script `ejemplo_0.py` valida que Selenium pueda abrir un navegador, acceder a Google y realizar una búsqueda automática.

### 2. Carga del sistema

El script `ejemplo_1_carga.py` valida que la página principal del sistema cargue correctamente desde la URL publicada.

### 3. Login correcto

El script `ejemplo_2_login_correcto.py` valida el ingreso al sistema con credenciales válidas de administrador.

### 4. Login incorrecto

El script `ejemplo3_login_incorrecto.py` valida que el sistema muestre un mensaje de error cuando se ingresan credenciales inválidas.

### 5. Pruebas organizadas con Pytest

El script `ejemplo4_pytest.py` integra pruebas de carga, login correcto y login incorrecto utilizando una estructura basada en Pytest.

## Recomendación para completar el requisito adicional

Para cubrir completamente el requisito de una funcionalidad distinta a las vistas en clase, se recomienda agregar un nuevo archivo de prueba, por ejemplo:

```text
test_modo_oscuro.py
```

o

```text
test_ayuda.py
```

Este script puede validar una funcionalidad adicional del sistema, como:

- Cambio a modo oscuro.
- Apertura de la sección de ayuda.
- Consulta de perfil.
- Cierre de sesión.
- Búsqueda de archivos.

El script adicional también debe guardar evidencia en la carpeta `evidencias/`.

## Notas adicionales

- El sistema utiliza Supabase como backend y base de datos.
- El sistema maneja usuarios con diferentes permisos.
- Los administradores tienen acceso a funciones de gestión más amplias.
- Los trabajadores tienen acceso limitado de acuerdo con su área.
- Las pruebas automatizadas se ejecutan con Selenium WebDriver sobre Google Chrome.
- Las evidencias permiten comprobar el resultado de las pruebas realizadas.