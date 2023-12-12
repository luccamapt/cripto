<div id="top"></div>

# Introdução à Criptografia

<!---Shields em: https://shields.io --->

![GitHub repo size](https://img.shields.io/github/repo-size/luccamapt/cg?style=for-the-badge&label=tamanho%20do%20repo&color=44aa00)
![GitHub contributors](https://img.shields.io/github/contributors/luccamapt/cg?style=for-the-badge&label=colaboradores&color=44aa00)
![GitHub stars](https://img.shields.io/github/stars/luccamapt/cg?style=for-the-badge&label=estrelas&color=44aa00)

<!-- LOGO -->
<br />
<div align="center">
  <a href="https://github.com/luccamapt/cripto">
    <img src="https://cdn.pixabay.com/photo/2016/03/31/17/58/computer-1294045_1280.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Introdução à Criptografia - Conjunto de Atividades</h3>

  <h5> Explore, aprenda e colabore para aprimorar seu entendimento sobre a arte da criptografia. </h5>
    <br />
    <a href="https://github.com/luccamapt/cripto/issues">Reportar erro</a>
    ·
    <a href="https://github.com/luccamapt/cripto/issues">Sugerir feature</a>
</div>
<br />
<br />

## 📜 Sobre o projeto

Este repositório é um espaço dedicado ao aprendizado e prática de conceitos fundamentais de criptografia. Aqui você encontrará exemplos de algoritmos de criptografia, implementações simples, exercícios resolvidos, e recursos educacionais para aprofundar seu conhecimento nessa disciplina fascinante da segurança da informação. Explore, aprenda e colabore para aprimorar seu entendimento sobre a arte da criptografia. 👨‍💻🔒

<p align="right"><a href="#top">↑</a></p>

## ⚙️ Desenvolvido com

Destacando as linguagens e documentações que contribuiram para a elaboração do projeto até aqui:
* [Python](https://docs.python.org/3/)

<p align="right"><a href="#top">↑</a></p>

## 🚀 Executando o projeto

### RC4

- Para a atividade de RC4 (16/10), execute o arquivo [*decrypt.py*](https://github.com/luccamapt/cripto/blob/main/rc4/decrypt.py) com a chave utilizada e uma entrada em hexadecimal (já criptografada). A pasta [entradas](https://github.com/luccamapt/cripto/tree/main/rc4/entradas) possui exemplo(s) de entrada, para executar o fornecido em classe basta executar:
  ```
  python3 decrypt.py < ./entradas/example.txt
  ```
  Se preferir, insira um entrada de sua preferência. A saída do example.txt fornecido em classe deve ser:
  ```
  Texto Decifrado: A resposta esta correta? SIM
  ```
  Outras saídas devem ser conferidas de acordo com a cifra utilizada.

### AES

- Para a atividade de AES (30/10), execute o arquivo [*decrypt.py*](https://github.com/luccamapt/cripto/blob/main/aes/decrypt.py) com a chave utilizada e uma entrada em hexadecimal (já criptografada). A pasta [entradas](https://github.com/luccamapt/cripto/tree/main/aes/entradas) possui exemplo(s) de entrada, para executar um exemplo padrão utilize o seguinte trecho:
  ```
  python3 decrypt.py < ./entradas/example-decrypt.txt
  ```
- Para a atividade de AES (13/11), execute o arquivo [*de-crypt.py*](https://github.com/luccamapt/cripto/blob/main/aes/de-crypt.py), uma versão extendida do código anterior que permite tanto descriptografar quanto criptografar. A pasta [entradas](https://github.com/luccamapt/cripto/tree/main/aes/entradas) possui exemplo(s) de entrada, para executar um exemplo padrão utilize um dos seguintes trechos:
  ```
  python3 decrypt.py < ./entradas/example-decrypt.txt
  ```

  ```
  python3 decrypt.py < ./entradas/example-decrypt.txt
  ```
  Se preferir, insira um entrada de sua preferência. A saída do example.txt fornecido deve ser:
  ```
  Texto Decifrado: A resposta esta correta? SIM
  ```
  Outras saídas devem ser conferidas de acordo com a cifra utilizada. No caso do AES que aceita apenas chaves de 16, 24 ou 32 bytes **a entrada deve ser alterada** para exibir a saída corretamente.

### Teoria dos números

- Para a atividade de Teoria dos números (11/12), execute os arquivos [*extended_gcd.py*](https://github.com/luccamapt/cripto/blob/main/atividade04/extended_gcd.py) ou [*square_and_multiply.py*](https://github.com/luccamapt/cripto/blob/main/atividade04/square_and_multiply.py). A seguir, exemplos de entrada e saída esperados:

| Exemplos GCD Extendido || 
| :---       | :---       | 
|Entrada     | Saída      |
|5 13        | 1 8        | 
|15 102      | 3 N        |

| Exemplos Quadrado-e-Multiplicação ||
| :---            | :---             |
| Entrada         | Saída            |
| 6 11 13         | 11               |
| 2215 5545 16381 | 11105            |

### RSA

- Para a atividade de RSA para números pequenos (11/12), execute o arquivo [*rsa_smallnumbers.py*](https://github.com/luccamapt/cripto/blob/main/rsa/rsa_smallnumbers.py). A seguir, exemplos de entrada e saída esperados:

| Exemplos RSA | Números pequenos |
| :---         | :---             | 
|Entrada       | Saída            |
|1073 71 436   | 726              | 
|91 43 19      | 33               |

<p align="right"><a href="#top">↑</a></p>

## ✔️ Roadmap - Ajustes e melhorias

O projeto ainda está em desenvolvimento de acordo com a sequência de atividades. Ainda assim, as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Otimização do código.
- [ ] Documentação da funções definidas e utilizadas.

<p align="right"><a href="#top">↑</a></p>

## 🤝 Colaborador

Por enquanto, apenas um padawan traça a jornada do herói:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/luccamapt">
        <img src="https://avatars.githubusercontent.com/u/62125928" width="100px;" alt="Foto do Lucca"/><br>
        <sub>
          <b>Lucca Marques</b>
        </sub>
      </a>
    </td>
  </tr>
</table>