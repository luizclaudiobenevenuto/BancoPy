from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.123.123-12', '02/09/1987')
angelina: Cliente = Cliente('Angelina jolie', 'angelina@gmail.com', '111.222.333-11', '08/07/1978')

# print(felicity)
# print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)