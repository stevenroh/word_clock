from constants import COMMANDS
import os

INVALID_TASK = "Invalid task"

class IOTUtils():
  def execute_if_valid(self, task):
    command = COMMANDS.get(task, INVALID_TASK)

    if command is not INVALID_TASK:
        os.system(command)
        return True

    return False