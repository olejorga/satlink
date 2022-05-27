<pre>
     _____ _            _ _             
    |  __ (_)          | (_)            
    | |__) | _ __   ___| |_ _ __   ___  
    |  ___/ | '_ \ / _ \ | | '_ \ / _ \ 
    | |   | | |_) |  __/ | | | | |  __/ 
    |_|   |_| .__/ \___|_|_|_| |_|\___| 
            | |                         
            |_|   A light web framework
</pre>

# Pipeline

> Let me introduce Pipeline. Pipeline is a light web framework, that aims to be _**easy to get started with**_, _**easy to build in**_ and _**easy to grow in**_, by focusing on core design principles, such as _"Low Barrier to Entry"_ and _"Self-documenting code"_. This framework is part of a project in Frameworks at HiØ, written with love in Python <3

## Getting started

### Dependencies

* There are almost none! 
* Pipeline uses only bits from the Python Standard Library. 
* All you need is Python 3.7 or greater.

### Installation

Since Pipline is not yet published on any python package index, such as pip, you will have to download the source code manually. This can be done via the link below.

[**Download now**](https://github.com/olejorga/pipeline/archive/refs/heads/main.zip)

Inside the downloaded zip file, there is a folder named "pipeline". This is the framework itself. In your project you will have to import the framework from this folder. Below you'll find a short tutorial on how set up a basic project.

### Your first project

1. Start by creating a direcotry for your project and entering it.
   ```console
   mkdir project
   cd project
   ```
2. Inside, let's create a new directory called `lib` **and paste the pipline folder inside here**.
   ```console
   mkdir lib
   ```
3. Let's also create a file called `app.py` in the root of our project.
   ```console
   touch app.py
   ```
   Now you should have a project structure like this:
   ```
   project
   |_ lib
   |  |_ pipeline
   |_ app.py
   ```
4. Now, populate the app.py file with the following code:
   ```python
   from lib.pipeline import Pipeline, Response
   
   app = Pipeline()
   
   @app.get('/')
   def index_view(req):
       return Response('Hello World!')
   
   app.run()
   ```
5. Lastly, let's start our web application.
   ```console
   python3 app.py
   ```
   When you visit [http://localhost:3000/](http://localhost:3000/) you should see the text "Hello World!".

To learn more, take a look at the [API documentation](https://github.com/olejorga/pipeline/wiki).

### Disclaimer

_If this project did use a package manager like pip. Installation would be as easy as typing `pip install pipeline`, which means you could skip step 2 of the tutorial, and import the framework by just typing `import pipeline`._
