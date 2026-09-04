from DEMH import DEMH


def main():

	# Leitura do arquivo de entrada:
	input_file = input("Nome do arquivo de entrada: ")
	input_file = "src/input/"+input_file

	print(input_file)
    # Declaração do DEMH de exemplo

	demh = DEMH(input_file)

	demh.execute()
    

if __name__ == "__main__":
	main()
