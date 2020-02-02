def consecutive(tekst,znak):
    longest_counter=0
    counter=0
    for s in tekst:
        if s == znak:
            counter+=1
        else:
            longest_counter=max(counter,longest_counter)
            counter = 0
    longest_counter = max(counter, longest_counter)
    return longest_counter

def test_consecutive():
    assert consecutive("aabbbaabbbb","b") == 4
    assert consecutive("aabbbbbaabbbaa", "b") == 5