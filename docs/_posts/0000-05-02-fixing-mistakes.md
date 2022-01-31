## Fixing mistakes

--

## Using Git is hard

+ It is hard to know how to fix things
+ We *all* get stuck from time to time
+ Useful resources can help you when you are stuck
+ Good to practice some of the techniques

--

<img src=https://rakhim.org/images/honestly-undefined/git.jpg>

<small>Source: [rakhim.org](https://rakhim.org/honestly-undefined/13/)</small>

--

## [Git Pretty](http://justinhileman.info/article/git-pretty/)

<img src=http://justinhileman.info/article/git-pretty/git-pretty.png>  <!-- .element width="50%" -->

--

## [Dangit, Git!?!](https://dangitgit.com/)

Written site with more detailed instructions about how to resolve problems

<img src=images/dangitgit.png>  <!-- .element width="50%" -->

--

## [Atlassian tutorial](https://www.atlassian.com/git/tutorials/undoing-changes)

Super long word documentation with lots of explanation about how to undo stuff

--

<background>https://i.pinimg.com/originals/bf/c6/3a/bfc63af24e16b3d8103ddae2e60085c5.gif</background>
<backgroundimageopacity>0.5</backgroundimageopacity>

## All that said… 

Sometimes it is easier to start again

`rm -rf apprentice-boot-camp-fundamentals-3`  
`git clone https://github.com/MCR-Digital/apprentice-boot-camp-fundamentals-3.git`

Notes: It can be slower to fix it properly, but it can be an opportunity to learn too—balance learning and progress

--

## Scenario

+ Your tests are failing
+ When you committed the tests were passing
+ You’ve no idea how to get them working
+ You committed quite a long time ago
+ What does ‘[git pretty](http://justinhileman.info/article/git-pretty/)’ say you should do?
  + `git reset --hard`

--

## Reset

+ Takes a commit, but this defaults to current HEAD
+ Changes the value of HEAD to specified commit and unstages files
  ```
  git reset
  ```
+ Can throw away local changes too, if we tell it to
  ```
  git reset --hard
  git reset --hard HEAD~1
  ```

--

## Scenario

+ You just committed (yay)
+ You forgot to update the message (boo)
+ You realised before you pushed your changes (yay)
+ What does ‘[git pretty](http://justinhileman.info/article/git-pretty/)’ say you should do?
  + `git commit --amend`
+ What if we forgot to add a new file?
  + `git add {file}`
  + `git commit --amend`

--

## Amend your last commit

+ Amend changes (replaces) the last commit
+ Why is it replacing the last commit?
  + Commits are immutable
+ The previous commit is not actually removed
+ What happens to `HEAD`?
+ Most often used to change the message
```
git commit --amend -m "Add new message here"
```

--

## Add to your last commit

+ Staging files before amending allows you to change the contents
+ You don’t have to change the message
```
git add .
git commit --amend --no-edit
```

--

<!-- .slide: style="font-size: 80%" -->

## Detached HEAD 🤯

```
You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

```

--

## Reattaching your HEAD 💆🏻

+ `git checkout` usually used to switch branches
+ Also accepts commit hashes
  + `HEAD` no longer points to the tip of a branch
+ Why might you checkout a commit?
  + Look at some code
  + Try running the tests
  + Create a branch from a historical commit
+ Reattach `HEAD` by checking out your branch again
  ```
  git checkout master
  git checkout my-branch
  ```

---

## Quick quiz

--

## What git command changes the last commit message?

- `checkout`
- `apply`
- `log`
- `amend`
- `add`
- `yolo`

Note: amend  

--

## How would you use git to restore changed tracked files to their last committed state

- `git revert`
- `git revert --soft`
- `git reset --hard`
- `git reset --hard HEAD~1`
- `rm -rf`

Note: git reset --hard  

--

## How do you get out of detached head mode?

- Following the advice in your terminal
- `git reset --hard`
- `git checkout`
- `git checkout master`
- `git reset --hard HEAD`
- `git branch bug-fix`
- `git staple neck`

Note: git revert --hard  

---

<!-- .slide: style="font-size: 80%" -->

## Exercise: git reset

1. In Terminal / Powershell, run ‘`cd exercises\git\reset`’
1. Run ‘`./setup.sh`’ / ‘`./setup.ps1`’ then ‘`cd exercise`’
1. You can run ‘`cd ..`’ and go back to step 2 to start over at any point
* Using [docs](https://git-scm.com/docs/git-reset), try to do these steps in order with single commands:
  1. Move HEAD to commit ‘9’, leaving file ‘`10.txt`’ being staged for commit
  1. Move to commit ‘8’, leaving files ‘`9.txt`’ and ‘`10.txt`’ being untracked
  1. Move to commit ‘7’, leaving ***only*** files ‘`9.txt`’ and ‘`10.txt`’ being untracked

Hint: use ‘`git status`’ and ‘`git log --oneline`’ to check progress

Note: [Reset Kata README](https://github.com/eficode-academy/git-katas/tree/master/reset)  
```
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
```
Share the exercise slide!  

--

<!-- .slide: style="font-size: 80%" -->

## Exercise: git commit --amend

1. In Terminal / Powershell, run ‘`cd exercises\git\amend`’
1. Run ‘`./setup.sh`’ / ‘`./setup.ps1`’ then ‘`cd exercise`’
1. You can run ‘`cd ..`’ and go back to step 2 to start over at any point
* Using [docs](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend), try to do these steps in order with single commands:
  1. Examine the most recent commit using ‘`git log -p`’
  1. Amend the commit to include file ‘`bar.txt`’ without changing the message (two commands)
  1. Examine the most recent commit using ‘`git log -p`’
  1. Change the previous message

Hint: use ‘`git status`’ and ‘`git log --oneline`’ to check progress

Note: [Amend Kata README](https://github.com/eficode-academy/git-katas/tree/master/amend)
```
git log -p
git add .
git commit --amend --no-edit
git commit --amend --m "new message"
```
Share the exercise slide!  

--

<!-- .slide: style="font-size: 80%" -->

## Exercise: detached head

1. In Terminal/Powershell, ‘`cd exercises\git\detached-head`’
1. Run ‘`./setup.sh`’ or ‘`./setup.ps1`’ then ‘`cd exercise`’
1. You can run ‘`cd ..`’ and go back to step 2 to start over at any point
1. Read the message you got, then try to do these steps in order with single commands:
  1. Reattach HEAD to the tip of the master branch
  1. Detach the HEAD from the branch and look at commit ‘A’
  1. Create a new branch called ‘`mirror`’ and switch to it
  1. Create a file called mirrorfile
  1. Stage your new file and commit it (two commands)
  1. Examine the structure of the branches

Hint: use ‘`git status`’ and ‘`git log --oneline --graph --all`’ to investigate

Note: [Detached Head Kata README](https://github.com/eficode-academy/git-katas/tree/master/detached-head)
```
git checkout master
git log -p (find hash of ‘A’)
git checkout [commit-hash-of-a]
git checkout -b mirror OR git switch -c mirror
touch mirrorfile
git add mirrorfile
git commit -m "Add mirrorfile"
git log --oneline --graph --all
```
Share the exercise slide!  
