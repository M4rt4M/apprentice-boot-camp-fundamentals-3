## Continuous Delivery & Deployment

Structure:

+ What is it?
+ Why is it important?
+ How do we do it?

Note: Laptops closed.  
  Ask people what they think it means  

--

## What is Continuous Delivery?

--

> “Continuous delivery … is a software engineering approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time and, when releasing the software, doing so manually. It aims at building, testing, and releasing software with greater speed and frequency  
> …

--

> “…  
> The approach helps reduce the cost, time, and risk of delivering changes by allowing for more incremental updates to applications in production. A straightforward and repeatable deployment process is important for continuous delivery.  
> …”

--

> “CD contrasts with continuous deployment, a similar approach in which software is also produced in short cycles but through automated deployments rather than manual ones.”  
> —<cite>[Wikipedia](https://en.wikipedia.org/wiki/Continuous_delivery)</cite>

--

> … teams produce software in short cycles …

Note: Just like our CI definition says several times a day…  
  Could be every five minutes, could be every two hours.  

--

> … ensuring that the software can be reliably released at any time …

Note: At any time means when code is pushed.  
  CI says “verified by an automated build”  
  Automated verification helps with this  
  Further: must be usable/desirable  
  Features should be complete or hidden  
  Going to focus on this  

--

> … when releasing the software, doing so manually …

Note: Manually triggering an automated process vs an automatic process.  

---

<img src="images/continous-integration-delivery-deployment.svg">

Note: Explain push from CI to CD  
