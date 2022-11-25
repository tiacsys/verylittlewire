# Contributing

Contributions are welcome, and they are greatly appreciated! Every little helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs to [our issue page][gh-issues]. If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Little Wire Python library could always use more documentation, whether as part of the official Little Wire Python library docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback [our issue page][gh-issues] on GitHub. If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome 😊

## Get Started!

Ready to contribute? Here's how to set yourself up for local development.

1. Fork the repo on GitHub.

2. Clone your fork locally:

   ```shell
   $ git clone git@github.com:your_name_here/verylittlewire.git
   ```

3. Create and activate a project specific [Python 3 virtual environment](https://docs.python.org/3/library/venv.html):

   ```shell
   $ python3 -m venv --prompt="$(basename $(pwd))[$(python3 --version)]" \
                     --clear --copies .venv
   $ source .venv/bin/activate

   $ pip3 install --upgrade pip setuptools
   $ pip3 install --upgrade poetry
   ```

4. Install the project dependencies with [Poetry](https://python-poetry.org):

   ```shell
   $ poetry install --all-extras
   ```

5. Create a branch for local development:

   ```shell
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

6. When you're done making changes, check that your changes pass our tests:

   ```shell
   $ poetry run pytest
   ```

7. Linting is done through [pre-commit](https://pre-commit.com). Provided you have the tool installed globally, you can run them all as one-off:

   ```shell
   $ pre-commit run -a
   ```

   Or better, install the hooks once and have them run automatically each time you commit:

   ```shell
   $ pre-commit install
   ```

8. Optional run tests on documentation and build them offline:

   ```shell
   $ make -C docs spelling
   $ make -C docs doctest
   $ make -C docs coverage ; cat docs/build/coverage/python.txt
   $ make -C docs linkcheck
   $ make -C docs html
   ```

9. Commit your changes and push your branch to GitHub:

   ```shell
   $ git add .
   $ git commit -m "feat(something): your detailed description of your changes"
   $ git push origin name-of-your-bugfix-or-feature
   ```

   Note: the commit message should follow [the conventional commits](https://www.conventionalcommits.org). We run [`commitlint` on CI](https://github.com/wagoid/commitlint-github-action) to validate it, and if you have installed pre-commit hooks at the previous step, the message will be checked at commit time.

10. Submit a pull request through the GitHub website or using the GitHub CLI (if you have it installed):

    ```shell
    $ gh pr create --fill
    ```

## Pull Request Guidelines

We like to have the pull request open as soon as possible, that's a great place to discuss any piece of work, even unfinished. You can use draft pull request if it's still a work in progress. Here are a few guidelines to follow:

1. Include tests for feature or bug fixes.
2. Update the documentation for significant features.
3. Ensure tests are passing on CI.

## Tips

To run a subset of tests:

```shell
$ pytest tests
```

## Making a new release

The deployment should be automated and can be triggered from the Semantic Release workflow in GitHub. The next version will be based on [the commit logs](https://python-semantic-release.readthedocs.io/en/latest/commit-log-parsing.html#commit-log-parsing). This is done by [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html) via a GitHub action.

[gh-issues]: https://github.com/tiacsys/verylittlewire/issues
