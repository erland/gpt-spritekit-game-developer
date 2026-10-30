# Release verification after GPT Byggaren 1.6.33 migration

The first new release after the migration must be published from the merged source on `main`, not from the old 1.5.0 build.

## Automated release checks
`.github/workflows/release.yml` verifies:
- Release tag follows `vMAJOR.MINOR.PATCH`.
- All five runtime ZIPs and the project ZIP are present.
- `SHA256SUMS.txt` matches the generated archives.
- `DELIVERY-MANIFEST.json` lists the required archives and release version.
- All generated ZIP files, checksums and delivery manifest are attached to the GitHub Release.

The builder may also output an additional Engine ZIP, which is retained and published. The required six archives are the project, Chat, Plugin, Claude Projects, Claude Skills and OpenCode.

## Manual acceptance
1. Merge this PR once its CI checks pass.
2. Publish a new GitHub Release using a new SemVer tag (for example `v1.2.0`) pointing to the intended `main` commit.
3. Confirm the `Release GPT distributions` workflow succeeds.
4. Confirm each required ZIP is downloadable and the published SHA256SUMS verifies the downloads.
5. Perform separate host checks as applicable (OpenAI Plugin install/activation, Claude Skills, OpenCode, and tvOS/macOS Xcode tests). CI archive validation does not prove host runtime parity.

The older `v1.1.0` release predates GPT Byggaren 1.6.33 migration and must not be treated as evidence of the new release workflow.
