## Exercise prep

If you haven’t got set up yet, see the [preparation instructions in the README](/README.md#prep-work-for-apprentices).

Note: explain difference between forking and using a template.  
  Share the exercise slide!  

--

## Exercise Part 1: Set up Travis CI

* Work in pairs
* Log into https://travis-ci.com with your GitHub account
* [Activate your repositories](https://app.travis-ci.com/account/repositories)
* You may need to confirm your Travis account in your email
* Check that you can see your repository in the list
* Activate Travis CI for your fork
* Subscribe to the free trial

Note:  
  You’ll be asked to authorise a Travis app  
  You can limit the repositories it has access to  
  Share the exercise slide!  

--

## Exercise Part 2: Configure your build

* On GitHub, create `.travis.yml` at root of repo
* Hopefully see your tests pass


```yaml
language: java
before_script: "cd exercises/java"
```
<!-- .element: style="font-size: 35%" -->

```yaml
language: csharp
solution: exercises/dotnet/TaxCalculator.sln
before_script: "cd exercises/dotnet"
mono: none
dotnet: "2.1.502"
script: 
  - "dotnet restore"
  - "dotnet test"
```
<!-- .element: style="font-size: 35%" -->

```yaml
language: node_js
before_install: "cd exercises/javascript"
node_js:
  - 10
```
<!-- .element: style="font-size: 35%" -->

```yaml
language: python
before_script: "cd exercises/python"
python: 
  - "3.6"
script: 
  - pytest
```
<!-- .element: style="font-size: 35%" -->

Note: Remind them about the dot at the front of the filename!  
  Share the exercise slide!  

--

## Exercise Part 3: Make it fail

* Pull down the changes (`.travis.yml`) you just made on GitHub
* Find the tests which aren't running (the ones for petrol vehicles)
* Make the tests run (and fail)
* Push your change
* Watch it fail

Note: Need to pull before you can push.  

--

## How does vehicle excise duty (vehicle tax) work?

+ How much tax you pay depends on a few things
+ In the first year it depends on the CO2 emissions and the fuel type
+ After the first year a ‘standard’ yearly rate applies depending on:
  + the fuel type 
  + the value (if it’s over £40,000)
+ There’s a detailed explanation on the [Auto Trader website](https://www.autotrader.co.uk/content/advice/car-tax-bands)

--

## Exercise Part 4: Make it pass

* Implement code to make **_only the petrol tests_** pass (see Story 1)
* ___***Do not change ‘DummyTaxCalculator’***___—write your own implementation (e.g. ‘DefaultTaxCalculator’)*
* Try to ___***keep your build green***___
* ___***Do not change the tests***___ (except to introduce your new calculator)
* Push your change and watch the build pass

**\*N.B. you'll need to set the year to `2019` in your `TaxCalculator` object**

Note: Did you get an email telling you it had failed?  
  Share the exercise slide!  

--

## Exercise Reflection

+ What do you think you actually set up?
+ How easy was it to set up?
+ How many commits did you make?
+ How does this contrast with your organisation?
