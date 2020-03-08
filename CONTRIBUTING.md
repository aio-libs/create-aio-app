# Contributing to create-aio-app

If you open this file, it means that you want to help. Thank you for that 🤗 
Here is how to do that.

## Steps to make a pull request

1. Clone this github repo
2. Make changes
3. `make test` command must exit without errors
4. Add your name to [CONTRIBUTORS.txt](https://github.com/aio-libs/create-aio-app/blob/master/CONTRIBUTORS.txt) to leave a trace in history 😀
5. Make pull request
6. If you change some `ui` of project, do not forget to add a screenshot with the changes

```bash
git clone https://github.com/aio-libs/create-aio-app.git
cd create-aio-app   
pip install -r requirements-dev.txt

make test

cd project_new 
make

open http://localhost:8080
```

## Some possible ideas for the pull requests

 - [good first issue](https://github.com/aio-libs/create-aio-app/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) - list of easy issues with description on what is have to be done
 - [documentation](https://create-aio-app.readthedocs.io/) - documentation needs to be continuously improved 🧐
