import random
import string

bugs = ['ambrosia beetle', 'army ant', 'bark mantis', 'bat bug', 'bat fly', 'birdwing', 'blister beetle', 'blue darner', 'bookworm', 'boxer mantis', 'canna leaf roller', 'cantharoid beetles', 'cardinal beetle', 'clothes moth', 'cockchafer', 'cockroach', 'cuckoo bee', 'cucumber beetle', 'cutworm', 'damselfly', 'dead leaf mantis', 'dragonfly', 'dung beetle', 'field cricket', 'fig wasp', 'flightless fruit fly', 'flour beetle', 'flower mantis', 'fungus gnat', 'glowworm', 'gnat', 'grass bagworm', 'grass mantis', 'grasshopper', 'green bottle fly', 'ground mantis', 'guava moth', 'harvester ant', 'holly leaf miner', 'housefly', 'kelp fly', 'leaf mantis', 'leafmimic katydid', 'locust', 'maguey worm', 'mezcal worm', 'midge', 'mud dauber', 'nairobi fly', 'paper wasp', 'pollen beetle', 'rat flea', 'sandfly', 'seed fly', 'shield mantis', 'silkworm', 'spruce sawflies', 'squash bee', 'stick mantis', 'toktokkies', 'twigborer', 'uzi fly', 'water beetle', 'waxworm', 'wheat fly', 'white flannel moth', 'witchetty grub', 'woodworm', 'yellowjacket']
letters = list(string.ascii_lowercase)
gridsize = 20
orientations = [ 'fhoriz', 'rhoriz', 'fvert', 'rvert', 'ufdiag', 'urdiag', 'dfdiag', 'drdiag']


chosenbugs = []
while len(chosenbugs) < 10:
    chosenbugs.append(random.choice(bugs))
    chosenbugs = list(set(chosenbugs))


chosenbugs = [''.join(x.split(" ")) for x in chosenbugs]
game = [['']*gridsize for x in range(gridsize)]




def assign(word, gridsize, direction):
    if direction == 'fhoriz' or direction == 'rhoriz':
        if direction == 'rhoriz':
            word = word[::-1]
        collision = True
        while collision:
            starthoriz = random.choice(range(gridsize - len(word)))
            startvert = random.choice(range(gridsize))
            w = list(word)
            for n in range(len(w)):
                if game[startvert][starthoriz + n] in ['', w[n]]:
                    pass
                else:
                    break
            else:
               for n in range(len(w)):
                   game[startvert][starthoriz + n] = w[n]
                   collision = False
    if direction == 'fvert' or direction == 'rvert':
        if direction == 'rvert':
            word = word[::-1]
        collision = True
        while collision:
            starthoriz = random.choice(range(gridsize))
            startvert = random.choice(range(gridsize - len(word)))
            w = list(word)
            for n in range(len(w)):
                if game[startvert +n][starthoriz] in ['', w[n]]:
                    pass
                else:
                    break
            else:
                for n in range(len(w)):
                    game[startvert + n][starthoriz] = w[n]
                    collision = False
                    
    if direction == 'ufdiag' or direction == 'urdiag':
        if direction == 'urdiag':
            word = word[::-1]
        collision = True
        while collision:
            starthoriz = random.choice(range(gridsize - len(word)))
            startvert = random.choice(range(len(word),gridsize))
            w = list(word)
            for n in range(len(w)):
                if game[startvert - n][starthoriz + n] in ['', w[n]]:
                    pass
                else:
                    break
            else:
                for n in range(len(w)):
                    game[startvert - n][starthoriz + n] = w[n]
                    collision = False
                    
    if direction == 'dfdiag' or direction == 'drdiag':
        if direction == 'rdiag':
            word = word[::-1]
        collision = True
        while collision:
            starthoriz = random.choice(range(gridsize - len(word)))
            startvert = random.choice(range(gridsize - len(word)))
            w = list(word)
            for n in range(len(w)):
                if game[startvert + n][starthoriz + n] in ['', w[n]]:
                    pass
                else:
                    break
            else:
                for n in range(len(w)):
                    game[startvert + n][starthoriz + n] = w[n]
                    collision = False

def fill():
    for y in range(len(game)):
        for x in range(len(game[y])):
            if game[y][x] == '':
                game[y][x] = random.choice(letters)


def addbug():
    for bug in chosenbugs:
        assign(bug, gridsize, random.choice(orientations))
    fill()
    for x in game:
        print(' '.join(x))

    print('your word bank is')
    bugq = []
    for x in chosenbugs:
        if len(bugq) < 3:
            bugq.append(x)
        else:
            print(' '.join(bugq))
            bugq = []
    else:
        print(' '.join(bugq))
            
if __name__ == "__main__":
    addbug()
                
