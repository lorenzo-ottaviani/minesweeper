from pathlib import Path
import json

class Score :

    def read_score(self):
        """
        Function called when launching the game
        if score.json does not exist while launching the game :
        creates score.json file
        returns dictionary object
        """
        try :
            score_f = Path(__file__).with_name("score.json")

            # if score file already exists : we read it
            if score_f.is_file():
                with open(score_f, "r") as openfile :
                    all_scores = json.load(openfile)
                    # if json_score is a json object : convert it into python dict
                    if type(all_scores) != dict :
                        all_scores = json.loads(all_scores)

            else :
                # create an empty dictionary, dumping empty dictionary to json object
                all_scores = {}
                json_score = json.dumps(all_scores)

                with open(score_f, "w") as outfile :
                    outfile.write(json_score)

            return all_scores

        except ( IOError, OverflowError) as error :
            print("IOError or OverFlowError")

        except (IsADirectoryError, FileNotFoundError, NameError, OSError, PermissionError) as error :
                print("Error with file or OS error")
        
        except (UnicodeDecodeError, UnicodeEncodeError) as error :
            print("Error with encoding or decoding")

        except Exception :
            print("Error while writing")


    def write_score(self, score):
        """
        writes new score into "score.json" file
        """
        try :
            with open("./score.json", "w") as file:
                json.dump(score, file)

        except ( IOError, OverflowError) as error :
            print("Error while writing")
        except (IsADirectoryError, FileNotFoundError, NameError, OSError, PermissionError) as error :
                print("Error with file or OS error")
        except (UnicodeDecodeError, UnicodeEncodeError) as error :
            print("Error with encoding or decoding")
        except Exception :
            print("Error while writing")


    def record_score(self, player_name, player_score):
        """
        retrieves score.json data
        updates all scores dictionary with player new score
        then calls write_scores method
        """

        all_scores = self.read_score()

        if player_name in all_scores.keys():
            all_scores[player_name] = player_score
        else :
            all_scores[player_name] = player_score
        self.write_score(all_scores)


    def enter_name(self):
        """
        return a tuple with 2 values :
        player name and his/het score
        """

        player_name = input("Bonjour, entrez votre nom\n")
        all_scores = self.read_score()

        if player_name in all_scores.keys():
            player_score = all_scores[player_name]
        else :
            player_score = 0
        return (player_name, player_score)

