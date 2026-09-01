import pytest
from fastapi.testclient import TestClient

from main import app, musicas

client = TestClient(app)


@pytest.fixture(autouse=True)
def restore_seed_data():
    original = list(musicas)
    yield
    musicas[:] = original


def test_listar_musicas():
    response = client.get("/musicas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 5


def test_buscar_musica_por_id():
    response = client.get("/musicas/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_buscar_musica_inexistente():
    assert client.get("/musicas/99999").status_code == 404


def test_cadastrar_musica():
    payload = {"titulo": "Viva La Vida", "artista": "Coldplay", "album": "Viva la Vida", "ano": 2008}
    response = client.post("/musicas", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["id"] is not None
    assert body["titulo"] == payload["titulo"]


def test_atualizar_musica():
    payload = {"titulo": "Numb (Remix)", "artista": "Linkin Park", "album": "Reanimation", "ano": 2002}
    response = client.put("/musicas/1", json=payload)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["album"] == "Reanimation"


def test_excluir_musica():
    response = client.delete("/musicas/1")
    assert response.status_code == 204
    assert client.get("/musicas/1").status_code == 404


def test_excluir_musica_inexistente():
    assert client.delete("/musicas/99999").status_code == 404


def test_rejeitar_dados_invalidos():
    payload = {"titulo": "", "artista": "Artista", "album": "Álbum", "ano": 2025}
    assert client.post("/musicas", json=payload).status_code == 422
