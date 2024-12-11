"""
Simulação do problema do Barbeiro Dorminhoco utilizando threads e semáforos em Python.

Este programa implementa o clássico problema de sincronização em sistemas operacionais,
o qual envolve um barbeiro que atende clientes em sua barbearia. O barbeiro dorme
quando não há clientes e atende-os conforme chegam e esperam em cadeiras limitadas.

Componentes principais:
1. Clientes chegam aleatoriamente e aguardam atendimento em uma fila circular limitada.
2. O barbeiro atende um cliente por vez, alternando entre cortar cabelos e dormir
   quando não há clientes.

Autores: Klebson Amarante, Mateus Tomaz, Isaac Alves
Data: 11/12/2024
"""

import threading
import time
import random

# Número máximo de cadeiras na sala de espera (excluindo a cadeira do barbeiro)
MAX = 3

# Fila circular para armazenar os clientes (com espaço adicional para o barbeiro)
begin = 0  # Posição inicial da fila
end = 0    # Próxima posição disponível na fila
size = 0   # Tamanho atual da fila
fila = [None] * (MAX + 1)  # Fila circular com tamanho MAX + 1 para facilitar operações

# Semáforos para controle de acesso e sincronização
semaforoFila = threading.Semaphore(MAX)  # Controla o número de clientes na fila de espera
semaforoBarbeiro = threading.Semaphore(0)  # Indica quando o barbeiro deve atender um cliente


# Função para verificar se a fila está vazia
def vazio():
    """
    Verifica se a fila está vazia.
    :return: True se a fila estiver vazia, False caso contrário.
    """
    return size == 0


# Função para adicionar um cliente à fila
def enqueue(cliente):
    """
    Adiciona um cliente à fila de espera.

    Se a fila estiver vazia, o cliente acorda o barbeiro.
    Caso a fila esteja cheia, o cliente vai embora sem ser atendido.

    :param cliente: ID do cliente que está entrando na fila.
    """
    global end, size

    if size < MAX + 1:
        # Cliente acorda o barbeiro ou senta na sala de espera
        if vazio():
            print(f"O cliente {cliente} acorda o barbeiro e senta em sua cadeira.")
        else:
            print(f"O cliente {cliente} senta em uma das cadeiras vagas da sala de espera.")

        # Adiciona o cliente à fila circular
        fila[end] = cliente
        end = (end + 1) % (MAX + 1)  # Incrementa posição circularmente
        size += 1

        # Sinaliza que há um cliente na sala de espera
        semaforoFila.release()
        semaforoBarbeiro.release()  # Acorda o barbeiro para atendimento
    else:
        # Cliente vai embora se não houver espaço
        print(f"Todas as cadeiras estavam ocupadas, o cliente {cliente} foi embora.")


# Função para atender um cliente (remover da fila)
def denqueue():
    """
    Remove o próximo cliente da fila e realiza o atendimento.

    O barbeiro corta o cabelo do cliente e, ao finalizar, verifica se há mais
    clientes na fila. Caso contrário, ele volta a dormir.

    :return: ID do cliente atendido ou -1 se a fila estiver vazia.
    """
    global begin, size

    if not vazio():
        # Simula o tempo de corte de cabelo (1 a 4 segundos)
        time.sleep(random.randint(1, 4))
        print(f"O barbeiro termina de cortar o cabelo do cliente {fila[begin]}, que vai embora.")

        cliente = fila[begin]
        begin = (begin + 1) % (MAX + 1)  # Incrementa posição circularmente
        size -= 1

        # Verifica se há mais clientes
        if vazio():
            print("Não há clientes para serem atendidos, o barbeiro vai dormir.")
        else:
            print(f"O cliente {fila[begin]} senta na cadeira do barbeiro.")

        return cliente
    else:
        # Fila vazia, barbeiro volta a dormir
        return -1


# Função que representa o comportamento de um cliente
def cliente_func(id_cliente):
    """
    Representa a chegada de um cliente na barbearia.

    O cliente tenta entrar na sala de espera e é adicionado à fila caso haja
    espaço. Caso contrário, ele vai embora.

    :param id_cliente: Identificador único do cliente.
    """
    global semaforoFila, semaforoBarbeiro

    # Aguarda até que haja espaço na sala de espera
    semaforoFila.acquire()
    enqueue(id_cliente)


# Função que representa o comportamento do barbeiro
def barbeiro_func():
    """
    Representa o trabalho do barbeiro.

    O barbeiro atende os clientes conforme chegam. Caso não haja clientes,
    ele dorme até que seja acordado por um cliente.
    """
    while True:
        # Aguarda até que haja um cliente para atender
        semaforoBarbeiro.acquire()
        denqueue()


# Função principal que cria threads para o barbeiro e os clientes
def main():
    """
    Função principal que inicializa a simulação.

    Cria uma thread para o barbeiro e simula a chegada de clientes com intervalos
    aleatórios.
    """
    # Cria a thread do barbeiro (daemon para encerrar com o programa)
    threading.Thread(target=barbeiro_func, daemon=True).start()

    i = 1  # Identificador dos clientes
    while True:
        # Simula a chegada de clientes em intervalos aleatórios (1 a 4 segundos)
        time.sleep(random.randint(1, 4))
        threading.Thread(target=cliente_func, args=(i,)).start()
        i += 1


# Executa a simulação
if __name__ == "__main__":
    main()
