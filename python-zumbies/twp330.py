def ip_valido(ip):
    ip = ip.split('.')

    for num in ip:
        if int(num) > 255:
            return False
    return True

arquivo_ips = open('IPS.txt')
ips_validos = open('ips_validos.txt', 'w')
ips_invalidos = open('ips_invalidos.txt', 'w')

for ip in arquivo_ips.readlines():
    if ip_valido(ip):
        ips_validos.write(ip)
    else:
        ips_invalidos.write(ip)

arquivo_ips.close()   
ips_validos.close()            
ips_invalidos.close()            
          

    