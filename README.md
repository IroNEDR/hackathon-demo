# Demo Project
This is a sample project to demonstrate how to setup your own ML service and publish it as a Docker container.  
It is intended to be used as a possible template for the participants of the Hackfestival 2024.

This service simulates the steps of training your ML Model and then serving the stored, trained model as a REST API. First in `train_model.py` random data is generated, then a simple local outlier probability model is trained on this data.  
The trained model is then saved to disk as a pickle and served as a REST API in `ml_service.py`.

A docker image is created, which only contains the trained model, the `requirements.txt` file and the `ml_service.py` file.  
The `send_request.py` file is only used for local testing and is not part of the docker image.  
The `train_model.py` file is only used to train the model localy on your machine and is also not part of the docker image.

## How to run this project (Optional)
This project is only intended to give you some inspiration. You don't need to run it yourself. However, if you want to run it, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/IroNEDR/hackathon-demo.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hackathon-demo
    ```
3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate # On Mac or Linux
    # On Windows:
    .\env\Scripts\activate
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Train the model:
    ```bash
    python train_model.py
    ```
6. Run the ML service:
    ```bash
    python ml_service.py
    ```
7. Open a new terminal and send a request to the service:
    ```bash
    python send_request.py
    ```


## How to create your own Python project
When you create your own Python project follow these steps:
1. Ensure that you have python and python-venv installed in your machine and if not install it following the instructions for your OS.
2. Create a directory for your project and navigate to it:
    ```bash
    mkdir your_project
    cd your_project
    ```
3. Create a virtual environment. You can choose your name, but I recommend using the name `env`:
    ```bash
    python3 -m venv env
    ```
4. Activate the virtual environment:
    ```bash
    source env/bin/activate # On Mac or Linux
    .\env\Scripts\activate # On Windows
    ```
5. Install the packages from the requirements.txt file using pip:
    ```bash
    pip install <package_name>
    ```
6. Create a requirements.txt that specifies all the external packages needed to run your app:
    ```bash
    pip freeze > requirements.txt
    ```
    Your teammates can then install all the dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
7. Create a .gitignore file in your project directory and [add this content](https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore) to it.
8. Create a README.md file in your project directory and add a description of your project.
9. Create a Dockerfile in your project and set it up similar to the one in this project.
10. Create a new repository on GitHub and push your project to it:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin <your_git_repository_url>
    git push -u origin main
    ```

11. Build and publish your docker image so that you can later use it in SAP AI Core.
    ```bash
    docker login
    # After you have logged in, build and push your docker image
    docker build -t <your_docker_image_name> .
    docker tag <your_docker_image_name> <your_docker_image_name>:latest
    docker push <your_docker_image_name>:latest
    ```

12. Follow the instructions in the [SAP AI CORE Hackathon Repository](https://github.com/EkinTiras/hackathon) if you want to run your docker image in SAP AI Core.
