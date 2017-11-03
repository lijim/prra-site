**A website prototype for Passaic River Rowing**

Based in:
- Flask (python) as our webserver.  Our needs are simple (landing page, static files), so we choose something easy to boot up.  Python 3.3+
- Basic HTML/CSS/JS front-end layer.  We choose this over a CMS like WordPress so we can modify the site more freely without all the overhead of a CMS.
- Hosting on Heroku

*Setup of our virtual env:*

```
python3 -m venv /path/to/virtual/environment
```
1. Install the virtual environment
- make sure that the path to the virtual environment isn't the same as the prra-site project folder.
- I'm use this paradigm:
```
python3 -m venv ~/.ve/prra
```

2. Activate the virtual environment
Use these commands to activate the environment
```
Mac (Terminal):
source <venv path>/bin/activate
Windows (cmd.exe):
C:\> <venv path>\Scripts\activate.bat
```

3. Install the requirements
```
pip install -r requirements.pip
```

(See here for more help: https://docs.python.org/3/library/venv.html)

4. Set up the environment variables
Use this command to set your FLASK_APP variable:
```
export FLASK_APP=prra_site/__init__.py
```
(Shortcut to running this all the time: add it to your .bash_profile file)

5. Run! 😃
```
flask run
```
