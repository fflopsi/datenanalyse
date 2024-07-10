let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  venvDir = "venv";
  packages = [ # buildInputs?
    pkgs.python3.pkgs.venvShellHook
    pkgs.python3
    (pkgs.python3.withPackages (python-pkgs: [
      #python-pkgs.pip
      python-pkgs.jupyter
      python-pkgs.numpy
      python-pkgs.scipy
      python-pkgs.pandas
      python-pkgs.matplotlib
      python-pkgs.scikit-learn
      python-pkgs.scikit-image
    ]))
  ];
}
