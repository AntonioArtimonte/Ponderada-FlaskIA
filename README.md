# Upload de Imagem com Predição I.A

Este projeto permite o upload de imagens para a predição utilizando dois modelos de rede neural: um modelo linear simples e o modelo LeNet-5. A aplicação é construída utilizando Flask para o backend e permite o upload de imagens através de uma interface web simples.

## Comparação de Modelos

### Modelo Linear
- **Tempo de treinamento:** 43.89964437484741 segundos
- **Acurácia no teste:** 0.9768000245094299

### Modelo LeNet-5
- **Tempo de treinamento:** 186.78246140480042 segundos
- **Acurácia no teste:** 0.9901000261306763

### Comparação de Execução

| Modelo       | Tempo de Treinamento (s) | Acurácia no Teste |
|--------------|---------------------------|-------------------|
| Linear       | 43.899644                 | 0.9768            |
| LeNet-5      | 186.782461                | 0.9901            |

## Estrutura do Projeto

- `src/main.py`: Arquivo principal que contém a aplicação Flask.
- `src/templates/index.html`: Página HTML para upload de imagens e exibição dos resultados.
- `src/models/modelo_mnist.h5`: Arquivo do modelo LeNet-5 treinado.
- `src/models/linear_modelo_mnist.h5`: Arquivo do modelo linear treinado.

## Pré-requisitos

Certifique-se de ter os seguintes pacotes instalados:

- Flask
- TensorFlow
- PIL (Python Imaging Library)
- NumPy

Você pode instalar os pacotes necessários usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando o projeto

1. Clone o repositório

```bash
git clone https://github.com/AntonioArtimonte/Ponderada-FlaskIA
```

2. Inicie um ambiente virtual do python

```bash
python3 -m venv venv
```

3. Instale as depêndencias

```bash
python3 -m pip install -r src/requirements.txt
```

4. Inicie o serivodr flask

```bash
python3 src/main.py
```

## Uso

1. Na página inicial, faça o upload de uma imagem com algum algarismo.

2. A aplicação exibirá a predição dos dois modelos, junto com o tempo de processamento de cada um.

## Rotas da API

A aplicação Flask possui três rotas principais:

### 1. `/` (GET)

- **Descrição:** Esta rota é responsável por renderizar a página inicial do aplicativo.
- **Entrada:** Não recebe nenhum parâmetro.
- **Saída:** Retorna a página HTML contendo o formulário para upload de imagens.

### 2. `/upload_normal` (POST)

- **Descrição:** Esta rota processa a imagem enviada usando o modelo LeNet-5.
- **Entrada:**
  - Recebe um arquivo de imagem enviado através de um formulário com a chave `file`.
- **Processamento:**
  - A imagem é redimensionada para 28x28 pixels, convertida para escala de cinza, normalizada (dividida por 255) e reshapeada para o formato (1, 28, 28, 1).
  - O tempo de início é registrado antes de fazer a predição.
  - A predição é realizada pelo modelo LeNet-5.
  - O tempo de término é registrado após a predição.
- **Saída:**
  - Retorna um JSON com os seguintes dados:
    - `predict`: Classe prevista pelo modelo (inteiro).
    - `predict_normal_time`: Tempo gasto no processamento da predição (segundos).

### 3. `/upload_linear` (POST)

- **Descrição:** Esta rota processa a imagem enviada usando o modelo linear.
- **Entrada:**
  - Recebe um arquivo de imagem enviado através de um formulário com a chave `file`.
- **Processamento:**
  - A imagem é redimensionada para 28x28 pixels, convertida para escala de cinza, normalizada (dividida por 255) e reshapeada para o formato (1, 28, 28, 1).
  - O tempo de início é registrado antes de fazer a predição.
  - A predição é realizada pelo modelo linear.
  - O tempo de término é registrado após a predição.
- **Saída:**
  - Retorna um JSON com os seguintes dados:
    - `predict_linear`: Classe prevista pelo modelo (inteiro).
    - `predict_linear_time`: Tempo gasto no processamento da predição (segundos).


## Códigos referentes ao treinamento

Ambos os códigos utilizados para o treinamento do modelo estão disponíveis na pasta `Códigos-Treinamento`.

Ambos foram utilizados do jeito que estão em um arquivo `.py`, afim de diminuir o tempo de treinamento porém diminuir a acurácia pode-se reduzir as `epochs`, no treinamento dos modelos utilizados foram utilizadas épocas **50**.

## Vídeo

Para saber melhor como a aplicação funciona, segue um vídeo abaixo demonstrando o uso da mesma

[![Vídeo](IMG_1165.MOV)]

## Autor

Projeto desenvolvido por Antonio Artimonte Vaz Guimarães