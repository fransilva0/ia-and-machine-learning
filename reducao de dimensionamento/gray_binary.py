import requests
from PIL import Image
from io import BytesIO

# Função para baixar a imagem

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Função para converter a imagem em níveis de cinza

def rgb_to_gray(image):
    gray_image = []
    width, height = image.size
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            row.append(gray)
        gray_image.append(row)
    return gray_image

# Função para binarizar a imagem

def gray_to_binary(gray_image, threshold=128):
    binary_image = []
    for row in gray_image:
        binary_row = []
        for pixel in row:
            if pixel >= threshold:
                binary_row.append(255) 
            else:
                binary_row.append(0)   
        binary_image.append(binary_row)
    return binary_image

# Função para converter a matriz de volta em imagem (grayscale)

def matrix_to_image(matrix):
    height = len(matrix)
    width = len(matrix[0])
    img = Image.new('L', (width, height))
    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), matrix[y][x])
    return img

# Utilizando nossas funções 

url = 'https://wallpapers.com/images/hd/landscape-pictures-a3hr6gk3xfx36dyg.jpg'

img = download_image(url)

gray_image = rgb_to_gray(img)
binary_image = gray_to_binary(gray_image, threshold=128)

gray_img = matrix_to_image(gray_image)
binary_img = matrix_to_image(binary_image)

gray_img.show(title='Imagem em Níveis de Cinza')
binary_img.show(title='Imagem Binarizada')

gray_img.save('imagem_gray.png')
binary_img.save('imagem_binary.png')
