from rotary_encoder.rotary_encoder import util


def draw_encoder(r_inner:float=3, widths:float=2, bits:int=4, mask:float=0, origin_x:float=0, origin_y:float=0, invert=False) -> None:
    """
    Draw an absolute rotary encoder pattern

    :param r_inner: the inner radius of the encoder in mm
    :param widths: the width of encoder rings
    :param bits: the resolution of the encoder (number of rings) in number of bits
    :param mask: A masked out region in between each ring to reduce bleeding from channel to channel,
    defined as a ratio (0...1) of the provided width
    :param origin_x: The x coordinate in mm of the origin of the encoder
    :param origin_x: The y coordinate in mm of the origin of the encoder
    :param invert: Creates the inverted image of the encoder in a square area which saves a lot of copper etching
    """
    mask_width = widths * mask
    mask_offset = widths-(mask_width/2)
    chains = []

    # Start with the inner masking ring
    if mask > 0 and not invert:
        chains += [util.get_ring(r_inner, mask_width/2, origin_x, origin_y)]

    # Draw each of the encoder rings
    for bit in range(bits):
        ri = r_inner + (widths*bit) + mask_offset
        chains += util.get_encoder_ring(r_inner = ri, width=widths-mask_width, sections=2**bit, origin_x=origin_x, origin_y=origin_y)

        # Add a masking ring between consecutive encoder rings
        if mask > 0 and not invert:
            chains += [util.get_ring(ri+mask_offset, mask_width, origin_x, origin_y)]

    util.draw_polyshape(chains, invert)
