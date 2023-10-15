# Python Application using OpenAI API

This Python script uses the OpenAI API to process user input and generate responses. It includes functions to set API keys, take user input, and process that input using a custom model.

## Prerequisites

-   Python 3.6+
-   OpenAI API key

## Installation

### Step 1: Clone the repository

Clone the repository to your local machine.

```bash
gh repo clone boostedcoder/app_generator
```

### Step 2: Set up a virtual environment

Navigate into the project directory:

```bash
cd app_generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

-   **Windows**

    ```bash
    .\venv\Scripts\activate
    ```

-   **Unix or MacOS**

    ```bash
    source venv/bin/activate
    ```

### Step 3: Install dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Set up the API Key

Ensure to set up your OpenAI API key. You can do this by setting up an environment variable as follows:

-   **Windows**

    ```bash
    setx OPENAI_KEY "your-api-key-here"
    ```

-   **Unix or MacOS**

    ```bash
    export OPENAI_KEY="your-api-key-here"
    ```

## Usage

Run the script using Python:

```bash
python3 main.py
```

Replace `script_name.py` with the name of your Python file.

## Function Descriptions

### `set_openai_key()`

This function retrieves the OpenAI API key from the environment variables and sets it up for use in the script.

### `get_and_print_user_input()`

This function prompts the user for input, prints it, and then returns it for further use.

### `processinput(input)`

This function accepts a user input and processes it using the OpenAI API, utilizing a custom model and function to generate a response.

### `main()`

This function orchestrates the flow of the script, calling the previously described functions in order.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.

## Acknowledgments

-   OpenAI for providing the API used in this script.
