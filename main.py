import os
import openai



def set_openai_key():
    try:
        # Get OPENAI_KEY from the environment variables
        openai_key = os.environ['OPENAI_KEY']
        openai.api_key = openai_key
    except KeyError:
        raise SystemExit("ERROR: OPENAI_KEY not set in the environment variables")

def get_and_print_user_input():
    # Prompt the user for input
    user_input = input("Please enter a string: ")
    # Print the input string
    print("You entered:", user_input)
    return user_input

def processinput(input):
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": "You are an application generator that can generate a standard webui dialog.  You have all of the standard UI elements like buttons, input field, radio buttons, checkboxes, images, and the like.\n\nYou will be given an English description of an application, and you need to figure out what elements would be needed for that. "
        },
        {
        "role": "user",
        "content": input
        }
    ],
    temperature=1,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response)

def main():
    set_openai_key()
    input = get_and_print_user_input()
    processinput(input)

if __name__ == "__main__":
    main()

