import openai

# Inserir a chave de API para o programa funcionar

chave_api = input("Insira aqui a sua chave de API: ")

openai.api_key = chave_api

image = input("\nDigite a sua mensagem: ")

# Função que puxa a API da openai para gerar a imagem

gerador = openai.Image.create(
    model="dall-e-3",
    prompt=image,
    size="1024x1024",
    quality="standard",
    n=1,
)

print(gerador)

