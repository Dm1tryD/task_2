  for num in range(11,78):
    word = ''
    if num % 3 == 0:
        word+='$$'
    if num % 5 == 0:
        word+='@@'
    if word != '':
        print(word)
