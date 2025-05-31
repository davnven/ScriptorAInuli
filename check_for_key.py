import os

#print(os.environ["OPENAI_API_KEY"])
def has_key() -> bool:
    try:
        has_key = (bool(os.environ["OPENAI_API_KEY"]))
    except:
        print(f"OPENAI_API_KEY is not set as en env variable. Please execute the following command in the command line: \n setx OPENAI_API_KEY 'your_api_key_here' (Windows)")
        return False
    else:
        if __name__ == "__main__" :
            print("OPENAI_API_KEY is env variable.")
        return True
    
if __name__ == "__main__" :
   has_key()