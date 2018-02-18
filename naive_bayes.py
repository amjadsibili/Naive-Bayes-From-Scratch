import math
import re


try :
	
	training_data_label_1 = open('train1.txt', 'r').read()
	training_data_label_2 = open('train2.txt', 'r').read()

	test_data = open('test.txt', 'r')

except IOError :

	print 'Data not found !'
#######Training of Naive Byes classifier goes here#######

prior_probability_label_1 = 0.5
prior_probability_label_2 = 0.5




_training_data_label_1 = re.sub('[^a-zA-Z0-9 \n\.]', '', training_data_label_1).decode('utf-8').lower()
_training_data_label_2 = re.sub('[^a-zA-Z0-9 \n\.]', '', training_data_label_2).decode('utf-8').lower()

_training_data_label_1_max = len(_training_data_label_1) 
_training_data_label_2_max = len(_training_data_label_2) 


def get_net_occurance_probabilities(weighted_table, occurance_list, prior_probability) :

	prod = prior_probability

	for occurance in occurance_list :

		occurance_list = [x for x in occurance_list if x != occurance]
		prod *= weighted_table[occurance]

	return prod



def get_frequency_table(training_data) :

	dict_temp = {}
	training_data = training_data.split(' ')

	for i in training_data :

		dict_temp[i] = 0

		for j in training_data :

			if i == j :

				dict_temp[i] += 1

	return dict_temp


frequency_table_label_1 = get_frequency_table(_training_data_label_1)
frequency_table_label_2 = get_frequency_table(_training_data_label_2)

def get_weighted_table(frequency_table, max_count) :

	_dict = {}

	total = 0

	for obj in frequency_table :

		total += frequency_table[obj]

	
	for obj in frequency_table :

		_dict[obj] = float(frequency_table[obj]) / total
	

	return _dict


weighted_table_label_1 = get_weighted_table(frequency_table_label_1, _training_data_label_1_max)
weighted_table_label_2 = get_weighted_table(frequency_table_label_2, _training_data_label_2_max)


	#######Training ends#######

#######Testing starts######



inv_weighted_table_label_1 = {v: k for k, v in weighted_table_label_1.iteritems()}
inv_weighted_table_label_2 = {v: k for k, v in weighted_table_label_2.iteritems()}


_test_data = test_data.read()

__test_data = _test_data.split(' ')


occured_words_label_1 = []
occured_words_label_2 = []


for i in __test_data :

	for j in _training_data_label_1.split(' ') :

		if i == j :

			occured_words_label_1.append(i)


for i in __test_data :

	for j in _training_data_label_2.split(' ') :

		if i == j :

			occured_words_label_2.append(i)


for word in __test_data :

	try :
		prior_probability_label_1 *= weighted_table_label_1[word]
		prior_probability_label_2 *= weighted_table_label_2[word]

	except KeyError :

			print ''


print prior_probability_label_1
print prior_probability_label_2

_prior_probability_label_1 = (prior_probability_label_1 / (prior_probability_label_1 + prior_probability_label_2)) * 100
_prior_probability_label_2 = (prior_probability_label_2 / (prior_probability_label_1 + prior_probability_label_2)) * 100

print 'Results :\n Label 1 : ',_prior_probability_label_1,'%\nLabel 2 : ',_prior_probability_label_2,'%'
