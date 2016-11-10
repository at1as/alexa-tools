import re

"""
given input string with multiple choices inserted between '<' and '>' brackets
return all posibilities. Split options around pipe:
  <a|b>  => 'a', 'b'
  <a|b|> => 'a', 'b', ''


Ex. '<good morning|good evening> this is <a test|not a test>'
  => good morning this is a test
  => good morning this is not a test
  => good evening this is a test
  => good evening this is not a test

Useful for building Amazon
"""

output_text = []
input_text = "<get|fetch|retrieve> <me||for me> the <{postNum}|> <last|lastest|most recent> <audio|> <post|blog post|entry|blog entry|item|blog item>"

def balanced_parenthesis(input_str):
  # Ensure equal opening '<' and closing '>' braces
  if len(re.findall('<', input_str)) != len(re.findall('>', input_str)):
    raise Exception('Unbalanced brackets "<" and ">"')

def extract_choices(input_str):
  # From '... <choice1|choice2> ...' extract ['choice1|choice2']
  return re.findall("\<([^\>]*)\>", input_str)

def remove_choices(input_str):
  # Replace '<choice1|choice2>' with '<>' in text string
  return re.sub("(\.*)\<([^\>]*)\>(\.*)", "<>", input_str)

def split_choices(choice_list):
  # split 'choice1|choice2' into list ['choice1', 'choice2']
  for idx, i in enumerate(choice_list):
    choice_list[idx] = i.split('|')

  return choice_list


def expand_choices(input_str, options, level=0):
  for x in options[level]:
    replaced_str = input_str.replace('<>', x, 1)

    if len(re.findall('<', replaced_str)) != 0:
      expand_choices(replaced_str, options, level + 1)
    else:
      output_text.append(replaced_str)


def print_results(list_of_results):
  for output_str in list_of_results:
    print ' '.join(output_str.split())

balanced_parenthesis(input_text)
choices = extract_choices(input_text)
choices = split_choices(choices)
stripped_text = remove_choices(input_text)
expand_choices(stripped_text, choices)

print_results(output_text)
