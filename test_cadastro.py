import random
import pytest
from playwright.sync_api import Page, expect

def test_criar_conta_nova(page: Page):
    numero_aleatorio = random.randint(1000, 9999)
    username = f"priscila{numero_aleatorio}"
    password = "SenhaSegura123!"

    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    
    page.locator("[name='customer.username']").fill(username)
    page.locator("[name='customer.password']").fill(password)
    page.locator("[name='repeatedPassword']").fill(password)
    
    page.get_by_role("button", name="Register").click()
    
    expect(page.locator("h1.title")).to_contain_text(f"Welcome {username}")
    expect(page.locator("#rightPanel p")).to_contain_text("Your account was created successfully.")
    
    print(f"\nUsuário cadastrado com sucesso: {username} / {password}")


def test_cadastro_sem_last_name(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    # 1. Preenche o First Name, mas deixa o Last Name vazio
    page.locator("[name='customer.firstName']").fill("Priscila")
    
    # Preenche todos os outros dados
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    
    numero_aleatorio = random.randint(1000, 9999)
    page.locator("[name='customer.username']").fill(f"priscila{numero_aleatorio}")
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    
    page.get_by_role("button", name="Register").click()
    
    # Valida erro de Last Name
    erro_last_name = page.locator("[id='customer.lastName.errors']")
    expect(erro_last_name).to_be_visible()
    expect(erro_last_name).to_contain_text("Last name is required.")


# --- NOVO TESTE: VALIDAÇÃO DE ERRO (STATE OBRIGATÓRIO) ---
def test_cadastro_sem_state(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    
    # Deixa o State em branco de propósito! (não preenche o 'customer.address.state')
    
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    
    numero_aleatorio = random.randint(1000, 9999)
    page.locator("[name='customer.username']").fill(f"priscila{numero_aleatorio}")
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    
    page.get_by_role("button", name="Register").click()
    
    # Valida erro de State
    erro_state = page.locator("[id='customer.address.state.errors']")
    expect(erro_state).to_be_visible()
    expect(erro_state).to_contain_text("State is required.")


# --- NOVO TESTE: VALIDAÇÃO DE ERRO (CITY OBRIGATÓRIA) ---
def test_cadastro_sem_city(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    # Deixa City em branco!
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    
    numero_aleatorio = random.randint(1000, 9999)
    page.locator("[name='customer.username']").fill(f"priscila{numero_aleatorio}")
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    
    page.get_by_role("button", name="Register").click()
    
    # Valida erro de City
    erro_city = page.locator("[id='customer.address.city.errors']")
    expect(erro_city).to_be_visible()
    expect(erro_city).to_contain_text("City is required.")


# --- NOVO TESTE: VALIDAÇÃO DE ERRO (ZIP CODE OBRIGATÓRIO) ---
def test_cadastro_sem_zip_code(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    # Deixa Zip Code em branco!
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    
    numero_aleatorio = random.randint(1000, 9999)
    page.locator("[name='customer.username']").fill(f"priscila{numero_aleatorio}")
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    
    page.get_by_role("button", name="Register").click()
    
    # Valida erro de Zip Code
    erro_zip = page.locator("[id='customer.address.zipCode.errors']")
    expect(erro_zip).to_be_visible()
    expect(erro_zip).to_contain_text("Zip Code is required.")


# --- NOVO TESTE: VALIDAÇÃO DE ERRO (SSN OBRIGATÓRIO) ---
def test_cadastro_sem_ssn(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    # Deixa SSN em branco!
    
    numero_aleatorio = random.randint(1000, 9999)
    page.locator("[name='customer.username']").fill(f"priscila{numero_aleatorio}")
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    
    page.get_by_role("button", name="Register").click()
    
    # Valida erro de SSN
    erro_ssn = page.locator("[id='customer.ssn.errors']")
    expect(erro_ssn).to_be_visible()
    expect(erro_ssn).to_contain_text("Social Security Number is required.")


# --- NOVO TESTE: VALIDAÇÃO DE ERRO (SENHAS DIFERENTES) ---
def test_cadastro_senhas_diferentes(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    
    numero_aleatorio = random.randint(1000, 9999)
    page.locator("[name='customer.username']").fill(f"priscila{numero_aleatorio}")
    
    # Define senhas diferentes!
    page.locator("[name='customer.password']").fill("SenhaSegura123!")
    page.locator("[name='repeatedPassword']").fill("SenhaDiferente999!")
    
    page.get_by_role("button", name="Register").click()
    
    # Valida erro de senha repetida
    erro_confirmacao = page.locator("[id='repeatedPassword.errors']")
    expect(erro_confirmacao).to_be_visible()
    expect(erro_confirmacao).to_contain_text("Passwords did not match.")


# --- NOVO TESTE: VALIDAÇÃO DE ERRO (USUÁRIO JÁ EXISTENTE) ---
def test_cadastro_usuario_duplicado(page: Page):
    # Definimos um username fixo para tentar duplicar
    username_duplicado = f"usuario_teste_{random.randint(10000, 99999)}"
    
    # 1. Faz o primeiro cadastro com sucesso
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    page.locator("[name='customer.username']").fill(username_duplicado)
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    page.get_by_role("button", name="Register").click()
    
    # Garante que cadastrou
    expect(page.locator("h1.title")).to_contain_text(f"Welcome {username_duplicado}")
    
    # Fazer logout para poder tentar cadastrar de novo
    page.locator("text=Log Out").click()
    
    # 2. Tenta fazer o segundo cadastro com o mesmo username
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    page.locator("[name='customer.firstName']").fill("Priscila")
    page.locator("[name='customer.lastName']").fill("Marques")
    page.locator("[name='customer.address.street']").fill("Rua de Teste, 123")
    page.locator("[name='customer.address.city']").fill("Madrid")
    page.locator("[name='customer.address.state']").fill("Madrid")
    page.locator("[name='customer.address.zipCode']").fill("28001")
    page.locator("[name='customer.phoneNumber']").fill("+34 600 000 000")
    page.locator("[name='customer.ssn']").fill("123-456-789")
    page.locator("[name='customer.username']").fill(username_duplicado) # Username repetido!
    page.locator("[name='customer.password']").fill("Senha123!")
    page.locator("[name='repeatedPassword']").fill("Senha123!")
    page.get_by_role("button", name="Register").click()
    
    # Valida o erro de usuário já existente
    erro_username = page.locator("[id='customer.username.errors']")
    expect(erro_username).to_be_visible()
    expect(erro_username).to_contain_text("This username already exists.")