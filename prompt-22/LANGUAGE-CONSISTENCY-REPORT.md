# Language consistency update

Version: `1.0.0-rc9`

## Rule

- Chat replies follow the user's language.
- Code, identifiers, code comments, tests and technical project documentation are English.
- User-facing game text may use any language explicitly requested by the user.
- Localized game strings should be separated from technical code through localization resources where practical.

## Updated areas

- Final GPT instruction
- GPT role and principles
- SpriteKit architecture guidance
- Zip workflow guidance
- Regression test pack and machine-readable test cases

## Compatibility

Existing mixed-language projects are not mass-renamed automatically. New and substantially rewritten technical material follows English, while a larger migration is proposed and scoped separately.
