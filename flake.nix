{
    description = "Pyfetch a fastfetch alternative";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
        flake-utils.url = "github:numtide/flake-utils";
    };


    outputs = { self, nixpkgs, flake-utils }:
        flake-utils.simpleFlake {
            inherit self nixpkgs;

            packages = { pkgs }: {
                default = pkgs.python3Packages.buildPythonApplication {
                    pname = "pyfetch";
                    version = "1.0";
                    
                    src = ./.;


                    entryPoints = {
                        pyfetch = "main:main";
                    };
                    
                };
            };
        };
}