class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, a = []):

        array = []

        # Step 1: split object name into chars
        sok = ''.join(sorted(self.word))

        # Step 2:  iterate  through each element in list, for each, compare by sorting.
        for i in a:
            if(sok == ''.join(sorted(i))):
                array.append(i)
        return array
