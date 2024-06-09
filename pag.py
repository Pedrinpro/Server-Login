import subprocess
import sqlite3
import ctypes

def execute_as_admin(command):
    try:
        # Chama ShellExecute com o comando 'runas' para solicitar privilégios de administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", command, None, None, 1)
    except Exception as e:
        print("Erro ao solicitar permissões de administrador:", e)


def verify(usuario, senha):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('Data.db')
    cursor = conn.cursor()

    # Executa a consulta SQL para selecionar a senha do usuário fornecido
    cursor.execute("SELECT pss FROM login WHERE usr = ?", (usuario,))
    
    # Recupera a senha do usuário (se existir)
    resultado = cursor.fetchone()

    # Verifica se o usuário foi encontrado no banco de dados
    if resultado:  # Se um resultado foi encontrado
        senha_armazenada = resultado[0]  # A senha é o primeiro elemento da tupla resultado
        # Verifica se a senha fornecida corresponde à senha armazenada
        if senha == senha_armazenada:
            print("Senha correta. Acesso concedido.")
        else:
            print("Senha incorreta. Acesso negado.")
            exit()
    else:
        print("Usuário não encontrado.")
        exit()

print("""
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░░░░░░░██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░░░░██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝█████╗██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗╚════╝██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║░░░░░░███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░░░░╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝""")
N = input("$_USR: ")
P = input("$_SNH: ")
verify(N,P)

if N == 'admin' or N == 'root':
    execute_as_admin("cmd.exe")
elif N == 'user':
    while True:
        Comando_NaoADM_NaoROOT = input("$_")
        if Comando_NaoADM_NaoROOT.lower() == 'exit':
            print('Fechando...')
            exit()
        else:
            resultado = subprocess.run(Comando_NaoADM_NaoROOT, shell=True, capture_output=True, text=True)
            if resultado.returncode == 0:
                # Se não houver erro, imprime a saída padrão
                print("Saída do comando:")
                print(resultado.stdout)
            else:
                # Se houver erro, imprime a saída de erro
                print("Erro ao executar o comando:")
                print(resultado.stderr)
else:
    print("Usuário não reconhecido.")
