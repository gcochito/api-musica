import 'package:flutter_test/flutter_test.dart';
import 'package:musica_client/api/musica_api.dart';
import 'package:musica_client/model/musica.dart';

void main() {
  final api = MusicaApi(baseUrl: 'http://localhost:8000');
  api.onInit();

  const musica = Musica(
    titulo: 'Viva La Vida',
    artista: 'Coldplay',
    album: 'Viva la Vida or Death and All His Friends',
    ano: 2008,
  );

  test('listar usa MusicaApi e retorna uma lista de Musica', () async {
    final response = await api.listar();
    expect(response.statusCode, 200);
    expect(response.body, isA<List<Musica>>());
  });

  test('buscar por ID retorna Musica', () async {
    final response = await api.buscarPorId(1);
    expect(response.statusCode, 200);
    expect(response.body, isA<Musica>());
    expect(response.body!.id, 1);
  });

  test('buscar ID inexistente retorna 404', () async {
    final response = await api.buscarPorId(99999);
    expect(response.statusCode, 404);
  });

  test('cadastrar retorna 201 e música com ID', () async {
    final response = await api.cadastrar(musica);
    expect(response.statusCode, 201);
    expect(response.body, isA<Musica>());
    expect(response.body!.id, isNotNull);
  });

  test('atualizar retorna 200 e os dados atualizados', () async {
    final response = await api.atualizar(1, musica.copyWith(id: 1, titulo: 'Título atualizado'));
    expect(response.statusCode, 200);
    expect(response.body!.titulo, 'Título atualizado');
  });

  test('excluir retorna 204', () async {
    final response = await api.excluir(1);
    expect(response.statusCode, 204);
    expect((await api.buscarPorId(1)).statusCode, 404);
  });

  test('excluir ID inexistente retorna 404', () async {
    final response = await api.excluir(99999);
    expect(response.statusCode, 404);
  });
}
