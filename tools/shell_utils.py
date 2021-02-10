import subprocess


def run_shell_command(command):
    cmd = "{}".format(command).split()
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout
    except subprocess.CalledProcessError as e:
        print(e)
        print('Unable to run {}'.format(command))
        exit(1)
