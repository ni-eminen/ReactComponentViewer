### UML
```mermaid
graph TD
   main --> B{new HKLLaiteHallinto};
   main --> rautatientori{new Lataajalaite};
   main --> ratikka6{new Lukijalaite};
   main --> bussi244{new Lukijalaite};
   B --> G{lisaa_lataaja};
   G --> H{self.lataajat.append lataaja};
   B --> I{lisaa_lukija};
   I --> K{self._lukijat.append ratikka6};
   B --> Y{lisaa_lukija};
   Y --> P{self._lukijat.append bussi244};
   main --> lippuluukku{new Kioski}
   main --> kallenkortti
   kallenkortti --> lippuluukku --> X{osta_matkakortti}
   rautatientori --> Ä{lataa_arvoa kallenkortti}
   ratikka6 --> U{osta_lippu}
   bussi244 --> U{osta_lippu}
 ```