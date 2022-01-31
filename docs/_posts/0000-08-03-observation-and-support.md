## Observation and Support

What happens after deploying?

+ Acceptance tests
+ Graphs and charts
+ Checking logs and metrics
+ Responding to alerts
+ Automated user journeys

Note: Ask the group for things they are aware of happening.  
    Important techniques to learn, part of dev responsibility.  
    Importance of trust between dev and ops.  

--

## Testing in production

+ Used to be considered irresponsible
+ Inevitably happens anyway
+ Not a replacement for testing sooner
    + Fast feedback still better than slow
+ Test data can never beat real users

--

## RUM vs Synthetic

+ Real User Monitoring
    + Page Load Time
    + Conversions
    + E.g. Google Analytics, Contentsquare
+ Synthetic
    + Configured tests run continuously
    + E.g. ThousandEyes, Eggplant

--

## Good Logging

+ Logs very important when things go wrong
+ Importance of context
+ Keep noise down
    + Use log levels carefully
    + Errors should require human intervention, explain impact and how to resolve