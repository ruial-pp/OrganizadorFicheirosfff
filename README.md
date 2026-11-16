# Organizador de Ficheiros

Atividade Prática Integradora do Módulo 4 da UFCD 10806.

## Objetivo

Listar os ficheiros da pasta de trabalho, apresentar a extensão e o tipo de cada ficheiro e contar o total. A listagem abrange os ficheiros diretamente na pasta. A versão atual apresenta também o tamanho em bytes.

## Ferramentas

Python 3 e Spyder para o programa, Git Bash e Git para o controlo de versões, GitHub para publicar o projeto e Vim para editar as notas.

## Execução no Spyder

1. Abra `organizador.py` no Spyder.
2. Escolha a pasta a consultar como diretório de trabalho. Nas opções de execução do ficheiro, confirme que o Spyder usa esse diretório.
3. Prima F5 e consulte a consola. Para testar, crie `exemplo.txt` nessa pasta e confirme que aparece na listagem.

Em alternativa, abra o terminal na pasta a consultar. Se o script estiver nessa pasta, execute `python organizador.py`. Se estiver noutra, passe o caminho completo do script entre aspas.

O programa identifica ficheiros Python, de texto e CSV pelas extensões `.py`, `.txt` e `.csv`. Numa pasta vazia, apresenta uma mensagem e indica zero ficheiros.
