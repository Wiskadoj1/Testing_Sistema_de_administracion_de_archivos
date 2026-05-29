# Proyecto: Sistema de Administración de Archivos
Desarrollado por el equipo **R.O.M.**. Este sistema web permite la gestión eficiente de documentos mediante la digitalización progresiva. Su objetivo principal es facilitar a los usuarios subir, editar, buscar, visualizar y eliminar archivos de forma segura, organizándolos por categorías y áreas, y gestionando roles de acceso (Administradores y Trabajadores).

---
## Tecnologías utilizadas
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS).
* **Backend / Base de Datos:** Supabase (PostgreSQL para el almacenamiento de datos tabulares y Storage para almacenar documentos PDF/Imágenes).
* **Testing Automatizado:** Python, Selenium WebDriver y Pytest.

---
## Instalación
Al ser una aplicación web con una arquitectura enfocada en el cliente y conectada a Supabase (Backend-as-a-Service), no requiere instalación de un servidor local complejo:

### 1. Clonar el repositorio
\`\`\`bash
git clone https://github.com/wiskadoj1/Sistema-de-administraci-n-de-archivos.git
\`\`\`

### 2. Entorno de Pruebas (Opcional)
Si deseas ejecutar las pruebas automatizadas de QA, necesitas instalar Python y las siguientes librerías:
\`\`\`bash
pip install pytest selenium
\`\`\`
*Asegúrate de contar con el ChromeDriver compatible con tu versión de navegador para que Selenium funcione correctamente.*

---
## Ejecutar sistema
* **Para usar el sistema:** Simplemente abre el archivo `index.html` en tu navegador web de preferencia. Alternativamente, puedes usar una extensión como "Live Server" en Visual Studio Code para un mejor entorno de desarrollo local.
* **Para ejecutar las pruebas automatizadas:** Abre tu terminal en la ruta de los scripts de prueba y ejecuta el comando `pytest` (Ej. `pytest ejemplo4_pytest.py`).

---
## Uso del sistema
* **Inicio de Sesión:** Ingresa tus credenciales (`admin@rom.com` para administrador de prueba). El sistema detectará automáticamente tu rol y área.
* **Trabajadores:** Solo pueden consultar y visualizar los documentos pertenecientes a su área específica.
* **Administradores:** Tienen acceso a todos los documentos de todas las áreas, pueden ver el "Área de origen" de los archivos, registrar nuevos documentos, adjuntar PDFs, y editar o eliminar registros existentes.
* **Navegación:** Toda la interfaz principal funciona como una Single Page Application (SPA). Usa el menú lateral para alternar entre "Perfil y Alertas", "Subir Documento", "Consultar Archivos" y "Ayuda".

---
## Funcionalidades principales
* **Control de Acceso Basado en Roles (RBAC):** Vistas, menús y permisos dinámicos que cambian dependiendo si el usuario es Trabajador o Administrador.
* **Digitalización a Demanda:** Soporte para inventarios físicos importados desde Excel (CSV), mostrando el estatus "Físico" y permitiendo adjuntar el documento digitalizado posteriormente sin generar duplicados en la base de datos.
* **Gestión de Archivos (CRUD):** Creación, lectura, actualización y eliminación de documentos con reemplazo automático en la nube (Supabase Storage) para no dejar archivos "basura".
* **Alerta Trimestral:** Indicador inteligente que calcula de forma automática los días faltantes para el envío de archivos a la Dependencia Central.
* **Seguridad:** Requisitos estrictos de contraseña (mínimo 8 caracteres, 1 mayúscula, 1 número), validación cruzada para recuperar contraseñas, y un código de registro maestro exclusivo para crear cuentas de administradores.
* **Modo Oscuro:** Interfaz adaptable a tema claro y oscuro que guarda de forma persistente la preferencia del usuario en el navegador.

---
## Evidencias
Las capturas de pantalla generadas por las pruebas automatizadas de Selenium (como inicios de sesión correctos, credenciales inválidas o fallos de aserción) se guardan automáticamente en la carpeta `evidencias/` generada por los scripts de Python durante la ejecución de los tests.

---
## Estructura del proyecto
\`\`\`text
proyecto/
│
├── index.html                 # Pantalla de Login principal
├── README.md                  # Documentación del proyecto
├── assets/                    # Imágenes, logos e iconos de la interfaz
├── css/
│   └── hoja_de_estilos.css    # Estilos globales de formularios, SPA y modo oscuro
├── js/
│   ├── script.js              # Lógica de Login y validación de usuario
│   ├── script_principal.js    # Lógica de la SPA (oficina principal), CRUD de archivos y roles
│   ├── script_registro.js     # Lógica de registro con validaciones de seguridad fuertes
│   ├── script_recuperar.js    # Lógica para restablecer contraseña
│   ├── generar_campos.js      # Constructor dinámico de formularios y selectores
│   ├── mensaje.js             # Animaciones visuales de alertas (verdes/rojas)
│   └── supabase.js            # Llaves de conexión con la base de datos de Supabase
├── pages/
│   ├── principal.html         # Interfaz principal (Contenedor de Vistas)
│   ├── registro.html          # Pantalla de registro de usuarios
│   └── recuperar.html         # Pantalla de recuperación de contraseña
└── tests_qa/                  # Scripts de Python/Selenium para Testing
    ├── ejemplo_1_carga.py
    ├── ejemplo_2_login_correcto.py
    ├── ejemplo3_login_incorrecto.py
    └── ejemplo4_pytest.py
\`\`\`

---
## Notas adicionales
* **Código de Administrador:** Para registrar una nueva cuenta con privilegios de Administrador en `registro.html`, el sistema solicitará un Código de Seguridad maestro. El código por defecto configurado es `ROM2026`.
* **Protección de Datos Inter-departamental:** En la base de datos, los trabajadores son estrictamente restringidos mediante consultas a Supabase (`query.eq('id_area', area)`) para garantizar que la información de otras áreas sea confidencial e inaccesible para ellos en todo momento.
* **Uso de LocalStorage:** El sistema utiliza el almacenamiento local del navegador web para mantener la sesión del usuario activa (como un gafete de acceso digital), almacenando de forma segura su rol, ID y área asignada para la navegación entre páginas.