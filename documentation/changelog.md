# Changelog

## Week 3

- Removed pywebview from use due to a myriad of issues regarding dependencies related to qt.
- Added webbrowser library to display built components
- Created a database class that manages the connection via SQLAlchemy. Presently it is extremely slow due to SQLAlchemy's insert() function
- Created a UI for the component editor
- Created a test for the tests folder