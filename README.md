# Hell-Triangle
Resolução do desafio "Hell Triangle" (disponível no arquivo HellTriangle-Challenge-3-2.pdf)

# Funcionamento
Para rodar o script é necessário passar dois argumentos: número de linhas e o vetor que representa o triângulo.
Para um triângulo com 4 linhas, por exemplo, o vetor seria representado da seguinte forma (onde os valores podem ser números quaisquer):

 ```[[6],[3,5],[9,7,1],[4,6,8,4]] ```
 
 A chamada pela linha de comando seguiria este formato:
 
 ```python helltriangle.py 4 [[6],[3,5],[9,7,1],[4,6,8,4]]```
 
 # Implementação
 A programação do desafio foi feita na linguagem **Python 2.7.9**, por ser uma linguagem fácil de se utilizar e entender.
 
 O script **helltriangle.py** possui 2 métodos: maiorElemento e HellTriangle.
 
 **HellTriangle** é o método principal, responsável por receber o número de linhas e o vetor que representa o triângulo. Ele percorre todas as linhas e chama o método **maiorElemento** para descobrir qual o maior elemento daquela linha específica. Obtido este resultado, o valor retornado é adicionado ao vetor de caminho e a posição do elemento é armazenada para uso futuro. Quando todas as linhas são percorridas, o vetor de caminhos fica completo e o método simplesmente soma os valores, retornando o máximo total.
 
 O método **maiorElemento** é privado e acessível apenas através do método HellTriangle. Ele é responsável por calcular o maior valor de uma dada linha. Este cálculo é feito ao comparar cada elemento da linha com um valor predeterminado e verificando qual o maior. Além desta verificação também é avaliado se o valor em questão é "vizinho" do maior valor da linha anterior.
 
 # Testes
 Os testes automatizados são feitos através do framework **PyUnit** (unittest). Para isto foi criado um script adicional chamado **testes.py**
 
  A chamada pela linha de comando seguiria este formato:
  
```python testes.py```

Os testes realizados são os seguintes:
- **test_numero_linhas_maior_triangulo**: Testa para qualquer caso em que o numero de linhas informado seja maior que o numero de linhas do triangulo.
- **test_sucesso**: Utiliza o exemplo do pdf e testa se o caminho escolhido é o correto, exibindo o máximo total
- **test_linhas_invalidas**: Testa se o numero de linhas informado é menor ou igual a zero
- **test_triangulo_valido**: Testa se o triangulo possui uma configuração valida (Cada linha deve possuir um elemento a mais que a linha anterior)
