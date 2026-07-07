# **CLAUDE PRO**
----

## Talking to your codebase
- Type @ anywhere in your prompt to fuzzy-find and attach a file. Claude reads it before answering. e.g `> what does @src/auth.ts do?` or a specific line `> @src/auth.ts:42`
- Also try `@folder/` to attach a whole directory tree

## Steering with modes
- Pressing _shift+tab_ cycles through permission modes. Each mode changes how claude asks before acting `auto mode`, `default`, `plan` and `accept edits` modes
  - `default`: ask before every edit
  - `auto`: claude decides what is safe. Use this mode for long unattended tasks.
  - `plan`: reearch and propose, never touch files. Use this mode for big refactors you want to review first. 
  - `accept edits`: edit freely, ask for commands
 Run `/permissions` to pre-allow specific commands so Claude stops asking about them
