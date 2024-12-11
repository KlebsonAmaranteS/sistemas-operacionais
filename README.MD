# Sistema de Sincronização - O Barbeiro Dorminhoco

Este projeto implementa o algoritmo clássico de sincronização do "Barbeiro Dorminhoco", utilizando threads e semáforos. O objetivo do código é simular a situação em que o barbeiro atende os clientes de uma sala de espera limitada, onde o barbeiro pode "dormir" quando não há clientes, e os clientes podem ir embora se não houver cadeiras disponíveis.

## Funcionalidades

- Simulação de um barbeiro que atende clientes de uma sala de espera com cadeiras limitadas.
- Uso de semáforos para controlar o número de clientes na fila de espera e a disponibilidade da cadeira do barbeiro.
- Cada cliente entra na fila, espera sua vez, e o barbeiro atende um cliente de cada vez.
- Se a fila estiver cheia, o cliente vai embora.
- O barbeiro "dorme" se não houver clientes para atender.

## Requisitos

Para rodar este código, é necessário ter o Python instalado no seu sistema.

- Python 3.x
- Biblioteca `threading` (inclusa no Python padrão)

## Instalação

1. Clone este repositório ou baixe os arquivos.

2. Crie um ambiente virtual e ative-o (se não tiver um ambiente virtual):

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - **Windows**: 
        ```bash
        .\venv\Scripts\activate
        ```
    - **Linux/Mac**:
        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências necessárias:

    - Não há dependências externas além do Python, pois utilizamos apenas a biblioteca `threading`.

## Uso

1. Execute o script principal do barbeiro dorminhoco:

    ```bash
    python barbeiro-dorminhoco.py
    ```

2. O sistema começará a simular a chegada dos clientes e o atendimento do barbeiro. Cada cliente será atendido, ou será descartado se não houver cadeiras disponíveis.

## Explicação do Código

### Semáforos Utilizados

- **semaforoFila**: Controla o número de clientes na sala de espera. Permite até `MAX` clientes simultâneos na sala.
- **semaforoBarbeiro**: Controla a disponibilidade do barbeiro. Se não há clientes, o barbeiro "dorme". Quando um cliente chega, o barbeiro acorda.

### Funções Principais

- **enqueue(cliente)**: Adiciona um cliente à fila de espera. Se a fila estiver cheia, o cliente vai embora.
- **denqueue()**: Remove um cliente da fila e realiza o atendimento. Se não houver clientes, o barbeiro vai dormir.
- **cliente_func(id_cliente)**: Representa o comportamento de um cliente. O cliente aguarda na sala até que haja uma cadeira disponível.
- **barbeiro_func()**: Representa o comportamento do barbeiro, que aguarda por clientes para atender.

### Algoritmo de Funcionamento

1. Quando um cliente chega, ele verifica se há espaço na fila de espera. Se houver, ele se senta e notifica o barbeiro. Caso contrário, ele vai embora.
2. O barbeiro, por sua vez, aguarda que um cliente chegue. Quando um cliente chega, ele o atende e, após o atendimento, verifica se há mais clientes para atender ou se vai dormir.

## Exemplo de Execução

Aqui está um exemplo do que será exibido no terminal ao executar o programa:

    
    O barbeiro termina de cortar o cabelo do cliente 41, que vai embora.
    O cliente 42 senta na cadeira do barbeiro.
    O cliente 45 senta em uma das cadeiras vagas da sala de espera.
    Todas as cadeiras estavam ocupadas, o cliente 46 foi embora.
    O barbeiro termina de cortar o cabelo do cliente 42, que vai embora.
    O cliente 43 senta na cadeira do barbeiro.
    O cliente 47 senta em uma das cadeiras vagas da sala de espera.
    Todas as cadeiras estavam ocupadas, o cliente 48 foi embora.
    O barbeiro termina de cortar o cabelo do cliente 43, que vai embora.
    O cliente 44 senta na cadeira do barbeiro.
    O barbeiro termina de cortar o cabelo do cliente 44, que vai embora.
    O cliente 45 senta na cadeira do barbeiro.



## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para abrir issues e enviar pull requests.

### Passos para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b minha-nova-feature`).
3. Faça o commit das suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Faça o push para a sua branch (`git push origin minha-nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por **Klebson Amarante, Isaac Alves e Mateus Tomaz**.
