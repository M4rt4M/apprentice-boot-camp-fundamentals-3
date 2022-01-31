## Setting up

If you don’t already have it, install Visual Studio Community. As part of the install, select `.NET desktop` as one of the install modules. If you’re limited for bandwidth then speak to one of us about what you can trim from the install. You only need .NET core packages and maybe the JIT debugger.

If you've already installed Visual Studio then make sure that `.NET desktop` is added through this menu:
`Tools --> Get tools and features --> .NET Desktop`

## Running the tests

From your terminal, change directory into `exercises\dotnet`. Run `code .` and Visual Studio Code should start opening the .NET code. If prompted, choose to download dependencies.

Validate that you are set up correctly by running the tests. Open one of the tests and you should see the option to `Run All Tests`. These should run okay, with all the tests being skipped (not failing). You should see output similar to this:

```text
Total tests: 14. Passed: 0. Failed: 0. Skipped: 14
```

If you have any problems, let one of the people running the boot camp know and we will happily help! :) 