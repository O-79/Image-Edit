# Image Color Recognition, Balancing, Distortion, and more
<em>Author: Adi</em><br/>

<code>TODO:</code>

"DUL" -> for B, G, R of each pixel: avg(og,127) ... 1, 2, 3, 4 iterations ... save as DST(?)HUE(?)\_DUL\_\[0-4\]-IMAGE.---

### Requirements:
<code>pip install requests</code>

<code>pip install opencv-python</code>

<code>pip install numpy</code>

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
      COL_INV-IMAGE.png
      COL_BNW-IMAGE.png
      COL_RED-IMAGE.png
      COL_YEL-IMAGE.png
      COL_GRE-IMAGE.png
      COL_CYA-IMAGE.PNG
      COL_BLU-IMAGE.png
      COL_PUR-IMAGE.png
    DST/  # Distortions: pixellation, stretching (horizontal & vertical), randomization (4 outputs)
      DST_PXL-IMAGE.png
      DST_HOR-IMAGE.png
      DST_VER-IMAGE.png
      DST_MIX_0-IMAGE.png
      DST_MIX_1-IMAGE.png
      DST_MIX_2-IMAGE.png
      DST_MIX_3-IMAGE.png
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
