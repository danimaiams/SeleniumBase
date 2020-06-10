from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        #Abrir site
        self.open("http://automationpractice.com/index.php")
        self.maximize_window()
        self.assert_title("My Store") #conferir site correto

        self.update_text('input[class="search_query form-control ac_input"]', "printed dress")
        self.click('button[class="btn btn-default button-search"]')
        self.click('//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a')

        self.assert_text("Printed Summer Dress") #conferir se o vestido realmente é o escolhido
        self.click('a[id="color_14"]') #escolher cor azul de vestido
        self.click('button[class="exclusive"]')
    
    def test_submit_email(self):
        self.open("http://automationpractice.com/index.php")
        self.maximize_window()

        self.update_text('input[id="newsletter-input"]', 'falazeze@bomdia.com')
        self.click('button[name="submitNewsletter"]')
        self.assert_text_visible('This email address is already registered.')


    def test_wrong_search_item(self):
        self.open("http://automationpractice.com/index.php")
        self.maximize_window()
        self.update_text('input[class="search_query form-control ac_input"]', "bombapatch > pes")
        self.click('button[class="btn btn-default button-search"]')
        self.assert_element_visible('p[class="alert alert-warning"]')

    def test_login(self):
        self.open("http://automationpractice.com/index.php")
        self.maximize_window()

        self.click('a.login')
        self.update_text('input#email_create', 'cabuloso@cruzeiro.com')
        self.click('//*[@id="SubmitCreate"]/span')
        self.assert_element_visible('div#create_account_error')

        self.update_text('input#email', 'cabuloso@cruzeiro.com')
        self.update_text('input#passwd', 'Teste1234@') #poderia criptografar de alguma forma
        self.click('button#SubmitLogin')

        self.update_text('input[class="search_query form-control ac_input"]', "printed dress")
        self.click('button[class="btn btn-default button-search"]')
        self.click('//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a')

        self.assert_text("Printed Summer Dress") #conferir se o vestido realmente é o escolhido
        self.click('a[id="color_14"]') #escolher cor azul de vestido
        self.click('button[class="exclusive"]')
    
        self.click('span[class="continue btn btn-default button exclusive-medium"]')
        self.click('div.shopping_cart')
        self.assert_text_visible('1 Product')
    
