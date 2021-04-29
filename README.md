# VersionChanger
This python file (equipped with a `vu.json` configuration file) can edit the versions of multiple files (given that the version is written like `" * @version"`), this could be helpful when working with wordpress files.
## Usage:
Make sure that vu.json is configured like this:
- `"extentions"` is the extentions of the files where they need their versions updated.
- `"version"` is... well the version.
- `"ignore"` is the list of directories that it should ignore
- `"iterations"` is how deep should it go inside the directories (6 is recommended and is default)
- `"encoding"` is the type of encoding your files have ("utf-8" is default)
- `"logFile"` is the log file name (by default it's `"VULog.log"`).
