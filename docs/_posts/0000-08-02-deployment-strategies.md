## Deployment strategies

+ Blue Green
+ Canary
+ Ramped
+ Shadow
+ A/B Testing

--

## Blue green deployment

<img src=https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/graphics/fig10_2.jpg>

+ Two long lived environments exist—‘blue’ and ‘green’
+ Traffic routed to ‘green’ environment
+ New version deployed to ‘blue’ environment
+ Traffic switched to ‘blue’ environment
+ ‘Blue’ is now production
+ Either deploy new version to ‘green’ and switch back or perform next deployment to green

<small>Image credit [Continuous Delivery, Humble & Farley](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley-ebook/dp/B003YMNVC0)</small> 

--

## Blue green deployment pros/cons

+ 👍 Trivial to roll back (ignoring stateful apps)
+ 👍 Tests can be run against ‘blue’ environment before traffic switched
+ 👎 Uses twice the resources
+ 👎 Missed defects impact all users

Note: Point out that this can utilise existing redundancy.  

--

<backgroundimage>https://staticshare.america.gov/uploads/2014/11/canary_art22-1068x479.jpg</backgroundimage>
<backgroundimageopacity>0.25</backgroundimageopacity>

## Canary deployment

+ As in the canary in the coal mine
+ Feature released to small number of test users
+ Provides early warning sign
+ Released to 100% once confident
+ Sometimes called dark deployments
+ Similar to A/B Testing

<small>Image credit [State Department/Doug Thompson](https://share.america.gov/english-idiom-canary-coal-mine/)</small> 

Note: 
  You will always miss things and release defects/have issues in production.  
  Canary deployments are a technique to de-risk significant changes to production.  

--

<backgroundimage>https://staticshare.america.gov/uploads/2014/11/canary_art22-1068x479.jpg</backgroundimage>
<backgroundimageopacity>0.25</backgroundimageopacity>

## Canary deployment pros/cons

+ 👍 Visibility of problems before impacting everyone
+ 👍 Fast rollback
+ 👎 Takes longer to deploy
+ 👎 Can be hard to segment users
+ 👎 State can be hard to manage

--

## Ramped deployment

+ Naively replace/upgrade instances in serial
+ Traffic split across all instances
+ Possible to batch

--

## Ramped deployment pros/cons

+ 👍 Easy to set up
+ 👎 Slow
+ 👎 Risky to have multiple versions of the API / application available
+ 👎 Rollback is slow

--

## Shadow deployment

+ Version deployed without users being pointed at it
+ Realistic/duplicate traffic generated towards the new version
+ New version observed until confident
+ Traffic switched once confident

--

## Shadow deployment pros/cons

+ 👍 Real usage always beats scripted testing
+ 👎 Relies on manually monitoring or automating acceptance testing
+ 👎 Traffic might not be compatible with new version if the API has changed

--

## A/B Testing

+ Not really a form of deployment
+ Can be handled without changing deployment process
    + One version can present itself in different ways
+ Used to evaluate the impact of a change
+ Sometimes changes are prototypes
+ Users segmented and get different functionality based on their segment
+ Data gathered to inform decisions based on a statistically significant sample

--

## A/B Testing pros/cons

+ 👍 Real data to inform decisions
+ 👍 Can derisk significant changes
+ 👎 Can be hard to segment users—might require some investment
