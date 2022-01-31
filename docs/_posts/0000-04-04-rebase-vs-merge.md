## Rebase vs Merge

+ Can of worms
+ Sorry, not sorry
+ Cause of most problems with git

--

(feature is current branch)  
`git merge master`

<img src=https://wac-cdn.atlassian.com/dam/jcr:e229fef6-2c2f-4a4f-b270-e1e1baa94055/02.svg?cdnVersion=766><!-- .element width="75%" -->

Note: This is what merging looks like  

--

## git merge

+ Merge creates special commit with two parents
+ Joins two branches
+ No commits were destroyed in the making of this commit… history is preserved
+ Some people see extra commits as pollution

--

`git rebase master feature`

<img src=https://wac-cdn.atlassian.com/dam/jcr:5b153a22-38be-40d0-aec8-5f2fffc771e5/03.svg?cdnVersion=766>  <!-- .element width="75%" -->

Note: This is what rebasing looks like  

--

## git rebase

+ No extra commits
+ Reattaches your branch to the tip of another branch
+ Rebasing locally results in linear history
+ Changes history

--

<background>https://24.media.tumblr.com/8e09bcd941594205f9cb42f1821c1743/tumblr_mrwjtemvHR1qfr6udo1_500.gif</background>
<backgroundimageopacity>0.5</backgroundimageopacity>

> … the encounter could create a time paradox, the results of which could cause a chain reaction that would unravel the very fabric of the space time continuum, and destroy the entire universe!
> Doc Brown—Back to the Future Part II

--

<img src=https://wac-cdn.atlassian.com/dam/jcr:1d22f018-b2c7-4096-9db1-c54940cf4f4e/05.svg?cdnVersion=766><!-- .element width="75%" -->

--

## The Golden Rule of Rebasing

***Never rebase on public branches!***

+ Possible to end up with commits appearing multiple times
+ Might not be able to push
+ Might be told you need to force push… don’t!

Note: Fine to rebase from the remote branch  
Bad to rebase onto master then attempt to push  

--

## Don’t use the `--force`!

+ Force push is destructive
+ Almost always the result of trying to get out of a previous mistake
+ Overwrites remote history
+ Breaks other peoples’ working copies
+ Only do it to your private branches
+ Might be disabled in your organisation, or just on master

---

## Quick quiz

--

## What does rebase do?

- Places incoming commits after your commits
- Fetches changes and merges them in
- Moves your commits to a new branch
- Places your commits after incoming commits
- Makes you unpopular

Note: Places your commits after incoming commits

--

## When is it safe to force push?

- When your GitHub admins have permitted it
- When master is protected
- When no one else has a copy of the history
- When no one else has made any changes

Note: When no one else has a copy of the history

--

## Which statements about merge are true?

- Merge commits have a parent commit
- Merge will make you unpopular
- Merge changes the history
- Merging two branches results in one fewer branches
- Merge always creates a new commit
- Merge is one of the Bouviers

Note: will make you unpopular (if used wrong)  
**and** Merge always creates a new commit
