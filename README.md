# API Música

Implementação da atividade de **API REST de Músicas + Flutter/GetConnect**, sem Pages, Widgets ou Controllers. O projeto foi organizado em duas partes: um backend em Python/FastAPI e um cliente Flutter contendo apenas o Model, a camada de API e os testes.

## Estrutura

```text
api-musica/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── tests/test_main.py
└── flutter/
    ├── pubspec.yaml
    ├── lib/model/musica.dart
    ├── lib/api/musica_api.dart
    └── test/
        ├── model/musica_test.dart
        └── api/musica_api_test.dart
```

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`. A documentação interativa pode ser acessada em `/docs`.

| Método | Endpoint | Resultado esperado |
| --- | --- | --- |
| GET | `/musicas` | Lista de músicas, HTTP 200 |
| GET | `/musicas/{id}` | Música encontrada, HTTP 200; ou HTTP 404 |
| POST | `/musicas` | Música criada, HTTP 201 |
| PUT | `/musicas/{id}` | Música atualizada, HTTP 200; ou HTTP 404 |
| DELETE | `/musicas/{id}` | Exclusão realizada, HTTP 204; ou HTTP 404 |

A persistência é intencionalmente feita em memória, conforme permitido na atividade. O backend é iniciado com cinco músicas e valida `titulo`, `artista`, `album` e `ano` por meio de modelos Pydantic.

Para executar os testes do backend:

```bash
cd backend
pytest -q
```

## Flutter/GetConnect

Com o backend em execução, instale as dependências e rode os testes de Model e integração da API:

```bash
cd flutter
flutter pub get
flutter test test/model/musica_test.dart
flutter test test/api/musica_api_test.dart
```

A classe `MusicaApi` utiliza exclusivamente os métodos do `GetConnect` (`get`, `post`, `put` e `delete`) e configura um `defaultDecoder` para transformar respostas JSON em `Musica` ou `List<Musica>`. O endereço padrão é `http://localhost:8000`; em um dispositivo físico, substitua-o pelo IP da máquina que executa o backend.

> Os testes em `test/api` são testes de integração e precisam da API Python disponível no endereço configurado.

## Decisões da implementação

O campo `id` é opcional no Model Flutter para permitir o envio de uma música nova sem identificador. No backend, o identificador é atribuído automaticamente após o cadastro. Não foram criados diretórios `pages`, `controllers` ou qualquer interface gráfica, respeitando o escopo da atividade.
