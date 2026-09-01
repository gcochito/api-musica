import 'package:flutter_test/flutter_test.dart';
import 'package:musica_client/model/musica.dart';

void main() {
  const json = {
    'id': 1,
    'titulo': 'Numb',
    'artista': 'Linkin Park',
    'album': 'Meteora',
    'ano': 2003,
  };

  test('fromJson converte JSON em Musica', () {
    final musica = Musica.fromJson(json);
    expect(musica.id, 1);
    expect(musica.titulo, 'Numb');
    expect(musica.artista, 'Linkin Park');
    expect(musica.album, 'Meteora');
    expect(musica.ano, 2003);
  });

  test('toJson converte Musica em JSON', () {
    const musica = Musica(id: 1, titulo: 'Numb', artista: 'Linkin Park', album: 'Meteora', ano: 2003);
    expect(musica.toJson(), json);
  });

  test('conversão JSON -> Musica -> JSON mantém os dados', () {
    expect(Musica.fromJson(json).toJson(), json);
  });

  test('toJson omite ID quando a música ainda não foi cadastrada', () {
    const musica = Musica(titulo: 'Nova', artista: 'Artista', album: 'Álbum', ano: 2024);
    expect(musica.toJson().containsKey('id'), isFalse);
  });
}
