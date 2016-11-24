import serial

porta = 'COM4'
velocidade = 9600
conexao = serial.Serial(porta,velocidade);

opcao = 0;


while opcao != "2":
	opcao = input("Digite 1 para ligar o led\nDigite 0 para desligar  o led\nDigite 2 para fechar o programa!\n");
	if opcao != "2":
		conexao.write(opcao.encode());
conexao.close()
