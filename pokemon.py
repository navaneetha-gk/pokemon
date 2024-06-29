import requests

def print_type(type_of_pokemon): #to print each type with their background colour, I didnt find the data in the api so I had to hardcode the values
    color={"NORMAL": ["A8A77A",[168,167,122]],#grey
    "FIRE": ["EE8130",[238,129,48]],#orange
    "WATER": ["6390F0",[99,144,240]],#blue
    "ELECTRIC": ["F7D02C",[247,208,44]],#yellow
    "GRASS": ["7AC74C",[122,199,76]],#GREEN
    "ICE": ["96D9D6",[150, 217, 214]],#LIGHT BLUE
    "FIGHTING": ["C22E28",[194,46,40]],#RED
    "POISON": ["A33EA1",[163,62,161]],#PURPLE
    "GROUND": ["E2BF65",[226,191,101]],#LIGHT YELLOW
    "FLYING": ["A98FF3",[169, 143, 243]],#LIGHTPURPLE
    "PSYCHIC": ["F95587",[249, 85, 135]],#PINK
    "BUG": ["A6B91A",[166, 185, 26]],#MOSS GREEN 
    "ROCK": ["B6A136",[182, 161, 54]],#MUSTARD
    "GHOST": ["735797",[115, 87, 151]],#DARKPURPLE
    "DRAGON": ["6F35FC",[111,53,252]],#BRIGHT PURPLE VIOLET
    "DARK": ["705746",[112, 87, 70]],#BROWN
    "STEEL": ["B7B7CE",[183, 183, 206]],#LIGHTGREY
    "FAIRY": ["D685AD",[214, 133, 173]],#LIGHTPINK
    }  
    print('\033[48;2;%d;%d;%dm'%(color[type_of_pokemon][1][0],color[type_of_pokemon][1][1],color[type_of_pokemon][1][2]),type_of_pokemon,sep="",end='')

name=input("enter name of the pokemon\n")

url=f"https://pokeapi.co/api/v2/pokemon/{name}/"
response=requests.get(url)
statuscode=response.status_code

if statuscode==200:

    details_dict=response.json()

    #obtaining properties of pokemon
    details_to_display={"Name":name.capitalize(),
                        "National Number":details_dict["id"],
                        "Abilities":(details_dict["abilities"][0]["ability"]["name"]).title(),
                        "Type":'',
                        "Height":str(details_dict["height"]/10)+" m",
                        "Weight":str(details_dict["weight"]/10)+" kg"
    }
    for j in details_dict["types"]:
        details_to_display["Type"]=details_to_display["Type"]+j["type"]["name"].upper()+' '

    base_stats= {} 
    total=0

    #obtaining base stats and total
    for i in range(6):
       base_stats[details_dict["stats"][i]["stat"]["name"].upper()]=details_dict["stats"][i]["base_stat"]
       total+=details_dict["stats"][i]["base_stat"]

    print()

    #printing properties of pokemon (the escape sequences are used for bold text of the property)
    for key,value in details_to_display.items():
        print("\033[1;37;40m",end="")
        print(key,": ",end="")

        if key=="Type":#printing type with different background color
            for i in value.split():
                print_type(i)
                print("\033[0;37;40m ",end="")
            print("\033[0;37;40m ")
        else:
            print("\033[0;37;40m ",end="")
            print(value)

    #printing Base stats of pokemon (the escape sequences are used for bold text of the stat)
    print("\n\033[1;37;40mBase Stats:\n")
    base_stats["Total"]=total
    for key,value in base_stats.items():
        print("\033[1;37;40m",key,": ",sep="",end="")
        print("\033[0;37;40m",value)

    print()

    sprite_url=details_dict["sprites"]["other"]["official-artwork"]["front_default"]
    sprite_response=requests.get(sprite_url).content
    with open('sprite.png', 'wb') as image_sprite:
        image_sprite.write(sprite_response)
        print("\033[1;32;40mImage downloaded\033[0;37;40m",sep="",end="")

else:
    print("\033[38;2;214;133;173mPokemon not found\033[0;37;40m")

