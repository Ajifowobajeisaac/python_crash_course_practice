"""Demonstrates the use of Json"""

from pathlib import Path
import json

even_numbers = []

for i in range(0, 50, 2):
    even_numbers.append(i)


path = Path('numbers.json')
content = json.dumps(even_numbers)
path.write_text(content)
