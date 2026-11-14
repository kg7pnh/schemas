# schemas

JSON Schemas (draft-07) for RPG dice rolls.

| Schema | Describes |
|---|---|
| [`json/dieroll.schema.json`](json/dieroll.schema.json) | A die roll: die size, number of dice and optional modifiers, for example `3D6+1` |
| [`json/dierollmodifier.schema.json`](json/dierollmodifier.schema.json) | A modifier applied to a roll: `+`, `-`, `x`, `X` or `/` and a value |

## Tests

Example documents live in `tests/<schema>/valid/` and `tests/<schema>/invalid/`.
To run them locally:

```bash
pip install jsonschema
python tests/validate.py
```

The `validate` workflow runs the same check on every pull request.

## Releases

Releases are automated with [release-please](https://github.com/googleapis/release-please).
Write commit messages in the [Conventional Commits](https://www.conventionalcommits.org/) format:

- `fix: ...` makes a patch release
- `feat: ...` makes a minor release
- `feat!: ...` or a `BREAKING CHANGE:` footer makes a major release

After each push to `main`, release-please opens or updates a release PR.
Merging that PR updates `CHANGELOG.md`, tags the version (for example `v1.0.0`) and publishes a GitHub release.
