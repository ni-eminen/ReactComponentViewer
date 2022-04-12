# ReactComponentViewer

ReactComponentViewer's aim is to offer a quick and easy way to inspect React components without having to configure a React app.
## Contents

Be sure to checkout the backend code for this project at [RCV-backend](https://github.com/ni-eminen/RCV-backend)

### Documentation</br>

[uml](https://github.com/ni-eminen/ReactComponentViewer/blob/main/laskarit/viikko4/uml.jpeg)</br>

## Installation

1.  Navigate to ReactComponentViewer folder
2.  Install dependencies:

```bash
poetry install
```

3.  Run the program via Poetry

```bash
poetry run invoke start
```

	
### Running the program
In order for the program to work appropriately (for the time being), the user has to set up the backend server locally and have npm installed on their machine. A properly hosted backend will be introduced in the coming week.

Simply run:
```bash
poetry run invoke start
```
### Testing
```bash
poetry run invoke test
```
### Test coverage
Generate the test coverage via:
```bash
poetry run invoke coverage-report
```
A report will be generated to ReactComponentViewer root file.
