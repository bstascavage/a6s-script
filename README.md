## Savage Teleprompter

### Description

**Savage Teleprompter** is a Python script to generate a _callout script_ for Final Fantasy 14 raids. A _callout script_ is like a teleprompter, printing out instructions for a given raid. The teleprompter can wait for input, wait for a certain amount of time, and hightlight user input for later prompts. This allows for dynamic raid scripts that adapt for any pull.

### Prerequisites

- VSCode
- Docker
- [Dev Container plugin](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VSCode (For more details, see [here](https://code.visualstudio.com/docs/devcontainers/containers))

### How to use

1. Launch the [devcontainer in VScode](https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-an-existing-folder-in-a-container) by clicking the bottom-right of your VSCode instance, then selecting **Reopen in Container**.
1. Add your raid script YAML to the `resources/` directory (see here for more info on how to define a script), ie `resources/foo.yaml`.
1. Run your teleprompter via `task run raid=foo`, where `foo` is the name of your YAML file.

### Development

### Python

**Savage Teleprompter** uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage both its dependencies and virtual environments. New dependencies can be installed via `pipenv install <package>`, with their specific version being saved to the `Pipfile.lock` file; this is the preferred way to install new packages, as opposed to manually editting `Pipfile`.

Commands can be run inside of the Python virtual environment via `pipenv run <command>`

### Taskfile commands

**Savage Teleprompter** uses [Taskfile](https://taskfile.dev/) to wrap common development commands. The commands are:

| Command    | Description                                               | Options                            |
| ---------- | --------------------------------------------------------- | ---------------------------------- |
| `init`     | Initializes pre-commit and the Python virtual environemnt | `dev=true` to install dev packages |
| `clean`    | Remove the virtual environment                            |                                    |
| `validate` | Runs the pre-commit checks                                |                                    |
| `run`      | Runs the teleprompter                                     | `raid=<name_of_raid>`              |

### Raid script definition

A raid script is a YAML file stored in the `resources/` directory; the name of the actual YAML file will be the raid name passed into `task run raid=<name_of_raid>` (ie to run the teleprompter for a6s, create `resources/a6s.yaml` and run `task run raid=a6s`). Each element in the YAML file corresponds to a line on the teleprompter. A line can have the following properties

| Property   | Description                                                                                                                         | Required              | Default |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| `text`     | The actual text being displayed                                                                                                     | Yes                   |         |
| `input`    | Line waits for user input                                                                                                           | No                    | `false` |
| `variable` | Sets the user input to this variable name. This variable can be referenced in future `text` fields, ie: `"Please print {some_var}"` | Yes if `input` is set |         |
| `bold`     | Whether to bold the line                                                                                                            | No                    | `false` |
| `newline`  | Whether to print a newline after the line                                                                                           | No                    | `false` |
| `color`    | What color to set the line. See [here](https://pypi.org/project/termcolor/) for the full list                                       | No                    | `white` |
| `sleep`    | Wait a certain amount of seconds before continuing to the next line                                                                 | No                    | 0       |
