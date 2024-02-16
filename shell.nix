{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	packages = with pkgs; [
		git
		python311
		python311Packages.pip
		pkgs.pdm
	];
}
