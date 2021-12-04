## This Bot is now Depreciated
Quabbot uses the API wrapper [Rapptz/discord.py](https://github.com/Rapptz/discord.py) in order to run on Discord servers. This library is now [outdated](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1), and I will no longer continue this bots development, and I shall cease using Discord as a whole. Instead, I will move to [Matrix](https://matrix.org/), and begin bot development there.

# Quabbot
The Discord Companion and RPG Bot

## Launch

The [Nix package manager](https://nixos.org/)
can be installed on most Linux distributions.

### Nix Unstable

Add this to `/etc/nix/nix.conf` or `~/.config/nix/nix.conf`,
creating the file if it doesn't exist:

```ini
experimental-features = nix-command flakes
```

Then, this command will start Quabbot:

```sh
QUABBOT_TOKEN="xxxxx" nix run
```

### Nix Stable

Run the following commands:

```sh
nix build
QUABBOT_TOKEN="xxxxx" ./result/bin/quabbot
```
