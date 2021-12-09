import os

COMMANDS = {
    'poweroff': 'shutdown -h now',
    'reboot': 'reboot',
    'test': 'echo test > /tmp/test.txt',
    'on': '',
}

INVALID_TASK = "Invalid task"

def execute_if_valid(task):
    command = COMMANDS.get(task, INVALID_TASK)

    if command is not INVALID_TASK:
        os.system(command)
        return True

    return False