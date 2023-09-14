import pandas as pd

class Loader:

    def __init__(self):
        pass

    def load(self, path):
        
        try: 
            self.Df = pd.read_csv(path)
            return self.Df
        except:
            print("Não foi possível carregar o arquivo")
    