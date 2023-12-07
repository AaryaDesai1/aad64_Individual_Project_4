# aad64_Individual_Project_4
Auto Scaling Flask App Using Any Platform As a Service

YourAppFolder/
├── app.py
├── templates/
│   └── index.html  # Your HTML file
├── static/
│   ├── css/
│   ├── js/
│   └── images/      # Your image files
└── your_python_files/
    ├── __init__.py
    ├── data_processing.py
    └── other_python_file.py


## FAQs:

### 1. How do I create a Dockerhub repository?
Ans: I. First, you need to create a Dockerhub account. You can do so [here](https://hub.docker.com/signup).
II. Then, you need to create a repository. You can do so by clicking on `Create Repository`.
III. Then, you need to choose a name for your repository. For this project, I chose `individual_project_4`. (*Note*: Try to add a description as well so that you know what the repo is for.)
IV. Then, you need to choose whether you want the repository to be public or private. For this project, I chose `public` as I wanted to make it accessible to everyone.
V. Go ahead and click `Create`. Your screen should would look something like this (**Tip**: Keep website handy because you're going to need the Docker command soon.):


### 2. How do I initially create a web app in Azure? 
Ans: I. You start by opening up Microsoft Azure Portal. Go to `Create a New Resource` and click `Web` then `Web App`. 
II. Make sure you've been given enough credits to create a new web app (and if now, ask one of the TAs). 
III. Then, you need to choose or create a Resource Group. For this project, I created a new one. 
IV. Choose a name for your project and make sure it's unique. For this project, I called the web app `TellMeMyProfession`.
V. Choose how to publish your code. For this project, I chose `Docker Container` as I wanted to use Docker to deply my app as a Docker image.
VI. Choose the operating system. I chose `Linux` as I am working with a Mac.
VII. For region, pricing tier, and size, I chose the default options. 
VIII. Click Docker, and choose the following options (make sure to change it according to your needs):

IX. Click `Review + Create` and then `Create`.
For a much better, and much more detailed **how-to**, check [this](https://learn.microsoft.com/en-us/training/modules/host-a-web-app-with-azure-app-service/1-introduction) link out.

### 3. How do I build a docker image?
Ans. For this, you're first going to want to layout your dockerfile (you can check mine out [here]()). You can find the dockerfile for this project in the main project directory. This will install use Python 3.10.8 as the base image, set the working directory to /app and copy the local directory contents into the container, install required Python packages from a requirements.txt file, expose port 5000 to allow external access, set an environment variable NAME to myenv, and execute a Flask application (flask_app.py) with specified host and port configurations when the container starts.
Then, you want to first make sure you have the docker library, so make sure to run `pip install docker` in your terminal if you don't have it already.
* To then build the docker file, you use the following command: 
+ `docker build myapp`
* To run the docker file, you use the following command:
+ `docker run -p 5000:5000 myapp`
[**Note** These commands were run in a virtual environment.]

### 4. Why do I have two Dockerfiles?
Ans: I have two Dockerfiles because these two Dockerfiles serve different purposes - one for deploying the Flask application in a production-like environment, and the other for setting up a development environment. The Dockerfile is located in the *main project directory* and is used for deploying your Flask application. It includes instructions to set up a Python environment, copy your project files, install dependencies, and run your Flask app. The Dockerfile located in the *.devcontainer folder* is typically used in development environments, especially when working with Visual Studio Code or VS Code's Remote - Containers extension.

### 5. How do I build and push the docker image to my Docker Hub repository?
Ans: To build and push the docker image to your repo, you are going to want to run the following commands:
`docker login --<insert username>`
`docker build -t <insert username>/<insert repo name>`
`docker push <insert username>/<insert repo name>`
[**Note** These commands were run in a virtual environment.]

### 5. Why do I need to create a virtual environment? 
Ans: This project was created using Python 3.10.8. However, you may have a different version of Python installed on your computer. To avoid any version conflicts, you need to create a virtual environment. Also, this project was using an LLM from huggingface, which has a lot of dependencies (often conflicting with those you may have on your local computer). So, to avoid frustration and to make sure that the project runs smoothly, you need to create a virtual environment.
You can do so by running the following commands in your terminal:
`python3 -m venv <YOUR_VENV_NAME>`
`source <YOUR_VENV_NAME>/bin/activate`
Then, you want to make sure you have all the dependencies needed to run the prooject and you can do so by either running `pip install -r requirements.txt` or `make install` (depending on how you've formatted your Makefile by this point).

### 6. How do I use **huggingface** in my code?
Ans: First, you need to install the `openai` library using `pip install openai`. Then, you need to set up a virtual environment in Python using `python -m venv <YOUR_VENV_NAME>`. Then, you need to activate the virtual environment using `source <YOUR_VENV_NAME>/bin/activate` (for MacOS users). 
Then you needt to set up your API key. I used a single project API key (on the OpenAI website [here](https://platform.openai.com/account/api-keys)) because I only wanted it to be accessible for the current project, so I used `.env` and `.gitignore` for the same (click [here](https://platform.openai.com/docs/quickstart?context=python) for more information on set up). 
Then, you need to define functions to call the API in the main .py file that you're using to run your app. You can find the code for the same in `flask_app.py` in this project.

### 4. How do I deploy my web app?
Ans: There are multiple ways you can do this, but for the current project I used Flask. For the same, you need to create a `requirements.txt` file which contains all the libraries you need to run your app. You also need to create a `Procfile` which contains the command to run your app (`web: gunicorn flask_app:app`).

You can find the documentation for Flask [here](https://flask.palletsprojects.com/en/1.1.x/). You can also find a tutorial on how to deploy a Flask app on Azure [here](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask).

3. What are the libraries I need to install?
Ans: Most of the libraries are the usual ones we need for CI/CD (e.g., pytest, ruff, etc.). You can find the list of libraries in the `requirements.txt` file. You can install them by running `pip install -r requirements.txt` in your terminal. Some of the unique ones required specifically for this project were:
* `Flask` - to create the web app
* `gunicorn` - to run the Flask app on Azure
* `openai` - to use the GPT-3 API
* `Werkzeug` - collection of libraries that you can use to build Web Server Gateway Interface (WSGI) compliant web applications in Python. 

4. 

2. How to run the app locally?

