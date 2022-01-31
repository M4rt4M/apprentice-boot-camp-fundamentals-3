## Continuous Deployment safety

--

<img src="images/continous-integration-delivery-deployment.svg">

Staying safe involves practices at each step of the journey to production.

--

## Techniques involved

+ ***Release safety***
  + Minimising change
  + How to work on multiple changes at the same time
+ Automated testing
+ Automated packaging
+ Automated deployment
+ ***Deployment strategies*** (Risk mitigation)
+ Observation and support

Notes: Today talking about the highlighted points.    
  Other boot camps will cover the other parts.  

---

## Release safety

+ Smaller deployments are safer
+ Less to test in one go
+ Fewer suspects when investigating issues
+ Earlier visibility of problems

Note: Kinder to testers—less context to remember.  

--

## Working on multiple changes 
### Trunk vs Branch

+ Two different ways to make sure you don’t release incomplete changes
+ As usual this is a subjective issue
+ Each has pros and cons 

--

## What is a branch?

+ Formed when two commits have the same parent
+ Commits made against the branch your working copy points to

--

<img src="https://www.atlassian.com/dam/jcr:746be214-eb99-462c-9319-04a4d2eeebfa/01.svg">

Note:
Explain the diagram:
time goes left to right
circle = commit
lines are branches

--

## What is trunk?

+ Trunk is another term for master
+ It is a special branch

--

## What is a working copy?

+ Your local clone is a working copy
+ Working copy ≠ branch
+ The copy can consist of multiple branches
