import openai

# Insira a sua chave de API 

openai.api_key = "" 

image = input("Digite a sua mensagem: ")

# Função que puxa a API da openai para gerar a imagem

gerador = openai.Image.create(
    model="dall-e-3",
    prompt=image,
    size="1024x1024",
    quality="standard",
    n=1,
)

print(gerador)

