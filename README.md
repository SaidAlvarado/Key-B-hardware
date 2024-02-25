# KeyB-keyboard
ZMK based wireless half keyboard


Remember to attribute: https://github.com/daprice/keyswitches.pretty/tree/master

Attribute the Fanstel module footprint and symbols to: https://github.com/hemalchevli/Fanstel-kicad-library


## Battery
- [Big Option](https://www.amazon.fr/EEMB-Batterie-polym%C3%A8re-Rechargeable-connecteur/dp/B09DPPP8ZV/)
  - JST Connector (PH). [Digikey Link](https://www.amazon.fr/EEMB-Batterie-polym%C3%A8re-Rechargeable-connecteur/dp/B09DPPP8ZV/?th=1)
- [Slightly smaller option](https://www.amazon.fr/EEMB-Batterie-Rechargeable-Navigation-Enregistreur/dp/B08FD3V6TF)
- Charging current
  - std 0.2C, max. 1C. (60mA to 300mA)


## BOM

- Premade digikey cart: https://www.digikey.fr/short/4dtv58d8


## References

#### Crystal oscillator design
- [General nRF crystal design guidelines](https://devzone.nordicsemi.com/guides/hardware-design-test-and-measuring/b/nrf5x/posts/general-pcb-design-guidelines-for-nrf52)
- [nRF52840 reference circuit](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fps_nrf52840%2Fref_circuitry.html)
  - They recommend a 9pF crystal for the 32.768kHz crystal
- [Nordic White paper on Crystal oscillator design](https://infocenter.nordicsemi.com/pdf/nwp_015.pdf?cp=12_12) Note, there is a correction of this white paper on the first link in this section.
