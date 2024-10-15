def single_root_words(root_word, *other_words):
    # same words как бы сразу возвращается, реши не создавать переменную,
    # а написатm однострочную функцию, надеюсь так можно
    return [word for word in other_words if word.lower() in root_word.lower() or root_word.lower() in word.lower()]
   
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
