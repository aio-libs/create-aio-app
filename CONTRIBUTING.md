# Contributing to create-aio-app

If you open this file, it means that you want to help. Thank you for that 🤗 
Here is how to do that.

## Steps to make a pull request

1. Clone this github repo
2. Make changes

 > **Note**: _Please make commits according to topic "Conventional Commits", see below_

3. `make test` command must exit without errors
4. Don't forget to use `make changelog` command for generating CHANGELOG.md file
5. Add your name to [CONTRIBUTORS.txt](https://github.com/aio-libs/create-aio-app/blob/master/CONTRIBUTORS.txt) to leave a trace in history 😀
6. Make pull request
7. If you change some `ui` of project, do not forget to add a screenshot with the changes

```bash
git clone https://github.com/aio-libs/create-aio-app.git
cd create-aio-app   
pip install -r requirements-dev.txt

make test

cd project_new 
make

open http://localhost:8080
```

## Conventional Commits

A specification for adding human and machine readable meaning to commit messages. The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your application/library:

 1. **fix**: a commit of the type fix patches a bug in your codebase (this correlates with PATCH in semantic versioning).
 1. **feat**: a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in semantic versioning).
 1. **BREAKING CHANGE**: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with MAJOR in semantic versioning). A BREAKING CHANGE can be part of commits of any type.
 1. **types other than fix: and feat:** are allowed, for example @commitlint/config-conventional recommends build:, chore:, ci:, docs:, style:, refactor:, perf:, test:, and others.
 1. **footers other than BREAKING CHANGE**: <description> may be provided and follow a convention similar to git trailer format.

Example of conventional commit:

```
docs: add description of conventional commits to CONTRIBUTING.md file
```

Full description of [conventional commits specification](https://www.conventionalcommits.org/en/v1.0.0/).

## Some possible ideas for the pull requests

 - [good first issue](https://github.com/aio-libs/create-aio-app/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) - list of easy issues with description on what is have to be done
 - [documentation](https://create-aio-app.readthedocs.io/) - documentation needs to be continuously improved 🧐
