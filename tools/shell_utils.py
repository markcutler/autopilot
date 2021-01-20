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
