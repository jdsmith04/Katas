def cut_ends_off(string: str):
    if len(string) <= 2:
        return 'Your string is too short'
    else:
        return string[1:-1]


print(cut_ends_off('monopoly'))
print(cut_ends_off(''))
print(cut_ends_off('l'))
print(cut_ends_off('jk'))
print(cut_ends_off('abc'))
