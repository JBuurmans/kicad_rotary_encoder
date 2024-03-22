# kicad_rotary_encoder

## Description

This python module can be used for the creation of binary or gray encoded absolute rotary encoders of various resolutions and to your own specified dimensions.
The result is a polygon object on the F.Cu copper layer which is not associated to any part or net in the circuit diagram. As a result you can include it within any project during the PCB layout phase of your project.


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

### Masking

The term masking in this module refers to the addition of a light obscuring *masking ring* in between consecutive encoder rings. This can prevent the bleeding of light from one encoder ring to the sensor of a neighbouring ring, thereby simplifying hardware design and potential needs for signal post processing or sequential reading of sensors.

### Binary vs Gray Code

Binary is the simplest form of a rotary encoder and it might be sufficient for your needs, particularly when resolution is low. However, most typically, gray encoding is used for rotary encoders.
The reason for doing so is that on the edge cases, precisely between two specific positions, sensors might be partially obscured and the true reading can be unpredictable. With binary encoding, a single positional step can result in the flipping of multiple, or even all bits at the same time, which means that at these transitions there exists a potential for a large error in the determined position.

Gray encoding solves this problem as for each and every single step in position, only a single bit will ever transition. As a result, the interpreted position will only ever deviate by a single step from the true position.

An additional upside to gray encoding is that it is easy to convert back and forth between gray encoding and binary, and no lookup table is required.



## Demo

To demo the code and see eight individual examples of rotary encoders directly in KiCad, import the demo script from the module in the KiPython shell:

```
>>> from kicad_rotary_encoder import demo
```

The demo creates two rows of examples, the top examples are binary encoded and the bottom row shows their counterparts using gray encoding.

![plot](demo.png)