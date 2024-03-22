import pcbnew
from pcbnew import FromMM
import numpy as np


def draw_polyshape(chains, invert=False) -> None:
    """
    Create a compound polyshape from a list of closed chain objects
    """
    board = pcbnew.GetBoard()
    sps = pcbnew.SHAPE_POLY_SET()
    ps = pcbnew.PCB_SHAPE(board, pcbnew.SHAPE_T_POLY)

    for chain in chains:
        sps.AddOutline(chain)

    if invert:
        sps = invert_polyshape(sps)

    ps.SetPolyShape( sps )
    ps.SetFilled(True)

    board.Add(ps)
    pcbnew.Refresh()


def invert_polyshape(sps) -> pcbnew.SHAPE_POLY_SET:
    """
    Creates a rectangular shape of equal size to the provided polyshape and subtracts the polyshape from the rectangle
    """
    bbox = sps.BBox()
    container = pcbnew.SHAPE_POLY_SET()
    container.AddOutline(to_chain([(bbox.GetLeft(), bbox.GetBottom()), 
                                   (bbox.GetLeft(), bbox.GetTop()), 
                                   (bbox.GetRight(), bbox.GetTop()), 
                                   (bbox.GetRight(), bbox.GetBottom())]))
    container.BooleanSubtract(*[sps], 0)
    return container


def get_encoder_ring(r_inner:float, width:float, sections:int, origin_x:float = 0, origin_y:float = 0) -> list[pcbnew.SHAPE_LINE_CHAIN]:
    """
    Draw a ring with a specified number of equally spaced sections
    """
    angle = 360/sections
    chains = list()

    for i in range(sections):
        chains.append( get_arch(r_inner, width, angle=angle/2, rotation=angle*i, origin_x=origin_x, origin_y=origin_y) )
    return chains


def get_concentric_rings(r_inner:float, r_delta:float, width:float, n:int, origin_x:float = 0, origin_y:float = 0) -> list[pcbnew.SHAPE_LINE_CHAIN]:
    """
    Draw n concentric rings and return a list of chain objects
    """
    offset = width/2
    chains = []
    for i in range(n):
        ri = (r_inner + (r_delta*i)) - offset
        chains += [get_ring(ri, width, origin_x, origin_y)]
    return chains


def get_ring(r_inner:float, width:float, origin_x:float = 0, origin_y:float = 0) -> pcbnew.SHAPE_LINE_CHAIN:
    """
    Create a continuous ring shape
    """
    return get_arch(r_inner, width, angle=360, rotation=0, origin_x=origin_x, origin_y=origin_y)


def get_arch(r_inner:float, width:float, angle:float, rotation:float = 0, origin_x:float = 0, origin_y:float = 0) -> pcbnew.SHAPE_LINE_CHAIN:
    """
    Creates the vertices for an arch, a rainbow like shape
    """
    steps = int( np.ceil(angle/6) ) * 2
    angle = (angle/360)*2*np.pi
    phase = (rotation/360)*2*np.pi
    
    radians = np.linspace(0,angle,steps) + phase
    x = np.sin(radians)
    y = np.cos(radians)

    x = np.concatenate((x*r_inner, (x[::-1]*(r_inner+width)) )) + origin_x
    y = np.concatenate((y*r_inner, (y[::-1]*(r_inner+width)) )) + origin_y

    x = [FromMM(float(v)) for v in x] 
    y = [FromMM(float(v)) for v in y]

    return to_chain( list(zip(x,y)) )


def to_chain(verteces:list[tuple]) -> pcbnew.SHAPE_LINE_CHAIN:
    """
    Turn a list of verteces defined as tuples of x,y coordinates into a chain object for appending to a polyshape
    """
    chain = pcbnew.SHAPE_LINE_CHAIN()
    for (x,y) in verteces:
        chain.Append(x, y)
    chain.SetClosed(True)
    return chain


def to_gray(v:int, bits:int) -> int:
    """
    Convert an integer value to its gray encoded counterpart

    :param v: The value to be encoded
    :param bits: The resolution of the value in number of bits
    """
    gray = v ^ (v >> 1)
    gray |=  (v & (1<<(bits-1)))
    return gray


def from_gray(v:int, bits:int) -> int:
    """
    Convert a gray encoded value to its binary encoded counterpart

    :param v: The gray value to be decoded
    :param bits: The resolution of the value in number of bits
    """
    bits -= 1
    b = v & (1<<bits)
    while bits > 0:
        bits -= 1
        b |= ((b >> 1) ^ v) & (1<<bits)
    return b