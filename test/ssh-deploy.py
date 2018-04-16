import paramiko

# 通过ssh连接阿里云,并进行操作,可以作为自动部署
def ssh(sys_ip,username,password,cmds):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(sys_ip,22,username=username,password=password,timeout=20)
        results = []
        for cmd in cmds:
            stdin,stdout,stderr = client.exec_command(cmd)
            results.append(stdout.readlines())
        return results
    except Exception as e:
        print(e)
    finally:
        client.close()

if __name__ == '__main__':
    username = 'root'
    password = 'Malian9531!'
    sys_ip = '119.23.251.136'
    cmds = ['pwd','ls']
    results = ssh(sys_ip,username,password,cmds)
    print(results)
    pass