# Image Color Recognition and Balancing
<em>Author: Adi</em><br/>

### Run in CLI:
<code>python Control.py</code>

Y -> Provide image (.jpeg, .jpg, .png) in root directory.

N -> Use NASA's Astronomy Picture of the Day (APOD) (requires NASA APOD API key in root dir under 'key.txt' to choose this option)

### Output directory tree:
```
output/
  DIR-ANOTHER_IMAGE.jpg/
    ...
  DIR-IMAGE.png/
    COL/  # Color channel toggling + invert + grayscale
      INV-IMAGE.png
      BNW-IMAGE.png
      RED-IMAGE.png
      YEL-IMAGE.png
      GRE-IMAGE.png
      CYA-IMAGE.PNG
      BLU-IMAGE.png
      PUR-IMAGE.png
    HLT/  # Color channel highlighting
      HLT_ALL-IMAGE.png
      HLT_RED-IMAGE.png
      HLT_YEL-IMAGE.png
      HLT_GRE-IMAGE.png
      HLT_CYA-IMAGE.png
      HLT_BLU-IMAGE.png
      HLT_PUR-IMAGE.png
    HUE/  # Hue sliding
      HUE_30-IMAGE.png
      HUE_60-IMAGE.png
      HUE_90-IMAGE.png
      HUE_120-IMAGE.png
      HUE_150-IMAGE.png
    BAL-IMAGE.png.txt  # Color variation report
    IMAGE.png  # Original image
  DIR-SUPER_COOL_PHOTO.jpeg/
    ...
```
