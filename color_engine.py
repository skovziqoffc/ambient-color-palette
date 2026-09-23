import numpy as np
from PIL import ImageGrab
from sklearn.cluster import KMeans

def ext_dom_colors(x1, y1, x2, y2, num_colors=5):   
    l = min(x1, x2)
    t = min(y1, y2)
    r = max(x1, x2)
    b = max(y1, y2)

    if r - l < 2 or b - t < 2:
        return []

    scr = ImageGrab.grab(bbox=(l, t,r , b))
    scr = scr.convert("RGB")
    scr.thumbnail((150, 150))
    
    pix = np.array(scr)
    pix_list = pix.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=num_colors, n_init=10, random_state=42)
    kmeans.fit(pix_list)
    
    dom_rgb = kmeans.cluster_centers_.astype(int)

    hex_colors = []
    for x in dom_rgb:
        hex_str = f"#{x[0]:02X}{x[1]:02X}{x[2]:02X}"
        hex_colors.append(hex_str)
        
    return hex_colors
