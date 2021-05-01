# Contributing to create-aio-app

## Table of Contents

1. [Steps to make a pull request](#steps-to-make-a-pull-request)
2. [Conventional Commits](#conventional-commits)
3. [Managing releases in a repository](#managing-releases-in-a-repository)
4. [Some possible ideas for the pull requests](#some-possible-ideas-for-the-pull-requests)

If you open this file, it means that you want to help. Thank you for that 🤗 
Here is how to do that.

## Steps to make a pull request

1. Clone this github repo
2. Make changes

 > **Note**: _Please make commits according to topic "Conventional Commits", see below_

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

## Conventional commits

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

## Managing releases in a repository

> **Note:** This part applies only to users who can do releases

Creating a new release contains the following steps:

1. [Prepare release branch](#prepare-release-branch)
2. [Final updates](#final-updates)
3. [Merge release branch to master](#merge-release-branch-to-master)

In this example, we assume that the latest release was v0.0.9

### Prepare release branch
The short description types of release according to [semantic versioning](https://semver.org/):

 - patch release: v0.1.9 to v0.1.10, only for bug fixes
 - minor release: v0.1.9 to v0.2.0, contains bug fixes, new features that maintain backwards compatibility
 - major release: v0.1.9 to v1.0.0, contains bug fixes, new features that can break backwards compatibility 

#### Creating release branch

##### Patch release

Create a new release branch from the latest release tag

```
git checkout tags/v0.0.9 -b release_v0.0.10
```

If `<branch_name>` consists bug fixes that need to go in this patch release, we need to cherry pick corresponding pull requests and apply them to the release branch

##### Major or minor releases
For example, the branch `issue-98` contains all changes for a new release, we need to create release branch from this one

```
git checkout origin/issue-98 -b release_v0.1.0
```

#### Pushing the release branch to git

If you have prepared release branch locally, push it to git

```
git push origin release_v0.1.0
```

### Final updates

One of the last steps before creating release you need to update `CHANGELOG.md` file in the release branch. Please use `make changelog` command for generating CHANGELOG.md file.

### Merge release branch to master

Merge release branch to master via a pull request. Make sure that the `release_v0.1.0` branch is up to date.

## Some possible ideas for the pull requests

 - [good first issue](https://github.com/aio-libs/create-aio-app/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) - list of easy issues with description on what is have to be done
 - [documentation](https://create-aio-app.readthedocs.io/) - documentation needs to be continuously improved 🧐
