# kicad_rotary_encoder

## Description

This python module can be used for the creation of binary absolute rotary encoders of any specified resolution.

## Setup

Numpy is a dependency of this code and as such it is necessary to install numpy in the Python environment used by KiCad:

```
$ cd /Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/Current/bin
$ ./pip3 install numpy
```

On Mac OS go to the KiCad scripting directory and clone the repository there:

```
$ cd ~/Documents/KiCad/8.0/scripting/plugins
$ git clone git@github.com:JBuurmans/kicad_rotary_encoder.git
```

## Usage

In the KiCad pcb editor, open the KiPython shell and import `absolute_encoder` from the rotary_encoder module.

```
>>> from kicad_rotary_encoder import absolute_encoder as ae
```

Now use the `draw_encoder()` method of the module to create a rotary encoder that fits your needs.

### Examples

A 9 bit absolute encoder, with a central radius of 3mm and subsequent encoder rings of 2mm each.

```
ae.draw_encoder(r_inner=3, width=4, bits=9)
```

![plot](example1.png)

An inverted 9 bit absolute encoder with a central radius of 3mm, 4mm wide encoder rings and a *masking ratio* of 0.5.

:bangbang: Masking is the blocking of part of the encoder ring with a solid ring. This can prevent the bleeding of light from an encoder ring to the sensor of a neighbouring ring, thereby simplifying hardware design and potential needs for signal post processing.

```
ae.draw_encoder(r_inner=3, width=4, bits=9, mask=0.5)
```
![plot](example2.png)

An example of masking combined with inversion. This result limits the amount of copper that needs to be etched away.

```
ae.draw_encoder(r_inner=3, width=4, bits=9, mask=0.5, invert=True)
```

![plot](example3.png)