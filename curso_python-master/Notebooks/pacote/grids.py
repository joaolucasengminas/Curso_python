class Grid:
    
    def __init__(self, ox, oy, oz, nx, ny, nz, sx, sy, sz):
        
        self.ox = ox
        self.oy = oy
        self.oz = oz
        
        self.nx = nx
        self.ny = ny
        self.nz = nz
        
        self.sx = sx
        self.sy = sy
        self.sz = sz        
        
    def number_of_blocks(self):
        
        "This method calculates the number of blocks on a grid"
        
        return self.nx*self.ny*self.nz
    
    