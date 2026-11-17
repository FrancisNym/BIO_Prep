alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def step_two_to_four(deck, c):
    length = len(deck)
    new_deck = []
    half1 = deck[:length//2]
    half2 = deck[length//2:]
    for i in range(length//2):
        new_deck.append(half2[i])
        new_deck.append(half1[i])
    c = c % len(new_deck)
    first_c = new_deck[:c]
    new_deck = new_deck[c:]
    new_deck.extend(first_c)
    return new_deck    

def generate_decks(n,c,s):
    deck = []
    for i in range(n):
        deck.append(alphabet[i])
        deck.append(alphabet[i])
    for i in range(s):
        deck = step_two_to_four(deck, c)
    alpha, beta = [],[]
    for i in deck:
        if i not in alpha:
            alpha.append(i)
        else:
            beta.append(i)
    return [alpha,beta]



def manipulate_decks():
    global alpha, beta
    second = alpha[1]
    alpha.pop(1)
    if len(alpha) % 2 == 0:
        middle_a = len(alpha)//2
        alpha = alpha[:middle_a]+[second]+alpha[middle_a:]
    else:
        middle_a = len(alpha)//2+1
        alpha = alpha[:middle_a]+[second]+alpha[middle_a:]

    beta.append(beta[0])
    beta = beta[1:]
    third = beta[2]
    beta.pop(2)
    if len(beta) % 2 == 0:
        middle_b = len(beta)//2
        beta = beta[:middle_b]+[third]+beta[middle_b:]
    else:
        middle_b = (len(beta)//2)+1
        beta = beta[:middle_b]+[third]+beta[middle_b:]
    return beta

def encrypt(target):
    global alpha, beta
    for i in range(len(alpha)):
        if alpha[0] == target:
            return beta[0]
        else:
            alpha.append(alpha[0])
            alpha = alpha[1:]
            beta.append(beta[0])
            beta = beta[1:]

def Solution():
    global alpha, beta
    data = input("Enter: ")
    data = data.split()
    n = int(data[0])
    s = int(data[1])
    c = int(data[2])
    word = data[3]
    encrypted = ""
    decks = generate_decks(n,c,s)
    alpha = decks[0]
    beta = decks[1]
    for i in range(len(word)):
        encrypted = encrypted + encrypt(word[i])
        manipulate_decks()
    return encrypted

while True:
    print(Solution())
