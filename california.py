from random import choice

capital = "Sacramento"

flower = "Poppy"

song = "California Dreaming"

def randomfunfact():
    funfacts = [
        "California has seven National parks",
        "California has more people than any other state",
        "Most Californians don't surf",
        "The pacific ocean is freezing off the coast"
    ]

    index = choice("0123")
    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()