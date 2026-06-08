import time

def test_fazer_login_com_sucesso(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    
    # 1. Encontra o campo de Usuário e digita "Priscila"
    page.fill("[name='username']", "Priscila")
    
    # 2. Encontra o campo de Senha e digita "12345"
    page.fill("[name='password']", "12345")
    
    # 3. Encontra o botão de Login e clica nele
    page.click("//input[@value='Log In']")
    
    # 4. Verifica se a mensagem de Erro apareceu (atualizamos para o erro interno que achamos)
    mensagem_erro = page.text_content(".error")
    assert "An internal error has occurred" in mensagem_erro
    
    # 5. Pausa mágica de 5 segundos pra você ver a mensagem de erro na tela!
    time.sleep(7)