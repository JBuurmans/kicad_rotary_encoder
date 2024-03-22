from rotary_encoder.rotary_encoder import util


def encoder(r_inner:float, width:float, bits:int, mask:float = 0, gray:bool=True, origin_x:float = 0, origin_y:float = 0, invert=False) -> None:
    """
    Draw an absolute rotary encoder pattern

    :param r_inner: the inner radius of the encoder in mm
    :param widths: the width of encoder rings
    :param bits: the resolution of the encoder (number of rings) in number of bits
    :param mask: A masked out region in between each ring to reduce bleeding from channel to channel,
    defined as a ratio (0...1) of the provided width
    :param gray: Should the encoder be gray encoded (True,default) or binary(False)
    :param origin_x: The x coordinate in mm of the origin of the encoder
    :param origin_x: The y coordinate in mm of the origin of the encoder
    :param invert: Creates the inverted image of the encoder in a square area which saves a lot of copper etching
    """
    mask_width = width * mask
    window_width = width - mask_width
    offset = mask_width / 2

    angle = 360/(2**bits)
    chains = []

    # Draw masking rings
    if mask > 0 and not invert:
        chains += util.get_concentric_rings(r_inner, width, mask_width, bits+1, origin_x, origin_y)

    # Draw encoder
    for i in range(2**bits):
        phase = i * angle
        if gray:
            i = util.to_gray(i, bits)

        # Draw value encoded sections from msb(inner) to lsb(outer)
        for bit in range(bits):
            # Draw a blocking section bit is high, leave open if zero
            if i & (1 << (bits-bit-1)):
                ri = r_inner + (width*bit) + offset
                chains += [util.get_arch(ri, window_width, angle, phase, origin_x, origin_y)]

    util.draw_polyshape(chains, invert)
