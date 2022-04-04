### UML
```mermaid
graph TD
   main --> B{new Machine}
   B --> H(Machine.drive)
   H --> A{engine.is_running}
   A -->|false| U{end}
   A -->|true| I{engine.use_energy}
   I --> G{fueltank.consume}
 ```