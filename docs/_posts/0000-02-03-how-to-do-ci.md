## How to do Continuous Integration

--

## Important factors

+ Speed—short feedback loop
+ Reliability
+ Meaningful failures
+ Repeatability

--

## Good practices

+ Fix broken builds quickly (don’t commit over the top)
  + Be aware of failures—use notifications etc
+ Don’t ‘commit & quit’
+ You break it, you fix it
+ Fix or delete flaky tests (don’t just re-run)
+ Make sure your build stays fast
+ Keep test environment ‘like production’

Note: Some tests are unreliable—might fail 1% of the time.  
  Fast means 5 minutes or less for some positive feedback.  
  Test environment data is rarely comparible with production.  

---

## Typical Enterprise ‘Pipeline’

* Run fast tests
* Run slow tests and static analysis
* Publish packaged code
* Deploy to dev
* Deploy to test
* Deploy to production

---

## Many CI solutions

* Bamboo
* CircleCI
* CruiseControl.NET
* GitLab
* GoCD
* Jenkins
* TravisCI
* GitHub Actions (new)

Note: Enterprises tend to favour on site code and CI buy moving towards cloud hosted solutions.   

--

## Common Features

+ GitHub Integration
+ Support for describing work-flows of parallel tasks
+ Ability to run against multiple versions / variants
+ Publishing / releasing built artifacts
+ SCM support: Git / Subversion / CVS / etc.
+ Language / build tool support
+ Notifications
+ Configuration as code

---

## Upcoming Travis CI exercise

+ Not expecting you to have used Travis CI
+ Using it today in an exercise as an example
+ Partly as it is so easy to set up
+ We don’t use it other than this boot camp

--

## E.g. Travis CI

+ Authorise Travis CI to use your github.com account
+ Activate Travis CI with your repository
+ Add a `.travis.yml` file to your repository
+ Optional: add build badge to the repository

Note: GitHub Actions is the same, and you don’t even have to leave GitHub!

--

## Then…

+ GitHub tells Travis CI each time there is something to fetch and build
+ Travis fetches that version of the code
+ Travis works out what to run based on repository contents (including `.travis.yml`)
+ Travis reports status back to GitHub to mark commits with success/failure

--

## Build status

Status appears against each commit and PR.

<img src=images/travis-build-status.png>

--

## Configuring Travis

* Contents of `.travis.yml` tells Travis what to do
* Specific to each language… e.g.

```yaml
language: java
```

Note: Travis looks at repo to work out how to build once it knows language.  
  One line is enough to build and validate your Java.  

--

## Travis vs GitHub Actions

Travis:

```yaml
language: node_js
before_script: "cd exercises/javascript"
node_js:
  - 10
```
<!-- .element: style="font-size: 35%" -->

GitHub Actions:

```yaml
name: Node CI

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Read .nvmrc
      run: echo ::set-output name=NVMRC::$(cat .nvmrc)
      id: nvm
      working-directory: exercises/javascript
    - name: Setup node
      uses: actions/setup-node@v1
      with:
        node-version: '${{ steps.nvm.outputs.NVMRC }}'
    - name: npm install, build, and test
      run: |
        npm ci
        npm test
      working-directory: exercises/javascript
      env:
        CI: true
```

<!-- .element: style="font-size: 25%" -->

Notes: GitHub Actions is more verbose but seems more extensible

---

## Caution: Git

<img src="https://imgs.xkcd.com/comics/git.png">

<small>[XKCD](https://xkcd.com/1597/)</small> 
