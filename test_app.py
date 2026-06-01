from app import obtener_tareas


def test_lista_tareas():
    tareas = obtener_tareas()

    assert len(tareas) == 3
    assert "Estudiar GitHub Actions" in tareas