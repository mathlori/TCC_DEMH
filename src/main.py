from DEMH import DEMH


def main():

	# Leitura do arquivo de entrada:
	input_file = input("Nome do arquivo de entrada: ")
	input_file = "input/"+input_file

	print(input_file)
    # Declaração do DEMH de exemplo
	
	measures = [4]
	bpms = [120]
	tones = ["Am"]
	chords = ["Am", "F", "C", "G"]
	transitions = [
		"(0|1) [1, 2, 3] =4",
		"(1|2) [4, 5, 6] =4",
		"(2|3) [7, 8, 9] =4",
		"(3|4) [7, 8, 9] =4",
		"(4|1) [] =1",
		"(4|5) [] =4",
	]

	demh = DEMH(input_file)
	demh.print_demh()
    

if __name__ == "__main__":
	main()
