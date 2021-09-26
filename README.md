# Elevation2Plot

Generate elevation plots using open-elevation API and Google Earth.

> Open-Elevation is a free and open-source alternative to the Google Elevation API and similar offerings. <br> Open-Elevation API - https://api.open-elevation.com <br> More info: https://open-elevation.com <br> GitHub: https://github.com/Jorl17/open-elevation

## Requirements

---

- Python 3.3+
- Google Earth Pro
- Windows, Linux or macOS

## Usage

---

- Add the path using Google Earth
- Right Click on path > Save place as...
- Save the '.kmz' file
- Simply run the **Elevation2Plot.py** file, passing in the the *kmz* file which you have exported from **Google Earth** previously

```
Elevation2Plot.py <filename.kmz>
```
## Examples
----
### Elevation plot from **Google Earth**:

![GoogleEarthImage](src\GoogleEarthImage.png)

### Generated plot:

![GoogleEarthImage](src\ElevationPlot.png)

## License
----
**GNU General Public License v3.0**

This program is free software: you can redistribute it and/or modify it under the terms of the **GNU GPLv3**

Google Earth, Google Earth Pro are Copyright © by  **Google**

## Disclaimer
----
Open-Elevation API is a free and open-source alternative to Google Elevation API. The elevation plots generated from this script might be inacurate in some conditions.