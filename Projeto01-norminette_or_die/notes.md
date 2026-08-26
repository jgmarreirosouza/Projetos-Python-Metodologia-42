### Anotações sobre o projeto e aprendizados gerais durante a execução:



Antes de iniciar de fato os trabalhos, fui perguntar ao agente de I.A se eu poderia apenas tirar uma duvida sobre o enunciado do exercício, e ele me respondeu assim:
"Não, isso já é meio caminho andado pra eu confirmar seu raciocínio antes de você testar na prática — e aí eu vou estar corrigindo teoria, não código. Não é assim que funciona aqui. Escreve o código com a interpretação que você tem do subject. Se estiver errado, vai aparecer sozinho quando você rodar os casos de borda, ou eu vou puxar isso na correção com perguntas. Errar a interpretação também faz parte do exercício — é dado, não desperdício. Vai lá, tenta."



Percebemos que o agente está bem treinado para pegar no pé mesmo.



O programa pede: validador que clássica string e retorna relatório, sem usar biblioteca. O programa deve receber a senha como argumento e não input() fixo.



1ª IDEIA:
Minha primeira ideia é criar alguns dicionários para letras maiúsculas e minúsculas, números e caracteres especiais. Depois receber uma string, separar cada caractere verificar qual a "categoria" de cada um e designar por variáveis contadoras se a senha é ou não válida ou segura.
De primeira mão é a ideia mais "simples" no papel, mas talvez mais difícil na prática.

Critérios que eu decidi para classificar as senhas:

* Senha fraca: menos de 7 caracteres, ou strings sem pelo menos 1 caractere de cada "categoria"
* Senha média: menos de 9 caracteres, ou strings sem pelo menos 2 caracteres de cada "categoria"
* Senha forte: 9 ou mais caracteres com pelo menos 2 caracteres de cada "categoria"
* Senha muito forte: 12 ou mais caracteres com pelo menos 3 caracteres de cada "categoria"

