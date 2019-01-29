import secrets

# word list from first20hours github repo
# 10,000 most common English words in order of frequency, as determined by n-gram frequency analysis of the Google's Trillion Word Corpus
def get_word_list():
    word_list = []
    with open("google-10000-english-usa-no-swears-medium.txt") as words_txt:
        for word in words_txt:
            word_list.append(word.strip())
    return word_list;

def test_word_list():
    words = get_word_list()
    for word in words:
        print(word)
#test_word_list()

def gen_random_num():
    random_int = secrets.randbelow(10)
    return random_int;

def gen_random_word():
    word_list = get_word_list()
    random_int = secrets.randbelow(len(word_list))
    return word_list[random_int];
print("random word: " + gen_random_word())