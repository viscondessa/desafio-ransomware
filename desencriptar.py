importação os
importação pyaes

## abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
arquivo = abrir(file_name, "rb")
file_data = file.ler()
arquivo.fechar()

## chave para descriptografia
chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)
decrypt_data = aes.desencriptar(file_data)

## remover o arquivo criptografado
os.retirar(file_name)

## criar o arquivo descriptografado
new_file = "teste.txt"
new_file = abrir(f'{new_file}', "wb")
new_file.escrever(decrypt_data)
new_file.fechar()
