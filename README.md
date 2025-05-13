# Lunar Month (පොහොය මාස නාමකරණය) සහ Nakshatra (නක්ෂත්‍ර) 3D Orbital Simulation

This was originally created for my youtube video about the Nakshatra and Zodiac system in Sinhala. The project simulates the 27 Nakshatras and 12 Zodiac signs in a 3D environment using Three.js. This is to showcase the Naming of the lunar months and its relation to the Nakshatras (27 constellations) and Zodiac signs (12 constellations) in Sinhala. Feel free to use this for educational purposes or as a reference for your own projects.

---

## Features

* **27 Nakshatra Rings**: Alternating-opacity arcs for each Nakshatra, with labeled names and lunar month markers.
* **12 Zodiac Rings**: Alternating-opacity arcs for each zodiac sign, with labels and divider lines.
* **Earth, Sun & Moon**: Textured spheres for Earth, Sun, and Moon, placed in 3D space.
* **Orbits**: Circular orbit paths for Sun and Moon with adjustable radii.
* **Animation Controls**:

  * Play/Pause
  * Forward/Reverse direction
  * Speed presets (hour/day/week/month/year)
  * Reset to default speed
* **Manual Positioning**: Range sliders for Sun and Moon positions (0°–360°), with real-time display in D° M' S" and Sinhala rashi notation.
* **Moon Phase Panel**: Live Moon phase image and name based on current Sun–Moon elongation.
* **Zooming**: Mouse-wheel zoom on the canvas.
* **Responsive**: Canvas and camera adjust on window resize.

---

## Prerequisites

* Modern web browser with WebGL support (Chrome, Firefox, Safari, Edge).
* Internet access for Three.js CDN (or host locally).

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/27-nakshatra-zodiac-3d.git
   cd 27-nakshatra-zodiac-3d
   ```

2. **Serve files**
   You can open `index.html` directly in the browser, or run a simple HTTP server:

   ```bash
   # Python 3
   python -m http.server 8000

   # Node.js
   npx http-server . -p 8000
   ```

3. **Open**
   Navigate to `http://localhost:8000/index.html` in your browser.

---

## File Structure

```
/ (project root)
├── index.html        # Main HTML + CSS + JS file
├── README.md         # This documentation
├── /images           # Asset folder
│   ├── sun.png       # Sun texture
│   └── /moon_phases  # Moon phase images (phase_00.png ... phase_29.png)

```

---

## Configuration

> No configuration files are needed. All settings are in the `index.html` file.

For customization, you can adjust the following:
* **Moon Phase Images**: By default, `moonPhaseImageBasePath` is set to `/images/moon_phases/`. Ensure your 30 images are named `phase_00.png` through `phase_29.png`. Adjust the base path in the script if needed.
* **Sun Texture**: Path to Sun image is `/images/sun.png`. Change if storing elsewhere.
* **Nakshatra & Zodiac Labels**: Arrays `nakshatras`, `lunarMonthNames`, and `zodiacSigns` are defined in the script. Edit names or add translations as desired.

---

## Usage

* **Play/Pause**: Click ■/▶ to start or stop the orbital animation.
* **Direction**: Toggle Forward/Reverse to change the motion direction.
* **Speed**: Use +/– or Reset to adjust simulation speed.
* **Manual Adjust**: Drag the Sun or Moon slider to position them manually. Animation will pause automatically.
* **Zoom**: Scroll up/down over the 3D canvas.
* **Moon Phase**: Watch the top-right panel update with the current Moon phase.

---

## Customization

* **Camera Angle**: Modify `initialCameraY`, `minCameraY`, and `maxCameraY` in the script.
* **Materials & Colors**: Change arc materials’ colors and opacities in the `Materials` section.
* **Opacity & Ring Radii**: Tweak `nakshatraInner`, `nakshatraOuter`, `zodiacInner`, `zodiacOuter`, etc., for different ring sizes.
* **Debug Logging**: Set `const debug = true | false` in the script to control console logs.

---

## License

MIT License © Dasun Sameera Weerasinghe


---