'''A program to display how to manipulate files in python'''

from pathlib import Path

path = Path.cwd()
babylon = Path(f'{path}/8_files/the_richest_man_in_babylon.txt')
babylon_update = Path(f'{path}/8_files/text_files/the_richest_man_in_babylon_upda'
                      'ted.txt')
babylon_content = babylon.read_text()
babylon_content = (babylon_content.replace('[15]', ''))
babylon_content = (babylon_content.replace('[2]', ''))
babylon_content = (babylon_content.replace('[3]', ''))

# print(babylon_content)
babylon_tmp = ''
for line in babylon_content.splitlines():
    print(f'\n{line}\n')
    babylon_tmp += '\n' + line + '\n'

babylon_update.write_text(babylon_tmp)

# print(len(babylon_content.splitlines()))
