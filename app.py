def obtener_tareas():
    return [
        "Estudiar GitHub Actions",
        "Crear Dockerfile",
        "Publicar imagen en GHCR"
    ]


def mostrar_tareas():
    print("=== Lista de Tareas ===")

    tareas = obtener_tareas()

    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")


if __name__ == "__main__":
    mostrar_tareas()