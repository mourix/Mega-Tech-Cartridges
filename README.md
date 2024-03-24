# Mega-Tech-Cartridges
DIY Sega Mega-Tech game cart designs based on a full reverse engineering of the original 171-5782/171-5783 cartridges.
## 171-5782 - Mega Drive
Original cart for MD based games with a single 4 Megabit ROM.
### 171-5782 Repro
* 1:1 reverse engineered copy to the original.
* No jumper settings needed for use.
* Only supports 40-pin ROMs.
### 171-5782 Redux
* Removed unused jumpers / capacitors.
* Add 8-32Meg 42-pin EPROM support.
* Add 1mm edge connector length for shells with low tolerances.
* Add JLCPCB silkscreen for "Remove Order Number - Specify a location"
## 171-5783 - Master System
Original cart for SMS based games with a single 1 or 2 Megabit ROM.
### 171-5783 Repro
* 1:1 reverse engineered copy to the original.
* Needs JP1 bridged for 1 Megabit ROMs.
* Needs GND knot on IC1 drilled out as is done on original carts.
### 171-5783 Redux
* Removed unused jumpers / capacitors.
* Removed GND knot.
* Add 1mm edge connector length for shells with low tolerances.
* Add JLCPCB silkscreen for "Remove Order Number - Specify a location"
## Manufacturing Notes
The gerber zip files in each project folder can be uploaded directly to most suppliers.
### JLCPCB
* PCB specifications: standard 2 layer PCB, 1.6mm thickness. Select "Gold Fingers" and "30°finger chamfered".
* Redux PCBs: select "Remove Order Number - Specify a location".
