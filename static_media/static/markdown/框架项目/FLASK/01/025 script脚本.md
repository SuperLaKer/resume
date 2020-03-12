使用Flask-Script扩展，可以通过python main.py runserver，来启动服务

```python
# main.py
from flask import Flask
from flask_script import Manager
```

```python
app = Flaks(__name__)

manager = Manager(app)

@app.route("/")
def index()：
	return "index page"
if __name__ == "__main__"
	manager.run()
```

查看参数

```
python main.py runserver --help来查看参数

usage: main.py runserver [-?] [-h HOST] [-p PORT] [--threaded]
                         [--processes PROCESSES] [--passthrough-errors] [-d]
                         [-D] [-r] [-R]

Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit
  -h HOST, --host HOST
  -p PORT, --port PORT
  --threaded
  --processes PROCESSES
  --passthrough-errors
  -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                        code)
  -D, --no-debug        disable the Werkzeug debugger
  -r, --reload          monitor Python files for changes (not
                        100{'option_strings': ['-r', '--reload'], 'dest':
                        'use_reloader', 'nargs': 0, 'const': True, 'default':
                        None, 'type': None, 'choices': None, 'required':
                        False, 'help': 'monitor Python files for changes (not
                        100% safe for production use)', 'metavar': None,
                        'container': <argparse._ArgumentGroup object at
                        0x0000023284339D30>, 'prog': 'main.py runserver'}afe
                        for production use)
  -R, --no-reload       do not monitor Python files for changes
```

