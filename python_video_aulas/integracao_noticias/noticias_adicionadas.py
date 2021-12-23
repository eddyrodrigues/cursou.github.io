def insere_noticia(titulo, texto_noticia, autor):
  arq_tmp = open('minhas_noticias.php', 'a+', encoding="utf-8")
  minha_string_saida = '\nTemos a notícia de titulo "{}"</br>Onde o texto é: <strong>{}</strong></br>Postada por: <strong>{}</strong>'.format(titulo, texto_noticia, autor)
  arq_tmp.write(minha_string_saida)
  arq_tmp.close()

insere_noticia("Corona volta com tudo", "Coronavirus não é extinto", "Eduardo")
