
# Sistema Fuzzy para Controle de Freio de Veículos

Este projeto simula um sistema fuzzy para controle de freio de veículos, utilizando três variáveis de entrada: pressão no pedal, velocidade da roda, e velocidade do carro. O sistema fuzzy gera como saída a pressão no freio que deve ser aplicada.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

```
TRAB_FUZZY_V2/
│
├── controle_freio.fcl           # Arquivo de regras fuzzy (usado para inferência)
├── dados_freio.xlsx             # Arquivo de dados de entrada (gerado automaticamente)
├── defuzzification.py           # Script responsável pela defuzzificação (centroide)
├── fuzzy_logic.py               # Script para fuzzificação das variáveis de entrada
├── fuzzy_rules.py               # Script contendo as regras fuzzy
├── gera_dados_freio.py          # Script para gerar dados de entrada fictícios (Faker)
├── main.py                      # Script principal que processa os dados fuzzy
├── resultados_freio.xlsx        # Arquivo de saída com os resultados fuzzy
└── README.md                    # Documentação do projeto
```

## Pré-requisitos

1. **Python 3.x**: Certifique-se de ter o Python instalado no seu sistema. Para verificar, execute o seguinte comando no terminal:
   ```
   python --version
   ```
2. **Bibliotecas Python**: Você precisará instalar as seguintes bibliotecas:
   - `pandas`: Para manipulação de dados em Excel.
   - `openpyxl`: Para leitura e escrita de arquivos Excel.
   - `Faker`: Para gerar dados fictícios (se precisar simular entradas).
   
   Instale essas dependências rodando o seguinte comando:
   ```
   pip install pandas openpyxl Faker
   ```

## Como Executar

### 1. Gerar Dados de Entrada

O script `gera_dados_freio.py` gera um conjunto de dados fictícios para simular diferentes condições de pressão no pedal, velocidade da roda e do carro. Para gerar esses dados:

```bash
python gera_dados_freio.py
```

Isso irá gerar o arquivo `dados_freio.xlsx` contendo as colunas:

- **Pressao_Pedal**: A força aplicada no pedal de freio.
- **Velocidade_Roda**: A velocidade da roda em km/h.
- **Velocidade_Carro**: A velocidade do carro em km/h.

### 2. Processar os Dados Fuzzy

O script `main.py` lê os dados de entrada do arquivo `dados_freio.xlsx`, aplica as regras fuzzy definidas no arquivo `controle_freio.fcl`, e salva os resultados no arquivo `resultados_freio.xlsx`.

Para processar os dados e gerar os resultados:

```bash
python main.py
```

Os resultados são salvos em `resultados_freio.xlsx` e incluem as seguintes colunas:

- **Pressao_Pedal**: Entrada de pressão no pedal.
- **Velocidade_Roda**: Entrada de velocidade da roda.
- **Velocidade_Carro**: Entrada de velocidade do carro.
- **Aplicar_Freio**: Resultado fuzzy que indica se o freio deve ser aplicado.
- **Liberar_Freio**: Resultado fuzzy que indica se o freio deve ser liberado.
- **Centroide**: Resultado da defuzzificação (valor nítido da pressão no freio).

### 3. Modificar o Sistema Fuzzy

Se você precisar ajustar as regras fuzzy, modifique o arquivo `controle_freio.fcl`. O arquivo contém as definições das variáveis de entrada e saída, bem como as regras de inferência fuzzy (Mamdani).

## Explicação do Sistema Fuzzy

### Entrada:
- **Pressao_Pedal**: Variável de entrada que representa a força exercida no pedal de freio (0 a 100).
- **Velocidade_Roda**: Velocidade da roda em km/h.
- **Velocidade_Carro**: Velocidade do carro em km/h.

### Saída:
- **Pressao_Freio**: O sistema fuzzy determina a pressão no freio que deve ser aplicada ou liberada com base nos valores de entrada.

### Regras Fuzzy:

As regras fuzzy são aplicadas com base em condições lógicas para determinar a pressão no freio.

- **Regra 1**: Se a pressão no pedal for média, então aplicar freio.
- **Regra 2**: Se a pressão no pedal for alta e a velocidade da roda e do carro forem altas, então aplicar freio.
- **Regra 3**: Se a pressão no pedal for alta e a velocidade da roda for baixa, então liberar o freio.
- **Regra 4**: Se a pressão no pedal for baixa, então liberar o freio.

## Contribuições

Sinta-se à vontade para fazer contribuições, relatar problemas ou sugerir melhorias via pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
