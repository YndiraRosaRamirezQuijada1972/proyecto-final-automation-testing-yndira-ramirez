import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_obtener_post():

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    # Validar status code
    assert response.status_code == 200

    # Convertir respuesta a JSON
    data = response.json()

    # Validar estructura
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

    # Validar contenido
    assert data["id"] == 1

    # Validar tipos de datos
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

def test_crear_post():
 
    payload = {
    "title": "Proyecto Automation Testing",
    "body": "Prueba automatizada con Requests",
    "userId": 1
    }
    
    response = requests.post(
    f"{BASE_URL}/posts",
    json=payload,
    timeout=10
    )
    
    # Validar código HTTP de creación
    assert response.status_code == 201
    
    data = response.json()
    
    # Validar estructura
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data
    
    # Validar contenido enviado
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    
    print(f"Post creado con ID: {data['id']}")


def test_eliminar_post():
 
    response = requests.delete(
    f"{BASE_URL}/posts/1",
    timeout=10
    )
    
    # Validar eliminación exitosa
    assert response.status_code == 200
    
    # JSONPlaceholder devuelve un objeto vacío
    data = response.json()
    
    assert data == {}

