line = input()

line = line.replace(' ', '')
line = line.replace('⋅', '∙')
line = line.replace('∙', '∙')
line = line.replace('·', '∙')
line = line.replace('−', '–')
line = line.replace('—', '–')
line = line.replace('-', '–')
line = line.replace('∙', ' ∙ ')
line = line.replace('–', ' – ')
line = line.replace('+', ' + ')

web_line = line
print(web_line)

line = line.replace('</sup>', '')
line = line.replace('<sup>', '**')
line = line.replace(' ∙ ', '∙')
line = line.replace(' ∙ ', '*')
line = line.replace('∙', '*')
line = line.replace('–', '-')

print(line)
