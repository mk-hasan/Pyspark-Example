# Documentation(ComPredict Task)

Project Structure

    - Lidl-Task
        - ci
        - resources
            - config
                -config.json
            - data
                -result
        - src
            - app
            - job
            - utils
        - tests
            - unit
            - integration
        - requirements.txt
        - README

### Creating virtual env
You must/should create a virtual env to run the program. 
Run the following command to create virtual env 

- python3 -m venv /path/to/new/virtual/environment

Or follow this instructions from the website:

- https://docs.python.org/3/library/venv.html

It is also possible to use anaconda to create virtual env. Pelase follow the follwoing instructions from the website:
    
    - https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands

Next, Please use the requirements.txt file to install necessary librarires after creating the virtual environment using following command from the root directory:

 - pip install -r requirements.txt 



## Run the program

#### Step 1:
Creating the virutal environment using the above mentioned procedure
and
activate your virtual environment using the following command -> 

You’ll need to use different syntax for activating the virtual environment depending on which operating system and command shell you’re using.

- On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate
- On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh
- On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish
- On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
- On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1

After activating the virtual env, please run the requirements.txt file to install all libraries and dependencies.

      - pip install -r requirements.txt 

It will install all libraries needed to run the program.


Run the data extraction module:

From the src/app folder in the root directory, please run the follwoing command to run the program. 

      - python main.py

It will run and save the result in result folder in csv format. It is just to test that the result are producing.


Thank you


For any query, please contact me through the following email:
    
    - hasan.alive@gmail.com
