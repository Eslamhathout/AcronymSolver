from google import google
from nltk.tokenize import word_tokenize
import itertools
import operator


def acronyms_solver(acronym):
	try:
		acronyms= acronym
		# This function calculates the most repeted item in the possible ssentences list.
		def most_common(L):
		  SL = sorted((x, i) for i, x in enumerate(L))
		  groups = itertools.groupby(SL, key=operator.itemgetter(0))
		  def _auxfun(g):
		    item, iterable = g
		    count = 0
		    min_index = len(L)
		    for _, where in iterable:
		      count += 1
		      min_index = min(min_index, where)
		    return count, -min_index
		  return max(groups, key=_auxfun)[0]


		search_results = google.search(acronyms, 4)

		all_names=[] #All searching names
		all_descriptions= [] #All searching descriptions

		for n in search_results[0:10]:
			result_name= []
			result_description= []

			result_name= n.name
			result_description= n.description

			all_names.append(result_name)
			all_descriptions.append(result_description)



		#print all_names
		#print all_descriptions

		possible_correct= [] #allpossible correct acronyms.
		for i in range (0,10):
			words_zero= word_tokenize(all_names[i])

			first=-1
			second=-1

			for (i, word) in enumerate(words_zero):
				if word.startswith(acronyms[0]) and word != acronyms:
					if first == -1:
						first = i
				elif word.startswith(acronyms[-1]):
					if second == -1:
						second= i
				else:
					continue

			if first<second:
				possible_correct.append(words_zero[first:second+1])
			else:
				pass


		for i in range (0,10):
			words_zero= word_tokenize(all_descriptions[i])

			first=-1
			second=-1

			for (i, word) in enumerate(words_zero):
				if word.startswith(acronyms[0]) and word != acronyms:
					if first == -1:
						first = i
				elif word.startswith(acronyms[-1]):
					if second == -1:
						second= i
				else:
					continue

			if first<second:
				possible_correct.append(words_zero[first:second+1])
			else:
				pass

		the_right_acronym= most_common(possible_correct)
		the_output_acronm= ""
		for word in the_right_acronym:
			the_output_acronm += word + " "
		return the_output_acronm.lower()
	except:
		return acronym







print acronyms_solver("CTO")




