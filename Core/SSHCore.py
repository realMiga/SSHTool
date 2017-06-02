import paramiko

"""

@Setup Environment:
    python2 -m pip install paramiko -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    python3 -m pip install paramiko -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

@Run:
    python2 pyssh.py
    python3 pyssh.py

"""

HOST = "10.0.0.94"
PORT = 22
USER = "cc"
PASSWORD = "wahaha"

KEY_FILE = None


raw_input = input


class SSHResult:
    stdin = None
    stdout = None
    stderr = None
    Suc = False

    def __init__(self):
        pass

    def showResult(self):
        if self.stdout:
            for line in self.stdout:
                print(line[:-1])

    def showError(self):
        if self.stderr:
            for line in self.stderr:
                print(line[:-1])

    def getResult(self):
        if self.stdout:
            return self.stdout
        else:
            return None

    def getError(self):
        if self.stderr:
            return self.stderr
        else:
            return None

    def initData(self):
        self.stdout = self.stdout.readlines()
        self.stderr = self.stderr.readlines()


class SSHClient:

    BLACK_LIST_COMMAND = [
        'sudo', 'su', 'vi', 'passwd', 'gdb', 'mysql', 'do',
        'gedit', 'emacs', 'vim',
        'python', 'python3', 'python2', 'ruby', 'ipython', 'ipython3', 'zsh', 'sh', 'bash'
    ]

    def __init__(self, host, port, user, password=None, key=None):
        self.client = paramiko.SSHClient()

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.key = key
        self.turnOnAutoPolicy()

        if self.user == 'root':
            self.curPath = '/root'
        else:
            self.curPath = '/home/' + self.user
        self.homePath = self.curPath
        self.prePath = None

    def connect(self):
        if self.key is not None:
            self.client.connect(self.host, self.port, self.user, key_filename=self.key, timeout=5)
        else:
            self.client.connect(self.host, self.port, self.user, self.password, timeout=5)
        return self

    def turnOnAutoPolicy(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return self

    def quit(self):
        self.client.close()

    def isHasPath(self):
        if self.curPath is not None:
            return True
        else:
            return False

    def changePath(self, path):
        self.prePath = self.curPath
        self.curPath = path

    def download(self, remotePath, localPath):
        r = SSHResult()
        sftp = self.client.open_sftp()
        filename = remotePath.split("/")[-1]
        try:
            sftp.get(remotePath, localPath + filename)
            r.Suc = True
        except Exception as e:
            r.Suc = False
            r.stderr = e
        sftp.close()
        return r

    def upload(self, localPath, remotePath):
        r = SSHResult()
        sftp = self.client.open_sftp()
        filename = localPath.split("/")[-1]
        try:
            sftp.put(localPath, remotePath + "/" + filename)
            r.Suc = True
        except Exception as e:
            r.Suc = False
            r.stderr = e
        sftp.close()
        return r

    def run(self, cmd=None):
        if cmd is None:
            prompt = '%s@%s:%s$ ' % (self.user, self.host, self.curPath)
            try:
                command = raw_input(prompt)
            except EOFError as e:
                print(e)
                command = ''

            if command == 'exit':
                self.quit()
                exit()
        else:
            command = cmd

        r = SSHResult()

        if command.split(" ")[0] in self.BLACK_LIST_COMMAND:
            r.Suc = False
            r.stderr = 'Black List Command:\n' + ", ".join(self.BLACK_LIST_COMMAND) + "\n"
            return r

        command = 'cd %s; %s' % (self.curPath, command)

        r.stdin, r.stdout, r.stderr = self.client.exec_command(command)
        r.initData()

        if len(r.stderr) == 0:
            meta = command.split('cd')
            if len(meta) == 3:
                tPath = meta[2][1:].strip()
                if tPath[0] == '/':
                    self.changePath(command.split('cd')[2][1:])
                else:
                    if tPath == '~':
                        self.changePath(self.homePath)
                    elif tPath == '..':
                        p = '/'.join(self.curPath.split('/')[:-1])
                        self.changePath(p if p else '/')
                    elif tPath == '.':
                        pass
                    elif tPath == '-':
                        if self.prePath is not None:
                            self.changePath(self.prePath)
                    elif self.curPath is not '/':
                        self.changePath(self.curPath + '/' + tPath)
                    else:
                        self.changePath(self.curPath + tPath)
            r.Suc = True
        return r



if __name__ == '__main__':
    client = SSHClient(HOST, PORT, USER, PASSWORD)
    # client.connect()
    # # client.turnOnAutoPolicy().connect()
    # # lPath = 'D:/SSHToolkit/main.py'
    # # rPath = '/tmp/'
    # # r = client.upload(remotePath=rPath, localPath=lPath)
    # # if not r.Suc:
    # #     print(r.getError())
    # while True:
    #     try:
    #         r = client.run()
    #     except KeyboardInterrupt:
    #         continue
    #     if r.Suc:
    #         r.showResult()
    #     else:
    #         r.showError()
