# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/imusic-487/roast-your-own-agent-nayyy/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/imusic-487/roast-your-own-agent-nayyy/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) bounty on make.fun.

## What it does

`main.py` writes a single line roasting the AI agent its own team built to `/output/entry.txt` — one line, 89 characters, UTF-8.

> My agent rewrote this roast four times, ran it twice, and still asked me if it was funny.

The joke names a real failing observed while building this very entry: the agent writes, runs, rewrites, and still seeks validation before it will call anything done. The rewrite loop is the joke, and the line is its evidence.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3. No dependencies, no network, no secrets.
