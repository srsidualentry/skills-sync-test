# Troubleshooting

## An installed skill does not appear

- Run `npx skills add srsidualentry/skills-sync-test --list` to confirm the skill exists.
- Reinstall with `--skill <name>` and check which agent it was installed for.
- Restart the agent so it reloads its skills.

## The agent cannot reach DualEntry

Skills do not connect to DualEntry by themselves. Check your connection as described in
[Authentication](authentication.md).

## A tool returns a permission error

Details to be confirmed. Check that the signed-in user has access to the records the skill reads.

## Results appear incomplete

- Check the skill's defaults, such as the date range or scope, and say so in your request if you
  want something different.
- Large result sets may be paged. Ask the agent to continue until it has read every page.
