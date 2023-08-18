from PyPDF2 import PdfReader
import re
  
# creating a pdf reader object
reader = PdfReader('/home/kevinnguyen1413/Desktop/raw_fruits.pdf')
  
# printing number of pages in pdf file
print(len(reader.pages))
  
# getting a specific page from the pdf file
page0 = reader.pages[0]
page1 = reader.pages[1]
# extracting text from page
text0 = page0.extract_text()
text1 = page1.extract_text()

text2 = text0 + text1


fruit_list = re.findall(r'\b[A-Z].*?\b', text2)
fruit_calories = re.findall(r'\)\d\d', text2)
fruit_calories = [cal.replace(')', '') for cal in fruit_calories]

print(fruit_list)
print(fruit_calories)