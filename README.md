# 🛰 SATLINK

> Let me introduce Satlink. Satlink is a light web framework, that aims to be _**easy to get started with**_, _**easy to build in**_ and _**easy to grow in**_, by focusing on core design principles, such as _"Low Barrier to Entry"_ and _"Self-documenting code"_. This framework was part of a project in Frameworks at HiØ, written with love in Python <3

## Getting started

### Dependencies

* There are almost none! 
* Satlink uses only bits from the Python Standard Library. 
* All you need is Python 3.7 or greater.

### Installation

Since Pipline is not yet published on any python package index, such as pip, you will have to download the source code manually. This can be done via the link below.

[**Download now**](https://github.com/olejorga/satlink/archive/refs/heads/main.zip)

Inside the downloaded zip file, there is a folder named "satlink". This is the framework itself. In your project you will have to import the framework from this folder. Below you'll find a short tutorial on how set up a basic project.

### Your first project

1. Start by installing the package from pip.
   ```console
   pip install satlink
   ```
2. Let's create a file called `app.py`.
   ```console
   touch app.py
   ```
4. Now, populate the app.py file with the following code:
   ```python
   from lib.satlink.main import Satellite
   
   app = Satellite()
   
   @app.get('/')
   def index(uplink, downlink):
       return downlink.text('Hello, World!')
   
   app.transmit()
   
   """
   Alternatively, you may specify a port and/or hostname:
   app.transmit(8080, 'localhost')
   """
   ```
5. Lastly, let's start our application.
   ```console
   python3 app.py
   ```
   When you visit [http://localhost:3000/](http://localhost:3000/) you should see the text "Hello, World!".

To learn more, take a look at the [API documentation](https://github.com/olejorga/satlink/wiki).
