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
