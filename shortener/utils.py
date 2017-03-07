import string
import random


def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):
#     new_code =''
#     for _ in range(size):
#         new_code += random.choice(chars)
#     return new_code
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size = 6):
    new_code = code_generator(size = size)
#     print(instance)
#     print(instance.__class__)
#     print(instance.__class__.__name__)
    Klass = instance.__class__
    if Klass.objects.filter(shortcode = new_code).exists():
        return create_shortcode(instance, size = 6)
    return new_code