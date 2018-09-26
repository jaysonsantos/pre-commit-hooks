# pre-commit-hooks
My pre-commit hooks

# How to use
Configure our repository in your `.pre-commit-config.yaml` file like this:

```yaml
- repo: https://github.com/jaysonsantos/pre-commit-hooks
  rev: master
  hooks:
  -   id: poetry-lock-file
  -   id: pipenv-lock-file
```
