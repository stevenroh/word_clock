from threading import current_thread
from constants import MATRIX_WIDTH

LINES_TO_INVERT  = [0, 2, 4, 6, 8]

def prepare_matrix(arr):
  new_arr = []

  for item in arr:
    current_line = item // MATRIX_WIDTH
    if current_line in LINES_TO_INVERT:
      new_value = MATRIX_WIDTH * (current_line + 1) - item
      # print("invert " + str(current_line) + " change " + str(item) + " with " + str(new_value))
      new_arr.append(new_value)
    else:
      new_arr.append(item)
  
  return new_arr