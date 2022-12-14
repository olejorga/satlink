# 🛰 Satlink

> Let me introduce Satlink. Satlink is a light web framework, that aims to be _**easy to get started with**_, _**easy to build in**_ and _**easy to grow in**_, by focusing on core design principles, such as _"Low Barrier to Entry"_ and _"Self-documenting code"_. This framework was part of a project in Frameworks at HiØ, written with love in Python <3

## Getting started

### Dependencies

* There are almost none! 
* Satlink uses only bits from the Python Standard Library. 
* All you need is Python 3.11 or greater.

### Installation

1. Start by installing the package from pip.
   ```bash
   pip install satlink
   ```
2. Let's create a file called `app.py`.
   ```bash
   touch app.py
   ```
4. Now, populate the app.py file with the following code:
   ```python
   from satlink import Satellite
   
   app = Satellite()
   
   @app.get('/')
   def index(uplink, downlink):
       return downlink.text('Hello, World!')
   
   app.transmit()

   # Alternatively, you may specify a port and/or hostname:
   # app.transmit(3000, 'localhost')
   ```
5. Lastly, let's start our application.
   ```bash
   python3 app.py
   ```
   When you visit [http://localhost:3000/](http://localhost:3000/) you should see the text "Hello, World!".

To learn more, take a look at the [API documentation](https://github.com/olejorga/satlink/wiki).
