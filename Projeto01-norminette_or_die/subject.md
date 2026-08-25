### **PROJECT 01 — norminette\_or\_die**



#### **Objetivo**

Construir um validador de senha em Python que classifica uma string de entrada segundo critérios de robustez, retornando um relatório estruturado — sem usar nenhuma biblioteca pronta de validação (nada de re neste projeto).



##### **Regras**

* Proibido usar o módulo re (regex). Você vai iterar e comparar caractere a caractere.
* Proibido usar eval, exec, ou qualquer solução "mágica" de uma linha que esconda a lógica.
* Programa deve rodar via linha de comando, recebendo a senha como argumento (não como input() fixo — pense em como tornar isso flexível).
* Nenhuma função pode ultrapassar 15 linhas de corpo (sem contar assinatura e docstring).
* Zero código duplicado — se você perceber que copiou/colou lógica parecida em dois lugares, isso é uma reprovação na correção.



#### **O que o programa deve verificar**

A senha deve ser classificada em: fraca, média, forte, muito forte — com base em critérios que você vai definir e justificar (não vou te dizer quais critérios usar nem quantos pontos cada um vale). Na correção, vou te perguntar por que você escolheu os critérios que escolheu.



#### **Casos de borda que a correção vai cobrar (pense neles agora, não depois)**

* String vazia
* Senha com só espaços
* Senha gigante (tipo 500+ caracteres) — seu programa trava, fica lento, ou lida numa boa?
* Caracteres unicode/acentos (café123, senha\_com\_émoji)
* Argumento não fornecido na linha de comando



#### **Critérios de aceite (o que será avaliado)**

1. Funciona sem crashar em nenhum dos casos de borda acima
2. Nenhuma função > 15 linhas
3. Nomes de variáveis e funções autoexplicativos (nada de s, tmp, flag1)
4. Type hints em todas as funções
5. Você consegue justificar cada critério de classificação que escolheu

