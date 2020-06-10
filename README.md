Dei um Fork do Projeto base do SeleniumBase para faciltar a criação do ambiente de testes.

Com o Python (qualquer versão) e Git instalados, rodar os comandos abaixo:

  1- git clone https://github.com/danimaiams/SeleniumBase.git
  
  2- cd SeleniumBase
  
  3- pip install -r requirements.txt
  
  4- python setup.py install
  
  5- pip install seleniumbase
  
  
Para rodar no Chrome, fazer:
  6- seleniumbase install chromedriver
  
  7- seleniumbase install chromedriver latest
  
Nesta etapa já estará pronto para rodar os testes usando SeleniumBase

  Para rodar o teste, digite:
  
    pytest test_qa.py 
    
    ou 
    
    pytest test_qa.py --demo (este segundo mostra o test rodando devagar e mostrando os elementos)
    
  Para rodar o teste e ver o resultado depois, digite:
  
    nosetests test_qa.py --report --demo
    
  Após rodar, vá até a pasta "latest_report\report.html" ou "archived_reports\report_number" e procure pelo último gerado.
  
  Obs.:
  
    - Os elementos da páginas deveriam ficar em um script diferente para facilitar na manutenção do código
    
    - As etapas dos testes deveriam ser chamadas por funções para deixar o código mais limpo
    
    - O documento bem elaborado com os casos de testes bem explicados ficou faltante, justamente por falta de tempo.
    
    - Toda essa etapa de montagem do ambiente, criação do test e commit demorou entre 21hrs e 23hrs do dia 09/06 (sim, desculpa)
  
