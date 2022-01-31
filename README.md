<!--- ORGANISER THINGS TO CONSIDER 
- Which technical competencies, behaviours and knowledge module topics does the bootcamp cover/meet
- Structuring retros so that they can inform thinking for individual's personal learning records (off the job training record tab in their learning logs)
- Introducing some sort of test or quiz on basic concept learning points from the bootcamp to validate that they have taken stuff in, and provide organisation mentors with results to help them focus follow ups
--->

## Competencies, Behaviours and Knowledge units

These relate to the KSBs defined in the [Level 4 Software Developer standard](https://www.instituteforapprenticeships.org/apprenticeship-standards/software-developer-v1-1).

* **S1**: create logical and maintainable code
* **S4**: test code and analyse results to correct errors found using unit testing
* **S12**: follow software designs and functional or technical specifications
* **S10**: build, manage and deploy code into the relevant environment
* **S14**: follow company, team or client approaches to continuous integration, version and source control
* **S14**: follow company, team or client approaches to continuous integration, version and source control

## Resources 

* Slides
* Laptops
* Internet access
* Post-its
* Pens
* Whiteboard

## Mentors / Languages
 
Two–three mentors required in addition to leads. These should be able to cover support for the required languages.

Exercises (katas and code starters) will need to be ported to required languages.

Mentors should be comfortable with branching, feature toggles, setting up Travis for their chosen language.

## Prep-work for apprentices

* Make sure you can sign in to github.com with your own account by signing out and signing in again
* Open [the template repo](https://github.com/MCR-Digital/apprentice-boot-camp-fundamentals-3/) and click ‘Use this template’
* Clone your repo: `git clone https://github.com/[your-username]/apprentice-boot-camp-fundamentals-3.git`
* Follow the instructions in the README for your language under the `exercises` directory, **making sure you can run the tests** (which are all ignored)
  * [Java](exercises/java/README.md)
  * [JavaScript](exercises/javascript/README.md)
  * [C#](exercises/dotnet/README.md)
* It’s normal to have problems with this, so just let us know! :)

### Follow-on tasks

Organisation mentors should look to exercise the knowledge we’ve covered in the boot camp. Below are suggestions for tasks that would do this, but please use your own judgement to work out what to do. There is no need for anything to be returned to MD or the presenters—it’s just a learning exercise.

* Find out what CI systems the organisation uses
* Find out how the team works with branches and discuss this with your mentor
* Find out how the team deploys code and manages releases to mitigate risk

## Further reading / learning resources

### CI/CD

* Five minute read: [Continuous Integration by ThoughtWorks](https://www.thoughtworks.com/continuous-integration)
* Book: [Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley-ebook/dp/B003YMNVC0) by Jez Humble and David Farley
* [Feature Toggles](https://martinfowler.com/articles/feature-toggles.html) by Pete Hodgson at ThoughtWorks
* [Knightmare: A DevOps Cautionary Tale](https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/) about Knight Capital disaster
* [The Cathedral and the Bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/)
* [Six Strategies for Application Deployment](https://thenewstack.io/deployment-strategies/)
* [Trunk Based Development](https://trunkbaseddevelopment.com/) is a whole site dedicated to explaining TBD

### Git

* [Git Pretty](http://justinhileman.info/article/git-pretty/) is a flow chart that helps you fix git messes
* [Dangit, Git!?!](https://dangitgit.com/) is a written site with more detailed instructions about how to resolve problems
* [Git-it](https://github.com/jlord/git-it-electron) is a desktop (Mac, Windows and Linux) app that teaches you how to use Git and GitHub on the command line.
* This [Atlassian git tutorial](https://www.atlassian.com/git/tutorials/undoing-changes) is also a useful resource on undoing changes
* [Git for Teams](http://gitforteams.com/) is has a book and some video aimed at helping you create a workflow strategy with your team, and learn to use Git
* [git-katas](https://github.com/eficode-academy/git-katas/) has a bunch of exercises that we’ve dipped into in this boot camp to practice git learning
* [Learn Git Branching](https://learngitbranching.js.org/) is a git repository visualizer, sandbox, and a series of educational tutorials and challenges. It helps you understand git through visualising what you do.
* [CS Visualized: Useful Git Commands](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1) has some great animations which help bring git commands to life by visualising what is happening

## Slides

The slides can be viewed from the link at the top of the repository. Hit ‘`?`’ to see navigation controls.

## Exercises

* Setting up Travis CI, changing tax_calculator & watching Travis fail/pass
* Changing tax_calculator using feature branches
* Changing tax_calculator using trunk development and feature toggles
* Git: reset
* Git: amend
* Git: detached head
* Git: revert
* Git: stash

# Boot Camp Summary

* Continuous Integration
  * What it is and why we do it
  * Examples of different CI systems
  * Exercise: add Travis to fork of existing repo
  * Exercise: Make change to their fork and show (hopefully) successful build
* Continuous Delivery/Deployment
  * What it is and why we do it
  * Benefit of fast feedback—small/fast deployments
* Branch based development
  * What is a branch
  * Explain feature branching and pull requests
  * Exercise: Get them to make two changes using feature branches
* Trunk based development
  * What is a feature shield
  * Exercise: Get them to implement a feature shield
* Comparison of approaches

# Briefing for organisation mentors

* Review the summary above
* Have a go at the exercises to get a gist for the
    * Exercises are described in the slides linked to at the top of the repo
    * Code for the exercises is in the `exercises` directory
* On the day get involved when they are doing the exercises and help them when they get stuck
* Ask them open questions about what they are doing
  * Ask to see what they’ve done
  * Start with the tests
* Help resolve language specific issues
* Coach them towards finding their own solutions rather than fixing things for them

# Git kata exercises

The git exercises are included as a git subtree from https://github.com/eficode-academy/git-katas.git. **It is best not to update them** unless you are familiar with maintaining changes to subtrees. To fetch changes from the origin, run `git subtree pull --prefix exercises/git https://github.com/eficode-academy/git-katas.git master --squash`.

# Working with the slides

The slides are stored as Markdown files in `docs/_posts` and are presented using a combination of Jekyll and [reveal.js](https://revealjs.com/#/). A [remote Jekyll theme](https://github.com/autotraderuk/jekyll-revealjs) is used to help make changes to the Jekyll code centrally.

The easiest way to preview your changes locally is to use docker to run Jekyll. To do this, [install docker](https://www.docker.com/get-started) if you haven’t already and run `docker-compose up` from the root of this project in a terminal. Your changes will be visible on <http://localhost:4000/>. Any changes you make to the slides will be reflected in your browser—there’s no need to restart docker. You can hit `ctrl-c` to stop the process.

Once you push your changes the slides will be published using GitHub Pages automatically (see the link at the top of the repository).
