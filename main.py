def main():
   with open("./books/frankenstein.txt", 'r') as f:
      file_contents = f.read()
      wc = len(file_contents.split())
      cc = count_chars(file_contents)
      print(f"""
      --- Begin report of books/frankenstein.txt ---
      {wc} words found in the document
      """)

      for k,v in cc.items():
         if k.isalpha():
            print(f"The '{k}' character was found {v} times")

def count_chars(f):
   f = f.lower()
   f = list(f)
   result = dict()
   for c in f:
      if c not in result:
         result[c] = 1
         continue

      result[c] += 1
   
   return result


if __name__ == "__main__":
   main()