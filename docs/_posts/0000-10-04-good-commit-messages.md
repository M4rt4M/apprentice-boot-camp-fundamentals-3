## Good commit messages

+ Commit messages are important
+ They let you time travel—you are sending a message into the future
+ You might be sending it to yourself
+ Make sure it is useful

--

Borrowing content from [Use templates for better Git commit messages](https://engineering.autotrader.co.uk/2018/06/11/use-templates-for-better-commit-messages.html) on the Auto Trader Engineering Blog

--

<img src=https://imgs.xkcd.com/comics/git_commit.png>

“[Git Commit](https://xkcd.com/1296/)” by [XKCD](https://xkcd.com/) licensed under [Creative Commons Attribution-NonCommercial 2.5 License](https://creativecommons.org/licenses/by-nc/2.5/)

--

## Good message tips

+ Separate subject from body with a blank line
+ Limit the subject line to 50 characters
+ Capitalize the first letter of the subject line
+ Do not end the subject line with a period
+ Use the imperative mood in the subject line
+ Wrap the body at 72 characters
+ Use the body to explain what and why vs. how

--

## e.g.

```
9999 Add/Change/Refactor feature up to 50 char >|

https://tracker.example.com/issues/9999

Why this feature or fix was necessary/desirable. Be sure to hard-wrap
at 72 characters!

Optional notes on why the feature or behaviour was implemented in the
way it was, and side-effects or other consequences.

Co-authored-by: Person Name <person.name@example.com>
```

--

> the important part [of a pull request] is the message. I want to understand what I’m pulling, and why I should pull it. I also want to use that message as the message for the merge, so it should not just make sense to me, but make sense as a historical record too.  
> — [Linus Torvalds in the Linux Kernel Maintainer Handbook](https://www.kernel.org/doc/html/latest/maintainer/pull-requests.html)
