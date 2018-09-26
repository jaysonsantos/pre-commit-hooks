# pre-commit-hooks
My pre-commit hooks

# How to use
Configure our repository in your `.pre-commit-config.yaml` file like this:

```yaml
- repo: https://github.com/jaysonsantos/pre-commit-hooks
  rev: cf7f062c6ba5ca1b83f90c341f77f3d9f48d19db
  hooks:
  -   id: poetry-lock-file
  -   id: pipenv-lock-file
```
