This project uses `node` version 10, and `nvm` (node version manager) to manage the version of `node`.

1. Make sure `nvm` is installed by running `nvm --version || brew install nvm`
2. Make sure you have the correct version of `node` by running `nvm install`.
3. Make sure you have all the required packages by running `npm install` (note the subtle difference between `nvm` in the previous step and `npm` here).

Now you can run the tests (against the right version of node) using `nvm exec npm test`.

If you would like the tests to run in watch mode, run `nvm exec npm run test:watch`. By default, this runs the tests for any files that have changed, however you can choose to only run a particular file by pressing `p` and then entering a pattern to match a file. For example, to only run the tests for the checkout task, you could press `p` then enter `checkout`. To cancel watch mode, press `q` to quit.

Note: brew is not an officially supported installation method. If you have problems <sup>(e.g. [can’t `nvm exec`](https://github.com/nvm-sh/nvm/issues/856))</sup>, `brew uninstall nvm` follow [the official installation instructions](https://github.com/nvm-sh/nvm/blob/master/README.md#installing-and-updating)

If you have any problems, let one of the people running the boot camp know and we will happily help! :)
