## Projeto 01 — Password Validator:



### Interação com o agente:

Antes de iniciar de fato os trabalhos, fui perguntar ao agente de I.A se eu poderia apenas tirar uma duvida sobre o enunciado do exercício, e ele me respondeu:
"Não, isso já é meio caminho andado pra eu confirmar seu raciocínio antes de você testar na prática — e aí eu vou estar corrigindo teoria, não código. Não é assim que funciona aqui. Escreve o código com a interpretação que você tem do subject. Se estiver errado, vai aparecer sozinho quando você rodar os casos de borda, ou eu vou puxar isso na correção com perguntas. Errar a interpretação também faz parte do exercício — é dado, não desperdício. Vai lá, tenta."



Percebi que o agente está bem treinado para pegar no pé mesmo — errar a interpretação sozinho faz parte do processo.



### Contexto do projeto:

O programa pede um validador que classifica uma string (senha) e retorna um relatório, sem usar bibliotecas. O programa deve receber a senha como argumento e não input() fixo.



##### Ideia 1 (rejeitada):

Minha primeira ideia foi criar algumas listas separadas para letras maiúsculas e minúsculas, números e caracteres especiais. Depois receber uma string, separar cada caractere, verificar qual a "categoria" de cada um, e classificar se a senha é ou não válida ou segura utilizando variáveis contadoras para isso.



De primeira mão é a ideia mais "simples" no papel, porém mais difícil na prática.



###### **Motivo da rejeição:**

Após primeira verificação no sistema, o agente apontou que essa minha 1ª ideia apesar de funcional, não atendia aos requisitos que ele me pediu, pois as funções ficaram muito repetitivas.



Dessa maneira desenvolvi uma segunda linha de raciocínio.



##### Ideia 2 (aceita):

Criar apenas uma função "coringa" que recebe a ***senha*** e a ***lista desejada***, retornando a quantidade de caracteres dessa lista específica. Isso deixou o código muito mais limpo e fluido, eliminando a repetição.



#### Critérios que eu decidi para classificar as senhas:

|Classificação|Tamanho|Categorias exigidas|
|-|-|-|
|Fraca|menos de 7 caracteres|ou falta 1+ categoria|
|Média|menos de 9 caracteres|ou falta ter 2+ de cada categoria|
|Forte|9 ou mais caracteres|2+ de cada categoria|
|Muito forte|12 ou mais caracteres|3+ de cada categoria|



\---



## Aprendizados Técnicos:



* ##### **Função em python:**

Aprendi de maneira definitiva como funciona uma função em python.

Uma função é um bloco de código nomeado que realiza uma tarefa específica. Ela pode receber parâmetros de entrada e retornar um resultado. São criadas para evitar repetições de código, organizar o programa em partes menores e reutilizáveis, e permitir que uma mesma lógica seja utilizada com dados diferentes.



###### **Como funciona**:

Ex: *def soma(a, b):*

&#x09;*return a + b*



utilizamos o *def* para criar a função, em seguida damos um nome à ela.

Na frente colocamos os parâmetros que utilizaremos dentro dessa função ("os protagonistas"), em seguida dos dois pontos para indicar que iniciaremos o código da função.

Dentro colocaremos a lógica por trás de tal tarefa.

O comando *return* indica qual o resultado que essa função retornará ao ser utilizada, nesse caso, a função retornará a soma dos parâmetros *a* e *b*.



Para "chamarmos" a função, colocamos o nome dela e dentro os argumentos com os valores que queremos.

Ex: *print(soma(1, 3))*

O resultado um print retornando *4*.



Ou podemos guardar o resultado dentro de uma variável.

Ex: *resultado = soma(1,3)*

Agora a variável *resultado* tem o valor da tarefa executada pela função, nesse caso, a soma dos argumentos.



\---



* ##### **Regras básicas para criar uma senha segura:**

Para criar os critérios de segurança das senhas, tive que aprender alguns preceitos recomendados para que a senha seja segura. Aqui estão alguns deles:

* Longa: de preferência uma frase com letras, números e símbolos.
* Complexa: que tenha sentido apenas para você e não seja óbvia.
* Prática: você precisa se lembrar dela com facilidade.
* Impessoal: não use aniversário, nome ou informações muito pessoais.
* Atualizada a cada 6 ou 3 meses ou logo após usar em local inseguro.



\---



* ##### sys.argv:

O sistema pede para receber a senha como argumento, e não como um input() fixo. Fui atrás de maneiras de como fazer isso e descobri o sys.argv



O sys.argv é uma lista em python que guarda os argumentos fornecidos pela linha de comando.



###### **Como funciona:**

Primeiro, devemos importar o módulo utilizando o comando *import sys*.

Quando iniciamos um programa pelo terminal, fazemos desta forma:

*python solution.py* -> Assim o programa é iniciado.



Quando utilizamos os argumentos, colocamos ele na frente do nome do projeto. Ex:

*python solution.py senha123*



Desta forma, o módulo sys, cria uma lista recebendo os argumentos. A lista então fica assim: *sys.argv = \['solution.py', 'senha123']*.

O primeiro item (*sys.argv\[0]*) é sempre o nome do script. Os dados seguintes (*sys.argv\[1]*) são os valores digitados pelo usuário, e todos entram como texto (string).



Dentro do nosso código, podemos transformar o item numa variável:

senha = sys.argv\[1] -> Agora a variável guarda o valor do argumento digitado pelo usuário.



\---



* ##### Type Hints:

Os type hints são uma ferramenta que foi introduzida ao python para auxiliar desenvolvedores indicar explicitamente os tipos de dados de variáveis e dos retornos das funções. O uso não é obrigatório, mas elas podem ser extremamente úteis para quem está lendo o código.



###### Como funciona:

A sintaxe básica para adicionar type hints em variáveis é o seguinte:

*x: int = 10*

*y: float = 5.5*

*nome: str = 'João'*



Para funções, podemos indicar tanto o tipo dos parâmetros quanto o tipo de retorno:

*def somar(a: int, b: int) -> int:*

&#x20;   *return a + b*



Importante ressaltar que essas type hints não interferem no funcionamento do código, servindo então como praticamente um comentário.



















