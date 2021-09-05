## Setup Visual Studio code editor 
https://code.visualstudio.com/Download

- Explorer fix intent  = Code > Preferences > Settings > Workbench > appearance > Tree Indent > 14
- Extensions
  * GitLens
  * Git graph
  * Python
  * MagicPython
  * Python for Vscode
  * Python Extension Pack
  * Visual Studio Itellisense
  * Pylance
  * Json
  * Prettify json
  * Eslint for JS
- Cmd Shift P > Command Palette
- Autosave > files on window exit
- Settings pylance, add python path per project folder
- Setup python linter = flake8 in settings
- Settings Vertical ruler at 80 characters


If you are using the Pylance extension you can set your source folder via the python.analysis.extraPaths option. It also looks for common source folder names like src by default, this option is called python.analysis.autoSearchPaths.
Go to File > Preferences > Settings, search for pythonpath. Under the Pylance options you should see Extra Paths, this is where you set your source folder.
