def are_you_playing_banjo(name):
    if (name[0].lower() == 'r'):
        return name + " plays banjo"
    return name + " does not play banjo"

names = ["Rick", "rachel", "Adam", "Banjo", "R", "Robert Smith"]

for name in names:
    print(are_you_playing_banjo(name))
