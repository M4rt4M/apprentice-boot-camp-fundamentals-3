## Understanding some more Git terms

--

## Working copy

+ A copy of the repository
+ Contains much (if not all) of the history of the repository
+ What is the difference between working copy and repository?

Note: A repository will have many working copies

--

## Remote

+ A reference to a remote working copy
+ Might be a repo on github.com
+ Might be somewhere else
+ Remotes have names and addresses
  + What is origin?
  + What other remote names do we know?
+ View configured remotes with:
  ```
  git remote -v
  ```

--

## Fork (verb)

+ This is not a git term
+ When someone creates a linked working copy of a repo
+ A fork (noun) refers to the linked working copy 

--

## Clone

+ This is a git term!
+ How does cloning differ from forking? 
  + Creates an **unlinked** working copy from a remote
  + The new working copy is **local**

--

## Checkout

+ Switch current branch
+ Not to be confused with Subversion’s checkout command which fetches changes
+ Can create new branch in the process using `-b`
  ```
  git checkout master
  git checkout -b new-branch
  ```

--

## Fetch vs Pull

+ Fetch retrieves but does not apply changes (from a remote)
+ Pull fetches AND merges by default
  + With `--rebase` it rebases instead of merging

---

## Quick quiz

--

## How do see what remotes you have?

* `git show remotes`
* `git remote list`
* `git remote ls`
* `git remote -v`
* `git remotes`

Note: `git remote -v`

--

## How do you create a new branch and switch to it?

* `git checkout new-branch`
* `git checkout -b new-branch`
* `git branch new-branch`
* `git branch -n new-branch`
* `git switch -c new-branch`

Note: `git checkout -b new-branch` and `git switch -c new-branch`

--

## What does `git pull` do?

* Applies changes you’ve fetched
* Fetches and applies changes
* Fetches and merges
* Fetches and rebases

Note: Fetches and applies changes  
Also Fetches and merges
Doesn’t rebase unless you say --rebase