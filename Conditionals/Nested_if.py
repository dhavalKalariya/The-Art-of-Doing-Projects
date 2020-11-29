#nested if statement

#blank list [] and "" consider in the of statement as False boolean

teams = ["knicks","kings","heat","pacers","celtrics","pelicans"]

for team in teams:
    if team.startswith("k"):
        print("The "+team.title()+" could win the NBA Championship this year.")
        if team == "knicks":
            print("I know they will win!")
        else:
            print("They probably won't win though...")
    elif team.startswith("p"):
        print("The "+team.title()+"will probably make the playoffs.")
        if team == "pacers":
            print("They need Reggie Miller back though")
    else:
        print("The "+team.title()+" Stand no chance this year")