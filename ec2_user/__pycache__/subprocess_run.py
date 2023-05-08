"""pode usar o módulo subprocess para gerar novos processos, 
conectar-se a pipes de entrada/saída/erro e obter códigos de erro. 
A função subprocess.run() pode aceitar muitos novos argumentos, 
mas esses argumentos adicionais são opcionais.
A lista completa de argumentos de subprocess.run() é semelhante a esta:
subprocess.run(args, *, stdin=None, input=None, stdout=None, 
stderr=None, capture_output=False, 
shell=False, cwd=None, timeout=None, 
check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
Neste laboratório, o código será simples.
No arquivo que você criou para este laboratório, 
importe o módulo subprocess:"""

import subprocess

#Para executar o comando Bash ls, insira o seguinte comando:

#subprocess.run(["ls"])

"""No Python, os colchetes são tipos de dados de listas, o que significa que run() pode aceitar uma lista de argumentos. Continue fazendo adições ao script Python.

No arquivo de laboratório deste exercício, 
modifique a linha final do script e 
inclua um argumento adicional:
subprocess.run(["ls","-l"])"""

#subprocess.run(["ls","-l"])

"""Agora você chamará subprocess.run() com três argumentos. 
O terceiro argumento será o nome de um diretório.
Volte para o arquivo do Python e modifique a linha final do script:"""

#subprocess.run(["ls","-l","README.md"])

"""O "-l" é um argumento que diz ao comando ls para usar um formato de listagem longa.

Salve o arquivo no IDE Cloud 9 e selecione Run (Executar)  para executar o arquivo novamente.

Confirme se a saída é semelhante ao exemplo a seguir.

total 12
-rw-r--r-- 1 ec2-user ec2-user  55 Apr 16 20:20 sys-admin.py
-rw-r--r-- 1 ec2-user ec2-user 343 Apr 16 19:07 sys-admin_2.py
-rw-r--r-- 1 ec2-user ec2-user 569 Apr  6 02:17 README.md"""

"""uso do subprocess.run com três argumentos
Agora você chamará subprocess.run() com três argumentos. 
O terceiro argumento será o nome de um diretório.
Volte para o arquivo do Python e modifique a linha final do script:

subprocess.run(["ls","-l","README.md"])

Salve o arquivo no IDE Cloud 9 e selecione Run (Executar)  para executar o arquivo.
Confirme se a saída esperada é semelhante ao exemplo a seguir.
-rw-r--r-- 1 ec2-user ec2-user 569 Apr  6 02:17 README.md

"""

"""ercício 5: recuperação de informações do sistema
A função subprocess.run() é poderosa porque permite que você execute qualquer comando Bash. Neste exercício, você chamará o comando uname para obter informações do sistema.

Volte para o arquivo do Python e insira o seguinte código:
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

Salve o arquivo no IDE Cloud 9 e selecione Run (Executar)  para executar o arquivo.
Confirme se a saída esperada é semelhante ao exemplo a seguir.

Gathering system information with command: uname -a                          
Linux ip-172-31-29-181 4.4.0-139-generic #165-Ubuntu SMP Wed Oct 24 10:58:50
UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
"""


"""Para enfatizar que subprocess.run() permite a execução de 
qualquer comando, você executará o comando df para obter informações de disco.
Volte para o arquivo do Python e insira o seguinte código:

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

Salve o arquivo no IDE Cloud 9 e selecione Run (Executar)  para executar o arquivo.

Confirme se a saída esperada é semelhante ao exemplo a seguir.

Gathering active process information with command: ps -x                       
  PID TTY      STAT   TIME COMMAND                                           
18976 pts/459  S+     0:00 python3.6 lab_15_2.py                               
18977 pts/459  R+     0:00 ps -x                                             
21139 pts/459  S      0:00 /bin/bash -c export OLD_HOME=/home/ccc_4dfa91ec5a_
21164 pts/459  S      0:00 bash --rcfile /home/ccc_4dfa91ec5a_45122/.termrc
"""

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

