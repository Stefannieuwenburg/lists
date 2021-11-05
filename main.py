# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# Exercise:list

#opd 1
def alphabetical_order(movies):
    return sorted(movies)

movies = [
            "Schindler s List"
            "Earthquake",
            "Superman",
            "Fahrenheit",
            "Schindler's list",
            "Seven years in Tibet",
            "Toto XX",
            "Juresic Park",
            "Cinderella Liberty"]
#opd 2
def won_golden_globe(movie):
    winners = [
            "jaws",
            "star wars: episode iv – a new hope",
            "e.t. the extra-terrestrial",
            "memoirs of a geisha",
    ]
    if movie.lower() in winners:
       return True
    else:
       return False

#opd 3
def remove_toto_albums(list_strings):
    toto_albums = ['Fahrenheit',
                'The Seventh One',
                'Toto XX',
                'Falling in Between',
                '35th Anniversary - Live in Poland',
                'Toto XIV',
                'Old Is New', 
                '40 Tours Around the Sun',
                'With a Little Help from My Friends']

    new_list = [x for x in list_strings if x not in toto_albums]
    # new_list = list(set(list_strings) - set(toto_albums))
    return new_list

print(remove_toto_albums(['The Seventh One', 'Enne', 'Toto XX']))
print(won_golden_globe("Memoirs of a Geisha"))
print(alphabetical_order(movies))


