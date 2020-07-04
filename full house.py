full = ['10', 'J', '10', '10', '10']
#full = ['A', 'A', 'A', 'K', 'K']
#full = ['', 'J', 'J', '3', '3']
def is_full_house(full):
    one_char = full.count(full[1])
    two_char = full.count(full[-1])
    if(1 < one_char < 4) and (1 < two_char < 4):
        return True
    else:
        return False

print(is_full_house(full))