import subprocess


def run_shell_command(command):
    command_split = "{}".format(command).split()
    try:
        process = subprocess.run(command_split,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True,
                                 shell=True,
                                 check=False)
        return process.stdout
    except subprocess.CalledProcessError as e:
        print("Warning: " + str(e))
        exit(1)


def run_output_list(bash_cmd):
    cmd = "{}".format(bash_cmd).split()
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout
    except Exception as e:
        print(e)
        print('Unable to run {}'.format(bash_cmd))
        exit(1)