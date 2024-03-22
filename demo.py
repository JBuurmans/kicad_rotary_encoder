from rotary_encoder import absolute_encoder as ae


# Binary encoded examples:
ae.encoder(r_inner = 8, 
        width = 4, 
        bits = 4, 
        mask = 0,
        gray = False, 
        origin_x = 50,
        origin_y = 50,
        invert = False)

ae.encoder(r_inner = 5, 
        width = 2, 
        bits = 9, 
        mask = 0,
        gray = False, 
        origin_x = 100,
        origin_y = 50,
        invert = False)

ae.encoder(r_inner = 8, 
        width = 3, 
        bits = 5, 
        mask = 0.5,
        gray = False, 
        origin_x = 150,
        origin_y = 50,
        invert = False)

ae.encoder(r_inner = 8, 
        width = 3, 
        bits = 6, 
        mask = 0.5,
        gray = False, 
        origin_x = 200,
        origin_y = 50,
        invert = True)


# Gray encoded examples:
ae.encoder(r_inner = 8, 
        width = 4, 
        bits = 4, 
        mask = 0,
        gray = True, 
        origin_x = 50,
        origin_y = 100,
        invert = False)

ae.encoder(r_inner = 5, 
        width = 2, 
        bits = 9, 
        mask = 0,
        gray = True, 
        origin_x = 100,
        origin_y = 100,
        invert = False)

ae.encoder(r_inner = 8, 
        width = 3, 
        bits = 5, 
        mask = 0.5,
        gray = True, 
        origin_x = 150,
        origin_y = 100,
        invert = False)

ae.encoder(r_inner = 8, 
        width = 3, 
        bits = 6, 
        mask = 0.5,
        gray = True, 
        origin_x = 200,
        origin_y = 100,
        invert = True)