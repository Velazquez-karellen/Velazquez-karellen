# ORBIT profile review

All development is on feature/orbit-profile-v1. Do not merge until reviewed.

## Review
- Open the branch README on desktop and mobile.
- Confirm project URLs and public visibility before linking research or organization repositories.
- Confirm the portfolio and resume links before adding them to navigation.
- The vector banner is a fallback. To use a cinematic PNG, upload it to assets/hero/orbit-banner.png on the feature branch and replace the hero SVG reference in README.md.
- Use original project images only with permission.

## Activity
The workflow runs on changes to its own file or the generator on the feature branch. Check the Actions tab for Update ORBIT activity. The scheduled run only works on the default branch after approval and merge. The default GITHUB_TOKEN may have limited visibility; do not publish private research details or use a personal token without reviewing its scope. The initial SVG explicitly indicates pending data. External cards remain as a fallback until the native chart is verified.

## Before merge
Check SVG rendering, navigation links, activity generation and mobile readability. Review the branch comparison and merge only when satisfied.
