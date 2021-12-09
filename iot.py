import os
from observer import Subscriber

COMMANDS = {
  'poweroff': 'shutdown -h now',
  'reboot': 'reboot',
  'test': 'echo test > /tmp/test.txt',
}

INVALID_TASK = "Invalid task"

class IOTUtils(Subscriber):
  def execute_if_valid(self, task):
    command = COMMANDS.get(task, INVALID_TASK)

    if command is not INVALID_TASK:
        os.system(command)
        return True

    return False

  def update(self, message):
    print("IOTUtils receive message : " + message)