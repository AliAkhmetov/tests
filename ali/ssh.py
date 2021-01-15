### Импортируются необходимые библиотеки
import paramiko
import time
import datetime
import sys
import re
import os
import socket
import base64

### Задаются исходные параметры
user = 'root'

#secret= pas = base64.b64decode(b'cGFzc3dvcmQ=').decode('ascii') # совсем не надежно зашифрованный пароль, но хоть что то. Для получения зашифрованного пароля
# необходиом предварительно выполнить base64.b64encode('password'.encode('ascii'))'''
port = por = 22
host='192.168.2.47'

### используется модуль paramiko для установления соединения получения результата с оборудования:
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ### всегда доверяется SHA ключам
remote_conn_pre.connect(hostname=host, username=user, password='Nir41vana', port=por, timeout=90) ### устанавливается соединение используя заданные параметры
remote_conn = remote_conn_pre.invoke_shell() ### сессия постоянно поддерживается до принудительного завершения, либо по истечении времени жизни
remote_conn.settimeout(20) ### через 20 sec при отсутствии активности сессия будет разорвана
remote_conn.send ('\n') ### 'Enter' для проверки работоспособности
time.sleep(1) ### приостановка выполнения скрипта на 1 секундувышеописанная функция с присвоением значения переменной check, переводим значение переменной в строковый
# тип данных str()
stdin, stdout, stderr = remote_conn_pre.exec_command('lsblk')
res = []
for line in stdout:
    res.append(line.strip('\n'))
    print( line.strip('\n'))
remote_conn.close()

print('---------', res)

remote_conn_pre.close() ### SSH сессия с оборудованием больше не требуется.
