import abc


class MotorEventos(object):

    __metaclass__ = abc.ABCMeta

    memory = []

    rotinas_dict = {}

    acumulador = 0

    pc = 0

    def run(self):
        while self.pc < len(self.memory):

            instrucao = self.memory[self.pc]

            tipo_instrucao = self._identifica_instrucao(instrucao)

            self._executa_rotina(tipo_instrucao, instrucao)

    @abc.abstractmethod
    def _identifica_instrucao(self, instrucao):
        return

    @abc.abstractmethod
    def _executa_rotina(self, tipo_instrucao, instrucao):
        return