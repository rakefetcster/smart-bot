import logging
from  genai_manager import Manager

# TODO: Configure logging
logger = logging.getLogger(__name__)
giniManager = Manager()

def main():
    user_message = input('Please write you question:')
    output = giniManager.generate_response(user_message)
    print(output)
    
if __name__ == "__main__":
    main()
	
