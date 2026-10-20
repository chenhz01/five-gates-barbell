# Contributing

The method improves when someone brings a case where it gave the wrong answer.

## Sign off your commits

Use `git commit -s`. By signing off you certify you have the right to submit the
contribution, and you agree it is licensed under the same terms as the file you
changed (Apache-2.0 for code, CC BY 4.0 for docs).

## The most useful contributions

- **A case where a gate produced a false positive or false negative**, with the
  evidence you used. Cases are worth more than opinions.
- **A domain adaptation**: how you operationalised "behavioural evidence" in a
  market where payments are indirect.
- **A counter-example to a rule.** If "never all-in" was wrong for you, say why
  and what happened.

## What gets rejected

- Rewording the gates so that a borderline project passes.
- Adding a weighting scheme that lets red gates average out. That is the one
  thing this method exists to prevent.
- Anything containing confidential company data.

## Changing the gates themselves

Open an issue first. Changing a gate changes what FGM-1.0 means; that requires a
version bump and a written reason, not a silent edit.
