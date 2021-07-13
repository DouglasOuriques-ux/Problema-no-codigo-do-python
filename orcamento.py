# -*- coding: UTF-8 -*-


class Orcamento(object):
	
	em_aprovacao = 1
	aprovado = 2
	reprovado = 3
	finalizado = 4

	def __init__(self, valor):
		self.__itens = []
		self.estado_atual = Orcamento.em_aprovacao
		self.__desconto_extra = 0

	def aplica_desconto_extra(self):
		if self.estado_atual == Orcamento.em_aprovacao:
			self.__desconto_extra += self.valor * 0.02
		elif self.estado_atual == Orcamento.aprovado:
			self.__desconto_extra += self.valor * 0.05
		elif self.estado_atual == Orcamento.reprovado:
			raise Exception('Orçamentos reprovados não receberam desconto extra')
		elif self.estado_atual == Orcamento.finalizado:
			raise Exception('Orçamentos finalizados não receberam desconto extra')	
		
	@property	
	def valor(self):
		total = 0.0
		for item in self.__itens:
			total += item.valor
		return total - self.__desconto_extra

	def obter_itens(self):

		return tuple(self.__itens)

	@property
	def total_itens(self):
		return len(self.__itens)

	def adiciona_item(self, item):
		self.__itens.append(item)

class Item(object):

	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor = valor

	@property
	def valor(self):
		return self.__valor

	@property
	def nome(self):
		return self.__nome

if __name__ == '__main__':
			
	def __init__(self, orcamento, valor):
		self.orcamento = orcamento
		orcamento = Orcamento()
		orcamento.adciona_item(Item('ITEM - 1', 100))
		orcamento.adciona_item(Item('ITEM - 2', 50))
		orcamento.adciona_item(Item('ITEM - 3', 400))

		print (orcamento.valor)
		orcamento.aplica_desconto_extra()

		print (orcamento.valor)