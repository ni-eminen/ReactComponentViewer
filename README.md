# ReactComponentViewer

ReactComponentViewer's aim is to offer a quick and easy way to inspect React components without having to configure a React app.
## Contents

Be sure to checkout the backend code for this project at [RCV-backend](https://github.com/ni-eminen/RCV-backend)

### Documentation</br>

[uml](https://github.com/ni-eminen/ReactComponentViewer/blob/main/laskarit/viikko4/uml.jpeg)</br>
[requirement spec](https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/vaatimusmaarittely.md)</br>
[timetable](https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/timetable.md)</br>
[changelog]( https://github.com/ni-eminen/ReactComponentViewer/blob/main/documentation/changelog.md)</br>

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
