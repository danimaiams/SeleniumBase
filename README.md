Dei um Fork do Projeto base do SeleniumBase para faciltar a criação do ambiente de testes.

Com o Python (qualquer versão) e Git instalados, rodar os comandos abaixo:

  git clone ""
  
  cd SeleniumBase
  
  pip install -r requirements.txt
  
  python setup.py install
  
  pip install seleniumbase
  
  
Para rodar no Chrome, fazer:
  seleniumbase install chromedriver
  seleniumbase install chromedriver latest
  
Nesta etapa já estará pronto para rodar os testes usando SeleniumBase
  Para rodar o teste, digite:
    pytest nome_do_test.py ou pytest nome_do_test.py --demo (este segundo mostra o test rodando devagar e mostrando os elementos)
    
  Para rodar o teste e ver o resultado depois, digite:
    nosetests nome_test.py --report --demo
  Após rodar, vá até a pasta "Reports" e procure pelo último gerado.
  
