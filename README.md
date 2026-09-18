# Laboratorio de Sherlock

Este repositorio es un laboratorio sencillo para aprender a ejecutar **Sherlock** en Windows sin mezclarlo con otros programas de Python.

Sherlock busca coincidencias de un nombre de usuario en sitios públicos. Los resultados son pistas: una coincidencia de nombre **no demuestra** que todas las cuentas pertenezcan a la misma persona.

## Inicio rápido en Windows

1. Descargá o cloná este repositorio en tu computadora.
2. Asegurate de tener instalado **Python 3.9 o superior**. Durante la instalación de Python, marcá la opción **Add Python to PATH**.
3. Hacé doble clic en `iniciar_sherlock.bat`.
4. Escribí un nombre de usuario propio o uno que tengas autorización para investigar.
5. Revisá el archivo CSV creado dentro de la carpeta `resultados`.

La primera ejecución puede tardar unos minutos porque crea un entorno aislado llamado `.venv` e instala Sherlock. Las siguientes serán más rápidas.

## ¿Qué contiene?

- `iniciar_sherlock.bat`: prepara el entorno y abre el buscador.
- `buscar_usuario.py`: valida el nombre, ejecuta Sherlock y organiza el resultado.
- `requirements.txt`: fija la versión utilizada para que el experimento sea reproducible.
- `.gitignore`: impide publicar el entorno local y los resultados de las búsquedas.
- `resultados/`: guarda localmente los CSV generados.

## Uso desde una terminal

También podés ejecutar directamente:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe buscar_usuario.py
```

## Qué esperar de los resultados

- Algunas páginas bloquean consultas automáticas o exigen iniciar sesión.
- Facebook, Instagram y X pueden no aparecer aunque exista una cuenta.
- También pueden aparecer falsos positivos.
- Conviene abrir y verificar manualmente cada enlace encontrado.
- Ejecutarlo desde una computadora personal suele funcionar mejor que desde servidores compartidos como Colab.

## Uso responsable

Usá este laboratorio únicamente con información pública y con fines legítimos. No lo utilices para acosar, suplantar identidades, recopilar datos sensibles ni intentar acceder a cuentas. Los resultados permanecen fuera de GitHub por defecto.

Proyecto original: [Sherlock Project](https://github.com/sherlock-project/sherlock), distribuido con licencia MIT.
