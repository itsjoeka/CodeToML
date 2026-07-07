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

## Undo anything
Claude checkpoints files before every edit.
- Press Esc Esc (double tap) to open `/rewind` and roll back to any prior state - be it code, conversation, or both
- `/clear` wipes conversation but keeps files
- `/branch` forks the conversation to try two approaches

## Run in the background
- Add \& to any bash command and it runs in the background, while you keep chatting, Claude will notifiy you when the task is finished
- Run `/tasks` to see everything in flight

## Teach Claude your rules
- Drop a `CLAUDE.md` file in your repo and claude reads it at the start of every session. Conventions like: test commands, style rules, do-not-touch directories can be put in there
- Run `/init` to generate a starter CLAUDE.md from your codebase.
- Run `/memory` to eidit it inline

## Extend tools
MCP or Model Context Protocols give claude new tools: read our slack, query your database, control your browser/
- Run `/mcp` to browser and connect servers. You can connect github or slack or mattermost servers

Once connected, tools appear automatically, ask Claude to "check my calendar" or "search our notion" and it just works
- In the shell: `claude mcp add my-server -- npx some-mcp-pkg` to wire one up without living the terminal

## Automate your workflow
- Save a prompt to `.claude/skills/deploy/SKILL.md` and it becomes `/deploy`. Type it and claude runs it.
- Run `/skill` to see what you have
- Run `/install-github-app` to let Claude review PRs when tagged.
