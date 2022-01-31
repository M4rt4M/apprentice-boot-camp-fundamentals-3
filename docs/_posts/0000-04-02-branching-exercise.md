## Exercise: setting upstream

* Create new local branch of this repository:
    ```
    git checkout -b tracking-test
    ```
* Check tracking branches:
    ```
    git branch -vv
    ```
* Try to push:
    ```
    git push
    ```
* Push and set upstream:
    ```
    git push -u origin tracking-test
    ```
* Check tracking branches again

Note: do this one together, as a group  
  Share the exercise slide!  

--

## Exercise prep: add a collaborator

* You are going to work in pairs
* Both need to push to the same repository
* ___***ONE***___ of you needs to add the other person as a collaborator:
    * Click Settings in your forked repository on GitHub
    * Choose ‘Manage Access’
    * Add your partner

Note: split off into rooms  
Share the exercise slide!  

--

## Exercise prep: change your remote

* The ___***OTHER***___ person needs to point their `origin` remote at your repository

```
git remote set-url origin https://github.com/[USER]/apprentice-boot-camp-fundamentals-3.git
```

--

## Exercise: Make changes on branches

* Work in pairs, ___***SHARE THE SAME GIT REPOSITORY***___
* Create two branches based on the same start point
  * `git checkout -b story_2`
  * `git checkout -b story_3`
* One person enables Story 2 tests & implements
* Other person enables Story 3 tests & implements
* Both add to your TaxCalculator implementation with regular commits, ___***BOTH CHANGE THE SAME FILE***___
* Merge branches back to master one by one
  * Use a GitHub PR or merge on the command line
* Check Travis after each push

Notes:
See branch ```petrol_tax``` for a starting point to this exercise if they haven't completed the previous one.  
N.B. don't get them to checkout the branch (git weirdness will ensue), just get them to copy-paste the working code.  
There are already test suites for these stories they just need to be enabled so the build runs them.  
When pushing they will need to run `git push --set-upstream origin story_2` etc  
Share the exercise slide!  

--

## Reflection

* What happened?
* Did you have any failed builds? If so, why?
* Did your changes conflict?

Note: Laptops closed.  
  These were very small changes.  
  Some changes last days… weeks…

--

<img src="images/merge.png">

+ GitHub can visualise your branches
+ Click ‘Insights’ then ‘Network’ on the left

Note: Created two branches  
  Merged diesel into master  
  Merged master into alternate  
  Merged alternate into master  

--

## git tree

+ Create command line text tree diagram to visualise branches
```
git log --oneline --decorate --all --graph
```
+ Also see `tig` which is interactive
  * `brew install tig`

---

<img height="600" src="https://wac-cdn.atlassian.com/dam/jcr:61ccc620-5249-4338-be66-94d563f2843c/05%20(2).svg?cdnVersion=kv">

Note: Git Flow: another branch based workflow  
