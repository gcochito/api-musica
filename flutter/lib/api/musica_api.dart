import 'package:get/get.dart';

import '../model/musica.dart';

class MusicaApi extends GetConnect {
  MusicaApi({String baseUrl = 'http://localhost:8000'}) {
    httpClient.baseUrl = baseUrl;
  }

  @override
  void onInit() {
    httpClient.defaultDecoder = (response) {
      if (response is List) {
        return response
            .map((item) => Musica.fromJson(Map<String, dynamic>.from(item)))
            .toList();
      }
      if (response is Map<String, dynamic>) {
        return Musica.fromJson(response);
      }
      return response;
    };
    super.onInit();
  }

  Future<Response<List<Musica>>> listar() {
    return get<List<Musica>>('/musicas');
  }

  Future<Response<Musica>> buscarPorId(int id) {
    return get<Musica>('/musicas/$id');
  }

  Future<Response<Musica>> cadastrar(Musica musica) {
    return post<Musica>('/musicas', musica.toJson());
  }

  Future<Response<Musica>> atualizar(int id, Musica musica) {
    return put<Musica>('/musicas/$id', musica.toJson());
  }

  Future<Response<void>> excluir(int id) {
    return delete<void>('/musicas/$id');
  }
}
