# Programa criado para testar afinidade com cursos da UFMG</h2>

<p>Esse programa foi criado espontâneamente por mim quando eu estava pensando em qual curso da UFMG queria ingressar. Anteriormente ja tinha olhado as grades dos cursos e conforme ia olhando a matéria decidia se gostava ou não daquela materia, o curso que eu gostasse de mais matérias ganhava. Entretanto, eu efetuei isso pelo navegador e abrindo as páginas dos cursos, o que pode me deixar imparcial. Foi por conta disso que tive a idéia desse programa.</p>
<h2>Versão 1</h2>
<p>Inicialmente a idéia era que ele funcionasse apenas para dois cursos, que eu estava em duvida entre eles, portanto, eu criei o programa "tester.py" que efetua o teste da seguinte forma: mostra no terminal, de maneira aleatória, o nome de alguma matéria dos cursos da ufmg que foram selecionados, solicita ao usuário uma resposta S ou N e contabiliza pontos se a resposta for S. Porém, no mesmo dia minha namorada disse que queria fazer também. Aí eu criei o importer.py que importava as matérias de um curso da ufmg via um link específico desse curso. Logo, depois desenvolvi o formater, que pegava a saida do importer.py e criava um arquivo txt que seria usado no tester.py. Após isso, meu amigo falou que queria realizar o teste também, foi nesse momento que integrei todos os programas eno version1.py e implentei novas funcionalidades como:</p>

- Funcionamento com mais de 2 cursos
- Mostrar um pequeno resumo de cada matéria
- Remoção de linhas vazias
- Remoção de linhas em que a disciplina é uma continuação de outra disciplina (Como Calculo II)
- Correção de bugs
- Utilização de argumentos de linha de comando para a escolha dos cursos
- Verificar se o curso selecionado existe por meio de um Dicionário gerado dinamicamente pela página da UFMG com o nome do curso e o link dele

<br>
<h2>Versão 2</h2>
<p>Programa transformado em web app com ajustes e funcionalidades:</p>

- Design Agradável
- Melhor UI
- Suporta como resposta um input do tipo range con intesidades de 0 a 5, indicando no 0 nenhuma afinidade e no 5 muita afinidade, deixando o teste mais preciso.
- Correção de bugs
- Animação criada para mostrar os resultados 
- Possibilidade de salvar os resultados por e-mail

<p>https://testedeafinidade.onrender.com/</p>
https://user-images.githubusercontent.com/87478201/225094646-d7d8641e-f9c1-496a-a871-9f27a7c37be9.mp4

