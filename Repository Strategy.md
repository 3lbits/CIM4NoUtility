# digin-best-practice

This repository contains best practices for work performed in the digin github organization.

## Contributions

Anyone is welcome to contribute to this repository by opening a pull request with the desired changes with detailed documentation on the changes made. When creating this pull request please follow the branching strategy defined here

# Branching strategy for DIGIN projects

We fully adapt the git flow methodology, specifically the branch strategy for working on features, bugfixes, releases and hotfixes. For a walkthrough of this git strategy refer to the following site. We have 2 longlasting branches that contain the main code/data, develop and main, which are protected against code pushes into the Github repository. The different naming standards are used to indicate the purpose of a branch, which means that one should be able to identify what is being developed by looking at the branch names. Additions to the default naming standard can be considered on a repository by respository basis as long as the additional branch formats adds value to the development process.

Note that in some older repos master is used instead of main. This is due to standards that have since been changed. New repos should always use main.

## Branch overview

| Branch Format   | Lifetime  | Protected  | Purpose                                                                                                                                                           |
|:----------------|:----------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```main```      | Long      | Yes        | Contains the currently released code/data                                                                                                                         |
| ```develop```   | Long      | Yes        | Contains the unreleased code                                                                                                                                      |
| ```release/```  | Short     | No         | Contains the unreleased code that is being polished before release. This branch is optional                                                                       |
| ```feature/*``` | Short     | No         | Used to develop new changes to the develop branch                                                                                                                 |
| ```bugfix/*```  | Short     | No         | Used to develop fixes for bugs or errors in the development branch                                                                                                |
| ```hotfix/*```  | Short     | No         | Used to develop important fixes that need to be released as soon as possible. Suggested through Pull Request to main and then a merge to develop from main        |

```*``` in the branchformat above is to be replaced with a good description of the changes introduced in the branch. For example ```feature/add-documentation-to-endpoint-x``` and ```bugfix/remove-exception-while-importing-only-one-line```.

Long = exists forever, and is never erased. Should be protected.
Short = when the pull request to ```develop``` / ```main``` is approved and **squash-merged/merge** committed in, or not approved and Pull Request is closed, then the branch is deleted from the server. History is in the Pull Request discussion.

## Merge strategy

Into ```develop```:
All Pull Requests shall be **squash-merged** in. This means that all commits are squashed into a single main commit in the commit history for develop and thus the history becomes linear and clear. This creates a easy reading experience where it is easy to see what was added at any given time. Each commit links back to the pull request where it was added, for times where detailed review is useful.

Into ```main``` from ```develop```/```release```/:
All Pull Requests to ```main``` are merged with **merge commits**. In this way, the history is preserved into ```main```, but the history is marked with when new changes were introduced through the merge commit. This makes the history of main easy to read and understand by showing when changes where made to the ```main``` branch. If you have accidentally used squash-merge a clean up procedure is required.

```hotfix/*``` into ```main```:
Pull Requests for hotfixes to ```main``` are merged in through a **squash-merge**. This is performed to reduce all the commits made in the hotfix to one single entry in the commit log on the ```main``` branch. This is done to avoid clutter in the commit history. Then ```main``` can be merged into ```develop``` to deploy the hotfix to dev aswell.

# Guide to creating new repositories on Github

This guide is for administrators on Github which details how to create new repositories. The main purpose is to outline all the important settings that should be enabled to ensure high quality. The rules can in certain circumstances be omitted if the rules applied here are prohibiting an optimal workflow (however best practice is to follow this guide).

## 1. Creating a repository

### 1.1 Naming convention

Repositories should follow a common naming convention.

>**Note**: Make sure to create the repository in the ```digin-energi``` organization.

### 1.2 Assign a concise description

Every repository shall have a concise and appropriate description. This description should contain a short text detailing what the contents of the repository is, which should enable anyone to decide if the repository is relevant for them or their search.

### 1.3 Visibility

Repositories should by default be created as internal. If the project at hand has specific needs, then other visibility options can be considered. This can for instance be if the repository is to be available to the public or contains information that is not suitable to be shared with the entire organization. One important thing to consider is that a few of the options later in this guide requires either a public repository or licenses for every member of the repository.

> Visibility 101: <br/>
</br>
**Public** - Everybody on the entirety of the internet can see the repository. This means that all changes, the emails used to commit, code and data is available to the public (not exhausted list). <br/>
</br>
**Internal** - Everybody in the digin-energi enterprise account will be able to see the repository.<br/>
</br>
**Private** - Only people with assigned read or higher access can access the repository.</br>
</br>
For further information please refer to the Github explaination.

### 1.4 Instanciating repositories

> **Note**: Creating repositories from templates is prefered over manually re-creating a repository.<br/>
  **Note 2**: Skip this step if importing a repository from another source.

Review the available templates and choose one that is suitable.

If no suitable templates are available, then create a new repository. The created repository should contain a relevant gitingore for the contents of the repository aswell as a readme file further detailing what is in this repository and how to use it.

## 2. Settings

Navigate to the ```Settings``` tab in the newly created repository.

### 2.1 Features

Make sure that the feature section is entered as shown below.

* [ ] Wikis
* [x] Issues
* [x] Allow forking
* [ ] Sponsorships
* [ ] Projects

### 2.2 Merge Button

* [x] Allow merge commits
* [x] Allow squash merging
* [x] Allow rebase merging
* [x] Automatically delete head branches

## 3. Team access

Navigate to ```Manage Access``` in the settings menu.

### 3.1 Assign access

Assign the access to the desired teams or individuals. Repository owners are assigned ```maintain``` access, while developers are assigned ```write``` access.

## 4. Branch protection

Navigate to ```Branches``` in the settings menu. Using ```Add Rule``` we can assign branch protection rules for the different branches.

Branch protection is a necessary step to maintain the quality of the performed work. It is therefore essential to turn on as early as possible.

We want to protect the branches with long lifetime such as ```main``` and ```develop```.

### 4.1 Default branch

The default branch shall be set to ```develop```. This ensures that changes by default are deployed to the long life branch that is under development.

> **Note**: If ```develop``` does not exist, then it can simply be created from the front page of the repository.

### 4.2 ```main``` (previously ```main```) branch protection

This branch contains the stable/released code/data. It is therefore essential to have protection against unwanted commits or releases.

In the branch format field the value ```main``` is inputed.

Settings to be applied to the ```main``` branch.

* [x] Require pull request reviews before merging
* [x] Dismiss stale pull request approvals when new commits are pushed
* [x] Require review from Code Owners
* [x] Require status checks to pass before merging
* [ ] Require branches to be up to date before merging
* [ ] Require signed commits
* [ ] Require linear history
* [x] Include administrators
* [x] Restrict who can push to matching branches
* [ ] Allow force pushes
* [ ] Allow deletions

### 4.3 ```develop``` branch protection

This is the long lasting branch under development. New functionality is continously added untill one is ready to release.

In the branch format field the value ```develop``` is inputed

Settings to be applied to the ```develop``` branch.

* [x] Require pull request reviews before merging
* [x] Dismiss stale pull request approvals when new commits are pushed
* [x] Require review from Code Owners
* [x] Require status checks to pass before merging
* [x] Require branches to be up to date before merging
* [ ] Require signed commits
* [x] Require linear history
* [x] Include administrators
* [ ] Restrict who can push to matching branches
* [ ] Allow force pushes
* [ ] Allow deletions
