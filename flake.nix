{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (pkgs) fetchFromGitHub;
        inherit (pkgs.python3Packages)
          buildPythonPackage buildPythonApplication fetchPypi aiohttp discordpy;

        discord-py-slash-command = buildPythonPackage rec {
          pname = "discord-py-slash-command";
          version = "2.3.1";
          src = fetchPypi {
            inherit pname version;
            sha256 = "R2+lSV3WIZDg02F0Qbqn5ef6Mb/v73+I945CgWZsDUE=";
          };
          propagatedBuildInputs = [ aiohttp discordpy ];
        };

        typish = buildPythonPackage rec {
          pname = "typish";
          version = "1.9.2";
          src = fetchFromGitHub {
            owner = "ramonhagenaars";
            repo = "typish";
            rev = "v${version}";
            sha256 = "prgY43NS9QmBW8TcRUaW+rc7NdsNTWqWxgBSL39Wk30=";
          };
          doCheck = false;
        };

        jsons = buildPythonPackage rec {
          pname = "jsons";
          version = "1.5.0";
          src = fetchFromGitHub {
            owner = "ramonhagenaars";
            repo = "jsons";
            rev = "v${version}";
            sha256 = "V8iZPPiMEcjj0RzNILNFtSROjDVfiQDmh6G3d2XSOCY=";
          };
          propagatedBuildInputs = [ typish ];
          doCheck = false;
        };

      in rec {
        packages.quabbot = buildPythonApplication rec {
          name = "quabbot";
          src = ./.;
          propagatedBuildInputs = [ discord-py-slash-command discordpy jsons ];
        };
        defaultPackage = packages.quabbot;

        apps.quabbot = utils.lib.mkApp { drv = packages.quabbot; };
        defaultApp = apps.quabbot;

        checks = packages;
      });
}
