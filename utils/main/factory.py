from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt-BR')

def make_question():
    return {
        'title': fake.sentence(nb_words=6),
        'question_text': fake.sentence(nb_words=50),
        'created_at': fake.date_time(),
        'modified_at':fake.date_time(),
        'author': {
            'first_name':fake.first_name(),
            'last_name':fake.last_name(nb_letters=1)
        },
        'tag': {
            'name': fake.word()
        },
        'photo': {
            'url': 'https://loremflickr.com/%s/%s/food, cook' %rand_ratio(),
        }
    }