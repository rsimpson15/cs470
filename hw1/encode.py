
#Solution partially credited to hltbra: https://gist.github.com/hltbra/4117933
def encode(input_string):
     if not input_string: 
          return ""
     else:
          last_char = input_string[0]
          max_index = len(input_string)
          i = 1
          while i < max_index and last_char == input_string[i]:
               i += 1
          result_string = last_char + str(i) + encode(input_string[i:])
          if len(result_string) == len(input_string):
               return input_string
          return result_string


   
