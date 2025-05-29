# Requires response, requests and pydantic to be installed (use pip) prior to running
from dto import *
import getopt, requests, sys

def display_help():
    print('''
Usage:

userclient  -h | --help       Displays this help page
            -e | --endpoint   API endpoint
            -a | --apikey     API key
            -p | --page       Page, e.g. 1         
''')

class UserClient:
    def __init__(self, endpoint: str, apikey: str):
        self.endpoint = endpoint
        self.apikey = apikey

    def get_users(self):
        try:
            response = requests.get(
                self.endpoint,
                params={"page": str(self.page)},
                headers={"x-api-key": self.apikey},
            )
        except:
            print("An error occurred accessing the specified endpoint.")

        api_response = ApiResponseDTO(**response.json())
        return api_response.data        
    
    def run(self, page: int = 1):
        self.page = page
        users = self.get_users()
        for user in users:
            print("%s %s" %(user.firstName, user.lastName))

if __name__ == "__main__":
    # Set defaults for when parameters not supplied
    endpoint = "https://reqres.in/api/users"
    apikey = "reqres-free-v1"
    page = 1

    # Remove 1st argument (filename) from argument list
    argument_list = sys.argv[1:]

    # Options
    options = "heap:"

    # Long options
    long_options = ["help", "endpoint=", "apikey=", "page="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argument_list, options, long_options)
        
        # Checking each argument
        for current_argument, current_value in arguments:
            if current_argument in ("-h", "--help"):
                display_help()
                sys.exit()
                
            elif current_argument in ("-e", "--endpoint"):
                endpoint = current_value
                
            elif current_argument in ("-a", "--apikey"):
                apikey = current_value

            elif current_argument in ("-p", "--page"):
                page = current_value
                
    except getopt.GetoptError as error:
        # Output error, and return with an error code
        print(str(error))

    client = UserClient(endpoint = endpoint, apikey = apikey)
    client.run(page = page)