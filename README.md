# VersionChanger
This python file (equipped with a `vu.json` configuration file) can edit the versions of multiple files (given that the version is written like `" * @version"`).
## Usage:
Make sure that vu.json is configured like this:
- `"extentions"` is the extentions of the files where they need their versions updated (e.g. `*.php` is all PHP files, `style.css` only takes the files named `style.css`).
- `"version"` is... well the version. (e.g. `"1.1.2"` will make the version say `" * @version 1.1.2"` leave empty for no changes)
- `"author"` is... well the author. (e.g. `"CodyNinja1"` will make the version say `" * @author CodyNinja1"` leave empty for no changes)
- `"package"` is... well the package. (e.g. `"cool-package"` will make the version say `" * @package cool-package"` leave empty for no changes)
- `"ignore"` is the list of directories that it should ignore (no `/` or `\` needed, except when indenting files like this `"folder\to\ignore"`, this will ignore the folder `"ignore"` but won't ignore `"folder"` or `"to"`).
- `"iterations"` is how deep should it go inside the directories (`6` is recommended and is default)
- `"encoding"` is the type of encoding your files have (`"utf-8"` is default)
- `"logFile"` is the log file name (by default it's `"VULog.log"`).
