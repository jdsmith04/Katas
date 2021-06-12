def cut_ends_off(string: str):
    if len(string) <= 2:
        print('Your string is too short')
    else:
        return string[1:-1]


word = cut_ends_off('monopoly')
print(word)
