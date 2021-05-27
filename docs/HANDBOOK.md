# Handbook 📚

> The `api.samuelsandoval.me` handbook!!

## Contributing 🔨

1. Fork this repository You can accomplish this by clicking the [Fork] button on the top right corner of this page.
2. Navigating to your preferred workspace in your terminal to work on the repository locally. Use [this guide] if necessary.
3. Clone your forked repository by running the following command. Replace YOUR_GITHUB_USERNAME with your GitHub username.
```
git clone https://github.com/YOUR_GITHUB_USERNAME/api.samuelsandoval.me.git
``` 
4. Look over at the issues tab for features, bugs the project currently has available.

## Development 👨‍💻

Make sure to have Python3, and PIP installed. Pip download instructions below

Once you have both, install flask and gunicorn:

```
pip3 install flask gunicorn
```
To spin up the development server, execute `python3 main.py`.


## Package Managers 📦

### Pip 🛹

To check if Pip is installed.
unix/MacOS
```
python -m pip --version
```
Windows
```
py -m pip --version
```

To install pip using Command Line:
unix/MacOS
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
To check if installed:
```
python get-pip.py
```

Windows
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
To check if installed:
```
py get-pip.py
```


## Deployment 🚀

### Heroku 🀄

Visit the [Heroku Dashboard][heroku_dash] to deploy the latest version of the site.


[heroku_dash]: https://dashboard.heroku.com/apps/api-samuelsandoval-me