![logo](docs/logo.svg)

# Pipeline (WIP)

...


## Installation

```bash
git clone https://github.com/olejorga/pipeline.git
cd pipeline
```


## Quick start

```python
from pipeline import Pipeline
from pipeline.response import Response


app = Pipeline()


@app.get('/greeting/:name')
def greet(req):
    name = req.params['name']
    return Response(f'Hello {name}!')
  
  
app.run()
```
