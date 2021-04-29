# VersionChanger
This python file (equipped with a `vu.json` configuration file) can edit the versions of multiple files (given that the version is written like `" * @version"`).
## Usage:
Make sure that vu.json is configured like this:
- `"extentions"` is the extentions of the files where they need their versions updated (e.g. `*.php` is all PHP files, `style.css` only takes the files named `style.css`).
- `"version"` is... well the version. (e.g. `"1.1.2"` will make the version say `" * @version 1.1.2"`)
- `"ignore"` is the list of directories that it should ignore (no `/` or `\` needed).
- `"iterations"` is how deep should it go inside the directories (`6` is recommended and is default)
- `"encoding"` is the type of encoding your files have (`"utf-8"` is default)
- `"logFile"` is the log file name (by default it's `"VULog.log"`).
