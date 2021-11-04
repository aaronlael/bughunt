import random
import string

bugs = ['ambrosia beetle', 'army ant', 'bark mantis', 'bat bug', 'bat fly', 'birdwing', 'blister beetle', 'blue darner', 'bookworm', 'boxer mantis', 'canna leaf roller', 'cantharoid beetles', 'cardinal beetle', 'clothes moth', 'cockchafer', 'cockroach', 'cuckoo bee', 'cucumber beetle', 'cutworm', 'damselfly', 'dead leaf mantis', 'dragonfly', 'dung beetle', 'field cricket', 'fig wasp', 'fruit fly', 'flour beetle', 'flower mantis', 'fungus gnat', 'glowworm', 'gnat', 'grass bagworm', 'grass mantis', 'grasshopper', 'green bottle fly', 'ground mantis', 'guava moth', 'harvester ant', 'holly leaf miner', 'housefly', 'kelp fly', 'leaf mantis', 'leafmimic katydid', 'locust', 'maguey worm', 'mezcal worm', 'midge', 'mud dauber', 'nairobi fly', 'paper wasp', 'pollen beetle', 'rat flea', 'sandfly', 'seed fly', 'shield mantis', 'silkworm', 'spruce sawflies', 'squash bee', 'stick mantis', 'toktokkies', 'twigborer', 'uzi fly', 'water beetle', 'waxworm', 'wheat fly', 'white flannel moth', 'witchetty grub', 'woodworm', 'yellowjacket']
letters = list(string.ascii_lowercase)
gridsize = 20
bugcount = 10

orientations = [ 'fhoriz', 'rhoriz', 'fvert', 'rvert', 'ufdiag', 'urdiag', 'dfdiag', 'drdiag']
game = [['']*gridsize for x in range(gridsize)]

def assign(word, gridsize, direction, solution):
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
                solution[word] = {}
                solution[word]['start'] = [startvert, starthoriz]
                solution[word]['end'] = [startvert, starthoriz + len(w) -1]
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
                solution[word] = {}
                solution[word]['start'] = [startvert, starthoriz]
                solution[word]['end'] = [startvert + len(w) - 1, starthoriz]
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
                solution[word] = {}
                solution[word]['start'] = [startvert, starthoriz]
                solution[word]['end'] = [startvert - len(w) - 1, starthoriz + len(w) -1 ]
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
                solution[word] = {}
                solution[word]['start'] = [startvert, starthoriz]
                solution[word]['end'] = [startvert + len(w) - 1, starthoriz + len(w) - 1 ]
                for n in range(len(w)):
                    game[startvert + n][starthoriz + n] = w[n]
                    collision = False
    return solution

def fill():
    for y in range(len(game)):
        for x in range(len(game[y])):
            if game[y][x] == '':
                game[y][x] = random.choice(letters)


def addbug(printflag):
    chosenbugs = []
    while len(chosenbugs) < bugcount:
        chosenbugs.append(random.choice(bugs))
        chosenbugs = list(set(chosenbugs))


    chosenbugs = [''.join(x.split(" ")) for x in chosenbugs]

    solution = {}
    for bug in chosenbugs:
        assign(bug, gridsize, random.choice(orientations), solution)
    fill()
    if printflag == True:
        for x in game:
            print(' '.join(x))

        print('your word bank is')
        while len(chosenbugs) > 0:
            if len(chosenbugs) > 3:
                   print(' '.join(chosenbugs[:3]))
                   chosenbugs = chosenbugs[3:]
            else:
                print(' '.join(chosenbugs))
                break
        return solution
    else:
        return { 'game' : game,
                 'bugs' : chosenbugs,
                 'solution' : solution,
                 }

if __name__ == "__main__":
    print(addbug(True))
