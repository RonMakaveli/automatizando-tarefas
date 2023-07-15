# Sistema de Renomeação de Arquivos
Este é um sistema simples em Python que permite renomear arquivos em uma pasta especificada pelo usuário.<br>
Ele foi desenvolvido para ajudar a automatizar o processo de renomeação de arquivos em massa, especialmente para arquivos de música.

## Como usar
Clone este repositório em sua máquina local.<br>
Abra um terminal ou prompt de comando e navegue até a pasta do projeto.<br>
Execute o arquivo renomear_arquivos.py digitando python renomear_arquivos.py no terminal.<br>
Quando solicitado, digite o caminho completo para a pasta que contém os arquivos que deseja renomear.<br>
Aguarde enquanto o sistema renomeia os arquivos e exibe uma mensagem de conclusão.<br>

## Funcionamento
Este sistema é composto por um único arquivo Python, renomear_arquivos.py.<br>
Quando executado, ele solicita ao usuário que digite o caminho completo para a pasta que contém os arquivos que deseja renomear.<br>
Em seguida, ele usa a biblioteca os do Python para listar todos os arquivos na pasta especificada e iterar sobre eles.<br>

Durante o processo de iteração, o sistema executa três operações em cada arquivo:

Exclui os primeiros 10 caracteres do nome do arquivo.<br>
Renomeia os últimos 10 caracteres do nome do arquivo.<br>
Adiciona a extensão ".mp3" caso não exista.<br>
Após a conclusão do processo de renomeação, o sistema exibe uma mensagem de conclusão.<br>

## Pré-requisitos
Para usar este sistema, você precisará ter o Python instalado em sua máquina.<br> 
O sistema foi testado com sucesso nas seguintes versões do Python:

<ul>
  <li>Python 3.6</li>
  <li>Python 3.7</li>
  <li>Python 3.8</li>
  <li>Python 3.9</li>
</ul>

## Limitações
Este sistema foi desenvolvido para fins educacionais e não deve ser usado em ambientes de produção.<br>
Ele não inclui recursos avançados de tratamento de erros, como verificações de integridade de arquivos e pastas.<br> 
Portanto, use-o com cuidado e certifique-se de fazer backup de seus arquivos antes de executar o sistema.

## Contribuindo
Para contribuir para o projeto, sinta-se à vontade para enviar um pull request com suas melhorias ou correções.<br>
Faremos o possível para analisá-lo e integrá-lo ao projeto o mais rápido possível.
