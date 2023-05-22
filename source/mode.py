"""
mode.py
=======
The core module of the example project.
"""
# mode.py
from collections import Counter

def mode(data):
  """
  Return a mode

  Parameters
  ----------
  data
    input data
  """
  counter = Counter(data)
  _, top_count = counter.most_common(1)[0]
  return [point for point, count in counter.items() if count == top_count]
