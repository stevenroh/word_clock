from constants import MATRIX_WIDTH

LINES_TO_INVERT = []

def get_fixed_led_id(id):
  current_line = id // MATRIX_WIDTH

  if current_line in LINES_TO_INVERT:
    return (MATRIX_WIDTH * (current_line + 1)) - id
  
  return id