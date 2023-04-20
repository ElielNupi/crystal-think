import os 
import dotenv

def print_env(body):
    try:
        dotenv.load_dotenv()
        dict= {}
        for field in body:
            dict[field] = os.getenv(field)
        return dict
    except Exception as error:
        print(f'Um erro inesperado aconteceu: {error}')

if __name__ == "__main__":
    body = ['app_key']
    print(print_env(body))