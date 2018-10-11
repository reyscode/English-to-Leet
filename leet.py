import requests
import random

leet_file_path = 'https://gist.githubusercontent.com/suriyadeepan/4ce867a382a50ea8fbddeba4468337d0/raw/636346fc56c7d15344cc42a3f78e28d2c8744542/leet.txt'

def read_file_from_web(url):
  return requests.get(url).text

def create_lookup(filename):
  lookup_dict={}
  content = read_file_from_web(filename)
  list_of_contents=content.split('\n') 

  for line in list_of_contents: 
    key = line[0]
    remaining = line[2:]
    remaining_values=remaining.replace(' ','').split(',')
    lookup_dict[key]=remaining_values

  return lookup_dict 

def translate(message, lookup): 
  final_str=''
  for letter in message:
    if letter in lookup: 
      replace_list=lookup[letter]
      replace_char=random.choice(replace_list)
      final_str=final_str+replace_char
    else:
      final_str=final_str+letter

  return final_str

def encrypt(): 
  input_message=input("Enter message: ")
  input_message=input_message.upper() 
  lookup_dict_1=create_lookup(leet_file_path)
  final_message=translate(input_message,lookup_dict_1)
  return final_message

if __name__ == '__main__':
  # this is like your main function
  print(encrypt())
