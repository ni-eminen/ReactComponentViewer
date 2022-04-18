# UML
![UML](https://github.com/ni-eminen/ReactComponentViewer/blob/main/laskarit/viikko4/uml.jpeg)

```mermaid
sequenceDiagram
    Client->>+Backend: Component 
    Backend->>+Npx: Build Component
    Npx->>-Backend: React app
    Backend->>+Npx: gulp React app
    Npx->>-Backend: react_app.html
    Backend->>-Client: react_app.html
    Client->>+Webbrowser: react_app.html
```