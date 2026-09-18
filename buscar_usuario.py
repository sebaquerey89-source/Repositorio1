"""Interfaz sencilla y segura para ejecutar Sherlock desde este laboratorio."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


CARACTERES_VALIDOS = re.compile(r"^[A-Za-z0-9._-]{1,100}$")


def localizar_sherlock() -> Path | None:
    """Localiza el ejecutable instalado dentro del entorno virtual."""
    nombre = "sherlock.exe" if os.name == "nt" else "sherlock"
    junto_a_python = Path(sys.executable).resolve().parent / nombre
    if junto_a_python.exists():
        return junto_a_python

    encontrado = shutil.which("sherlock")
    return Path(encontrado) if encontrado else None


def main() -> int:
    if sys.version_info < (3, 9):
        print("Se necesita Python 3.9 o superior.")
        return 1

    usuario = input("Nombre de usuario que queres buscar: ").strip().lstrip("@")
    if not CARACTERES_VALIDOS.fullmatch(usuario):
        print(
            "Nombre no valido. Usa solamente letras, numeros, punto, "
            "guion o guion bajo."
        )
        return 2

    sherlock = localizar_sherlock()
    if sherlock is None:
        print("Sherlock no esta instalado. Ejecuta iniciar_sherlock.bat nuevamente.")
        return 1

    raiz = Path(__file__).resolve().parent
    carpeta_resultados = raiz / "resultados"
    carpeta_resultados.mkdir(exist_ok=True)

    print("\nBuscando coincidencias publicas...")
    print("Recordatorio: una coincidencia de nombre no confirma una identidad.\n")

    comando = [
        str(sherlock),
        usuario,
        "--print-found",
        "--csv",
        "--folderoutput",
        str(carpeta_resultados),
        "--no-color",
    ]

    try:
        proceso = subprocess.run(comando, cwd=raiz, check=False)
    except KeyboardInterrupt:
        print("\nBusqueda cancelada por el usuario.")
        return 130

    archivo_csv = carpeta_resultados / f"{usuario}.csv"
    if proceso.returncode == 0 and archivo_csv.exists():
        print(f"\nResultado guardado en: {archivo_csv}")
        print("Verifica manualmente cada enlace antes de sacar conclusiones.")
    elif proceso.returncode == 0:
        print("\nSherlock termino, pero no se encontro el CSV esperado.")
    else:
        print(f"\nSherlock termino con el codigo de error {proceso.returncode}.")

    return proceso.returncode


if __name__ == "__main__":
    raise SystemExit(main())
