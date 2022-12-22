word1 = ['t','e','t']
word2 = ['t','e','i']
# test if user has on won the game
def test_if_complete(word1,word2):
    if word1 == word2 :
        return True
    else :
        return False
    
if test_if_complete(word1,word2) :
    print("true")

