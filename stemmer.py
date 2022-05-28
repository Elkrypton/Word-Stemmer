
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer





porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')



def PorterStemming(word):
	stemmed = porter.stem(word)
	print("[PORTER STEMMER]:{}".format(stemmed))

def LancasterStemming(word):
	stemmed = lancaster.stem(word)
	print("[LANCASTER STEMMER]:{}".format(stemmed))

def SnowballStemming(word):
	stemmed = snowball.stem(word)
	print("[SNOWBALL STEMMER]:{}".format(stemmed))
	



#print("\n" ,formatted_text.format('INPUT WORD',* stemmer_names))


#for word in input_words:

 #   output = [word,porter.stem(word),
  #          lancaster.stem(word),
   #         snowball.stem(word)]
#
 #   print(formatted_text.format(*output))
    
def main():
	print("""
	Welcome to the Morphology Tool
	---- "Make it root!"-----
	
	1 - Porter Stemmer
	2 - Lancaster
	3 - Snowball
	4 - Use All Stemmers for my word
	5 - Exit
	""")
	STATE = True
	while STATE:
		word = input("<<WORD>>:")
		choice = int(input("<<CHOICE>>:"))
		if choice == 1:
			PorterStemming(word)
		elif choice == 2:
			LancasterStemming(word)
		elif choice == 3:
			SnowballStemming(word)
		elif choice == 4:
			PorterStemming(word)
			LancasterStemming(word)
			SnowballStemming(word)
			
		elif choice == 5:
			sys.exit("[!] Goodbye...")

if __name__ == "__main__":
	main()
		
		
		
		
		
