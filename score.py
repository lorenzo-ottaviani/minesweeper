from pathlib import Path
import json

# fonction pour demander nom du joueur

# va regarder si il existe un fichier JSON avec nom du joueur

    # si il n'existe pas, il le créé
    # sinon : il le charge

# factoriser code : pondre des fonctions

# pondre 1 main qui teste tout

def read_score():
    """
    This function will be called when launching the game
    where player enter his/her name

    if score.json does not exist while launching the game :
    create an empty dictionary, dumping empty dictionary to json object
    then save score.json file
    """

    try :
        score_f = Path(__file__).with_name("score.json")
#        score_f = Path("score.json")

        # if score file already exists : we read it
        if score_f.is_file():
            with open(score_f, "r") as openfile :
                json_score = json.load(openfile)
            print(json_score)

        # if score files does not exist :
        else :
            print("rien")
            # create an empty dictionary, dumping empty dictionary to json object
            empty_score = {}
            json_score = json.dumps(empty_score)
            # then save score.json file
            with open(score_f, "w") as outfile :
                outfile.write(json_score)

    except ( IOError, OverflowError) as error :
        print("Error while writing")

    except (IsADirectoryError, FileNotFoundError, NameError, OSError, PermissionError) as error :
            print("Error with file or OS error")
    
    except (UnicodeDecodeError, UnicodeEncodeError) as error :
        print("Error with encoding or decoding")

    except Exception :
        print("Error while writing")

