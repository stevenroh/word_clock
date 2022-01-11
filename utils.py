from constants import MATRIX_WIDTH

LINES_TO_INVERT = [1, 3, 5, 7, 9]

def get_fixed_led_id(identifier):
  current_line = identifier // MATRIX_WIDTH

  if current_line in LINES_TO_INVERT:
    start_of_line = current_line * 11
    return start_of_line + (MATRIX_WIDTH - (identifier % start_of_line)) - 1
  
  return identifier