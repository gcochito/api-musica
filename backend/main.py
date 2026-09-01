from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="API de Músicas", version="1.0.0")


class MusicaCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    artista: str = Field(..., min_length=1, max_length=200)
    album: str = Field(..., min_length=1, max_length=200)
    ano: int = Field(..., ge=1000, le=9999)


class Musica(MusicaCreate):
    id: int


musicas: List[Musica] = [
    Musica(id=1, titulo="Numb", artista="Linkin Park", album="Meteora", ano=2003),
    Musica(id=2, titulo="Bohemian Rhapsody", artista="Queen", album="A Night at the Opera", ano=1975),
    Musica(id=3, titulo="Billie Jean", artista="Michael Jackson", album="Thriller", ano=1982),
    Musica(id=4, titulo="Imagine", artista="John Lennon", album="Imagine", ano=1971),
    Musica(id=5, titulo="Tempo Perdido", artista="Legião Urbana", album="Dois", ano=1986),
]


def encontrar_musica(musica_id: int) -> Musica:
    musica = next((item for item in musicas if item.id == musica_id), None)
    if musica is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Música não encontrada")
    return musica


@app.get("/musicas", response_model=List[Musica])
def listar_musicas() -> List[Musica]:
    return musicas


@app.get("/musicas/{musica_id}", response_model=Musica)
def buscar_musica(musica_id: int) -> Musica:
    return encontrar_musica(musica_id)


@app.post("/musicas", response_model=Musica, status_code=status.HTTP_201_CREATED)
def cadastrar_musica(dados: MusicaCreate) -> Musica:
    novo_id = max((musica.id for musica in musicas), default=0) + 1
    musica = Musica(id=novo_id, **dados.model_dump())
    musicas.append(musica)
    return musica


@app.put("/musicas/{musica_id}", response_model=Musica)
def atualizar_musica(musica_id: int, dados: MusicaCreate) -> Musica:
    musica = encontrar_musica(musica_id)
    musica_atualizada = Musica(id=musica.id, **dados.model_dump())
    musicas[musicas.index(musica)] = musica_atualizada
    return musica_atualizada


@app.delete("/musicas/{musica_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_musica(musica_id: int) -> None:
    musica = encontrar_musica(musica_id)
    musicas.remove(musica)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
