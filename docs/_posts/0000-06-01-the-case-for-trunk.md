## The case for trunk based development

+ Everyone works on ‘master’
+ Changes regularly pushed back to origin
    + Ideally multiple times a day
+ Some people say using short lived feature branches still counts 

Note: Reminder: opinion follows  

--

## Benefits of TBD

+ 👍 No one likes merging
    + Frequently people not great with branches
+ 👍 Fewer conflicts reduces overhead
+ 👍 Still get conflicts but they are smaller
+ 👍 Earlier visibility of conflicts
    + Can back off from stepping on each others toes

--

> Branching is not the problem, merging is the problem.
> —Jez Humble

--

## How is work in progress handled?

+ Feature Toggles hide incomplete features in production
+ AKA Feature Shields/Flags/Switches/Flippers
+ Conditionals around bits of code/user interfaces
+ May be toggled on and off per environment or per test
+ (see Further Reading for a good [Feature Toggles article](https://martinfowler.com/articles/feature-toggles.html))

--

## Trunk Development + CI == 👍

+ All CI systems can work with trunk
+ Therefore… CI will always test trunk changes

--

## But my CI system handles branches…

+ Many do these days
+ CI is more than just testing on another machine
+ Integrating code means bringing changes together
+ They are integrated until they are on the same branch
+ Argued that branching means you aren’t doing CI

--

## How is testing accomplished?

+ Features are hidden
+ Have to toggle features on per environment (or per test)
+ If you do, feature is tested on each push
+ Increased complexity—introduces a new code path
+ May need to run tests with multiple toggle combinations
    + Combinations might be unmanageable

---

## Implementing a Feature Toggle

```javascript
  const features = fetchFeatureTogglesFromSomewhere();

  function generateInvoiceEmail(){
    const baseEmail = buildEmailForInvoice(this.invoice);
    if( features.isEnabled("next-gen-ecomm") ){ 
      return addOrderCancellationContentToEmail(baseEmail);
    }else{
      return baseEmail;
    }
  }
```

Taken from [Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html)

---

## Practical example

Review `FeatureToggleExampleTest` which explores feature toggles and Bowling Kata.

--

## Disadvantages

+ 👎 Extra process around creating toggles 
+ 👎 Feature toggles need to be tidied up once functionality fully released 
+ 👎 Developers need to be disciplined and trusted 
+ 👎 Can’t see whether code has been reviewed without merging 
    + Pairing helps
    + Can use simple dev branch model to mitigate this
        + But then all same arguments apply…
+ 👎 Need to be more careful not to break the build! 
