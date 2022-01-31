## A cautionary tale

[Knightmare: A DevOps Cautionary Tale](https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/)

--

## Knight Capital (traders) had $365M in assets

--

## Deployment of new feature was incomplete

💻 ✅ 💻 ✅ 💻 ✅ 💻 ✅ 💻 ✅ 💻 ✅ 💻 ✅ 💻 ❌

Note:   
  One server (of eight) had not been updated by a human  
  Server running 8yr old code hidden by now reused toggle  

--

## New feature reused eight year old feature toggle

🤓 🤓 🤓 🤓 🤓 🤓 🤓 😡

Note:
  Single server had old behaviour activated instead  
  That server followed a different strategy

--

## 09:30 Market opens

<fragment/> (09:31 Market panics)

Note: Market saw problem in by 09:31—one minute after opening  
  No kill switch  

--

## Deployment backed out

(toggle left on)

😡 😡 😡 😡 😡 😡 😡 😡

Note:  
  Back out left resulted in eight bad servers—4 million transactions  

--

## $460 million loss over in 45 minutes

Bankrupt!

<img src=https://miro.medium.com/max/1240/1*-BDqsaWVHxONCnnJI3PetQ.jpeg>

<small><caption>[Source](https://medium.com/dataseries/the-rise-and-fall-of-knight-capital-buy-high-sell-low-rinse-and-repeat-ae17fae780f6) (origin unknown)</caption></small>

--

## Exercise: discuss what lessons should be learned (5 minutes)

* Split into small groups of about three
* Discuss what happened
* Note down 3–4 lessons that should be learned

Note:
  Share the exercise slide!  

--

## What should we learn?

+ Don’t reuse feature toggles
+ Delete redundant code
+ Humans make mistakes
+ Deployments should be automated, reliable and consistent
+ Risky changes should be easily deactivated

Note: Get them to call out what they wrote down  
