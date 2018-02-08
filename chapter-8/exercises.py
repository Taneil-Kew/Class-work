import sys
import string


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
'''
#ex 3
def count_letters(string,ltr):
    count = 0
    repeats =0
    while repeats < len(string):
        str_index = string.find(ltr,repeats, repeats+1)
        if string.find(ltr,repeats, repeats+1)>=0:
            count+=1
        repeats += 1
     return count
print(count_letters("bananaa","b"))
'''

#ex 4
def count_letters(word,ltr):
    count = 0
    repeats=0
    while repeats < len(word):
        str_index = word.find(ltr,repeats,repeats+1)
        if str_index >= 0:
            count +=1
        repeats +=1

    return count
print(count_letters("banana","a"))
#ex 5
def analyze(str):
    s_without_punct = ""
    for letter in str:
        if letter not in string.punctuation:
            s_without_punct += letter
    mylist=s_without_punct.split()
    count = 0
    for i in mylist:
        if i.find("e")>=0:
            count+=1
    numwords = len(mylist)
    percentage = count / numwords *100

    return 'Your text contains {0} words, of which {1} ({2:.2f}%) contain an "e".'.format(numwords,count,percentage)

speech=""""Once more unto the breach, dear friends, once more;
Or close the wall up with our English dead.
In peace there's nothing so becomes a man
As modest stillness and humility:
But when the blast of war blows in our ears,
Then imitate the action of the tiger;
Stiffen the sinews, summon up the blood,
Disguise fair nature with hard-favour'd rage;
Then lend the eye a terrible aspect;
Let pry through the portage of the head
Like the brass cannon; let the brow o'erwhelm it
As fearfully as doth a galled rock
O'erhang and jutty his confounded base,
Swill'd with the wild and wasteful ocean.
Now set the teeth and stretch the nostril wide,
Hold hard the breath and bend up every spirit
To his full height. On, on, you noblest English.
Whose blood is fet from fathers of war-proof!
Fathers that, like so many Alexanders,
Have in these parts from morn till even fought
And sheathed their swords for lack of argument:
Dishonour not your mothers; now attest
That those whom you call'd fathers did beget you.
Be copy now to men of grosser blood,
And teach them how to war. And you, good yeoman,
Whose limbs were made in England, show us here
The mettle of your pasture; let us swear
That you are worth your breeding; which I doubt not;
For there is none of you so mean and base,
That hath not noble lustre in your eyes.
I see you stand like greyhounds in the slips,
Straining upon the start. The game's afoot:
Follow your spirit, and upon this charge
Cry 'God for Harry, England, and Saint George!'
"""
#print(analyze(speech))

#Problem 7


def reverse(word):
    reversed = ""
    for i in range(len(word) -1, -1, -1):
        reversed += word[i]
    return reversed

""""
test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")
"""
#Problem 9 one way

""""
def remove_letter(char,text):
    charremovedtext = ""
    for letter in text:
        if letter != char:
            charremovedtext += letter
    return charremovedtext
"""


#Problem 9 another way
def remove_letter(letter, word):
    count = 0
    new_word = ""
    for i in word:
        if i != letter:
            new_word += word[count:count+1]
        count += 1
    return new_word
""""
print("remive_letter",remove_letter("a","banana"))

test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")
"""
#ex 5


layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>10}{5:>10}{6:>10}{7:>10}{8:>10}{9:>10}{10:>10}{11:>10}"

print("\t",layout.format("i", "i*2", "i*3", "i*4", "i*5", "i*6","i*7","i*8","i*9","i*10","i*11","i*12"))
print("   :----------------------------------------------------------------------------------------------------------")
for i in range(1, 13):
    print("{0:>3}:".format(i),layout.format(i, i*2, i*3, i*4, i*5, i*6,i*7,i*8,i*9,i*10,i*11,i*12))