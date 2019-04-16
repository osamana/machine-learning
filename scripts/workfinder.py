import re

word_list = [u'', u'']

def get_occurrences(word, text):
    occ_list = [m.start() for m in re.finditer(word, text)]
    return len(occ_list)

print(get_occurences(u'ممتاز', text))


"""
what is needed:
we need to get the occurrence of each word in the list of words above in
each review for each hotel

pseudo code:
create a new field on Hotel > word_ocr (json)
word_list = ['word1', 'word2' , ...etc]
for hotel in hotels:
    word_ocr = {}
    for word in word_list:
        word_counter = 0
        for review in hotel.reviews:
            count = get_occurrence(word, review.text)
            word_counter += count
        word_ocr[word] = word_counter
    hotel.word_ocr = word_ocr
    hotel.save()
            
            


"""


