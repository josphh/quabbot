# Quabbot
The Discord Companion and RPG Bot

## Launch

Install the Nix package manager by running this command:
```sh
curl -L https://github.com/numtide/nix-flakes-installer/releases/download/nix-2.4pre20210604_8e6ee1b/install | sh
```
Add this to `~/.config/nix/nix.conf`, creating the file if it doesn't exist:
```ini
experimental-features = nix-command flakes
```

Then you can use this command to run Quabbot:
```sh
QUABBOT_TOKEN="xxxxx" nix run
```
