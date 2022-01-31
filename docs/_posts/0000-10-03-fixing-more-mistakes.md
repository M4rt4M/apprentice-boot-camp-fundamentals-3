## Fixing more mistakes

--

## Scenario

+ You pushed some changes
+ One of your changes caused tests to fail in the pipeline
+ You aren’t convinced you can quickly fix the test
+ You want to reverse what you did
+ What does ‘[git pretty](http://justinhileman.info/article/git-pretty/)’ say you should do?
  + `git revert {commit-hash}`

--

## Revert

+ Creates a new commit which negates a previous commit
```
git revert a18d33c
git revert HEAD~1
```
+ Old commit is still there in the history
+ You can always revert your revert

--

## Scenario

+ Your team uses branches and pull requests for code reviews
+ You made a change and committed it (yay)
+ You forgot to create a branch first (boo)
+ What does ‘[Dangit, Git!?!](https://dangitgit.com/)’ say you should do?
  ```
  git branch some-new-branch-name
  git reset HEAD~ --hard
  git checkout some-new-branch-name
  ```

--

## Scenario

+ You made a change and committed it
+ You forgot that yesterday you were working on a branch, and you didn’t switch to master before making your change
+ You want to move your changes to master
+ What does ‘[Dangit, Git!?!](https://dangitgit.com/)’ say you should do?
  ```
  git reset HEAD~ --soft
  git stash
  git checkout master
  git stash pop
  git add .
  git commit -m "New message"
  ```

Note: That’s complicated, so let’s go through it  

--

## What does reset do?

--

## Stashing your work

+ A bit like sticking stuff on the clipboard, like scratch commits
+ But… stashes go on a stack (FILO)
+ Push and pop things from the stack of stashes
  ```
  git stash
  git stash push -m "Some useful name"
  git stash list
  git stash pop
  ```

--

## Move changes to correct branch

For when you are forgetful, and commit changes to master when your team uses branches.

```
# undo the last commit, but leave the changes available
git reset HEAD~ --soft
git stash
# move to the correct branch
git checkout name-of-the-correct-branch
git stash pop
git add . # or add individual files
git commit -m "your message here";
# now your changes are on the correct branch
```

---

## Quick quiz

--

## What is a stash?

- A commit that doesn’t belong to a branch
- Saved changes that don’t belong to a commit
- Contents which will belong to the next commit
- Something that is best cut away before anyone sees

--

## How do you track a remote branch?

- `git set-upstream <remote> <branch>`
- `git push --set-upstream <remote> <branch>`
- `git push --u <remote> <branch>`
- `git push <remote> <branch>`

---

<!-- .slide: style="font-size: 80%" -->

## Exercise: git revert

1. In Terminal / Powershell, run ‘`cd exercises\git\basic-revert`’
1. Run ‘`./setup.sh`’ / ‘`./setup.ps1`’ then ‘`cd exercise`’
1. You can run ‘`cd ..`’ and go back to step 2 to start over at any point
* Using [docs](https://git-scm.com/docs/git-revert), try to do these steps in order with single commands:
  1. Create a new commit which reverses the last commit
  1. Find which commit added credentials
  1. Create a new commit which reverses that commit
    * Note that the credentials have disappeared from `HEAD` version

Hint: use ‘`cat greeting.txt`’, ‘`git status`’ and ‘`git log --oneline`’ to check progress

Note: [Revert Kata README](https://github.com/eficode-academy/git-katas/tree/master/basic-revert)
```
git revert HEAD
# observe result and
# find credentials commit hash
git log --oneline
git revert [credentials-commit-hash]
git log --oneline (show result)
```
Share the exercise slide!  

--

<!-- .slide: style="font-size: 75%" -->

## Exercise: git stash

1. In Terminal/Powershell, ‘`cd exercises\git\basic-stashing`’
1. Run ‘`./setup.sh`’ / ‘`./setup.ps1`’ then ‘`cd exercise`’
1. You can run ‘`cd ..`’ and go back to step 2 to start over at any point
1. Using [docs](https://git-scm.com/docs/git-stash), try to do these steps in order with single commands:
  1. Stash the work in progress (a mixture of staged/unstaged changes)
  1. Fix typos in bug.txt and commit (two steps)
  1. Look at what stashes are available
  1. Restore stashed changes without removing from the stack, resulting in a mixture of staged/unstaged changes again
    * You’ll need to supply an option to restore the state of the index
  1. Drop your stash and check it has gone (two commands)

Hint: use ‘`git status`’ and ‘`git stash list`’ to check progress

Note: [Stash Kata README](https://github.com/eficode-academy/git-katas/tree/master/basic-stashing)
```
git stash
vi bug.txt
git commit -am "Fix typos"
git stash list
git stash apply --index
git stash drop
git stash list
```
Share the exercise slide!  
