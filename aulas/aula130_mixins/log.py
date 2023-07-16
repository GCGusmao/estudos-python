# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt' #  exemplo de polimorfismo. Ele concatena a str com o path informado.

class Log:
    def _log(self, msg): #  Conhecido como assinatura do métrodo. Se você está sobreescrevendo o método, você não pode mudar a assinatura do mesmo (parâmetros, retorno e etc)
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que legal!')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que legal!')
