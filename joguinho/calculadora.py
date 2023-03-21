import os

class Calculadora:
	def __init__(self, initialValue):
		self.value = initialValue
		self.running = False
		print('-=-' * 30)

	def run(self):
		self.running = True
		
		while self.running:
			operation = float(input(f"O valor atual é {self.value}\nEscolha uma operação: [1] Somar, [2] Subtrair, [3] Multiplicar, [4] Dividir, [5] Divisão Exata, [6] Exponenciação\n[0] Tocar Valor, [-1] Cancelar: "))
			match operation:
				case -1:
					self.running = False
				case _:
					value = float(input("Qual o valor? : "))
					match operation:
						case 0:
							res = value
						case 1:
							res = self.soma(self.value, value)
						case 2:
							res = self.sub(self.value, value)					
						case 3:
							res = self.mult(self.value, value)					
						case 4:
							res = self.divi(self.value, value)	
						case 5:
							res = self.exdivi(self.value, value)
						case 6:
							res = self.expo(self.value, value)
						case _:
							print('Tente Novamente!')
							res = self.value
                        
			self.value = res
			os.system('cls' if os.name == 'nt' else 'clear')
			print('-=-' * 30)
			

	def soma(self, numA, numB):
		return numA + numB
                

	def sub(self, numA, numB):
		return numA - numB		

	def mult(self, numA, numB):
		return numA * numB

	def divi(self, numA, numB):
		return numA / numB

	def exdivi(self, numA, numB):	
		return numA // numB

	def expo(self, numA, numB):
		return numA ** numB


calc = Calculadora(float(input('Digite um valor inicial: ')))
calc.run()

input('press enter to exit')
