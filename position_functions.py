# imports
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as patches
import star_collection
import scipy.optimize as opt

# position function
def starpos(stars_list, inspection_radius):
    """
    collect the x-y, ra-dec & alt-az coordinates of each star for graphical comparison
    
    params
    ------
    stars : list/array, contains all coordinates for all collected stars in the image 
    inspection_radius : int, radius from the zenith of stars to look at in pixels
            
    output
    ------
    alt-r fit, az-theta fit
    """
    
    # define the radius in which the stars will be looked at
    stars = []
    for star in stars_list: # get rid of the pesky distorted stars at the edge
        if star[3] < inspection_radius:
            stars.append(star)
    
    # define empty lists for the coords to go
    x = []
    y = []
    r = []
    theta = []
    alt = []
    az = []
    outliers = []
    x_o = []
    y_o = []
    theta_o = []
    az_o = []
    alt_prop = []

    # add the coordinates for each star
    for star in stars:
        x.append(star[1])
        y.append(star[2])
        r.append(star[3])
        theta.append(star[4])
        alt.append(star[5])
        az.append(star[6])
        alt_prop.append(90/(star[5]))
    
    # check values
    if len(x) == 0:
        raise ValueError('no x values')
    if len(y) == 0:
        raise ValueError('no y values')
    if len(r) == 0:
        raise ValueError('no r values')
    if len(theta) == 0:
        raise ValueError('no theta values')
    if len(alt) == 0:
        raise ValueError('no alt values')
    if len(az) == 0:
        raise ValueError('no az values')
    
    return x, y, r, theta, alt, az, alt_prop

# define what an area is (aka the image area for the image we are looking at)
class area:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.center = [x1 + (x2 - x1)/2, y1 + (y2 - y1)/2]
        
        left = self.center[0] - (self.center[0] - x1)/2
        right = self.center[0] + (self.center[0] - x1)/2
        up = self.center[1] + (self.center[1] - y1)/2
        down = self.center[1] - (self.center[1] - y1)/2
        self.quads = [[left, up], [right, up], [left, down], [right, down]]
        
# expected fit
def cosfit(x, a, b, c):
  return a*np.cos(b*x) + c

def chisquare(obs, exp):
    top = (obs - exp)**2
    bottom = exp
    return sum(top / bottom)

def plot_img(img, save=False, name=None): # plot the image with the dark axis
    plt.figure(facecolor='#050505')
    plt.gca().tick_params(axis='x', colors='#aaaaaa')
    plt.gca().tick_params(axis='y', colors='#aaaaaa')
    plt.imshow(img)
    plt.xlim(0, img.shape[1])
    plt.ylim(img.shape[0], 0)
    if save == True:
        plt.savefig(f'{name}.pdf', bbox_inches='tight')

def optimal_quadrant(inspection_area):
    """
    determine the quadrant containing the zenith point in a given image
    this only gives the quadrant with the best fit 
    the actual zenith point must be found by executing this function multiple times
    
    1. the original area given by [x1, x2, y1, y2] is split into quadrants
    2. the centre point of each quadrant is taken to be the image centre
    3. the predicted positions of the star sample are compared with their actual positions
    4. the best fitting (by chi-square) quadrant is declared the optimal quadrant
    
    params
    ------
    x1, x2 : min and max x values defining the inspection area
    y1, y2 : min and max y values defining the inspection area
    
    output
    ------
    optimal_quadrant : the [x, y] coordinates of the centre of the quadrant containing the zenith point (best fitting values)
    x1_new, x2_new, y1_new, y2_new : the new parameters of the inspection area (to be used in the repeat use of this function)
    """
    # 1. DEFINE QUADRANTS
    q = inspection_area.quads

    # 2. DEFINE STAR COORDINATES WITH THE CENTRES OF EACH QUADRANT
    stars1 = star_collection.gimmiestars(q[0][0], q[0][1])
    stars2 = star_collection.gimmiestars(q[1][0], q[1][1])
    stars3 = star_collection.gimmiestars(q[2][0], q[2][1])
    stars4 = star_collection.gimmiestars(q[3][0], q[3][1])

    inspection_radius = 3000 # pix
    x1, y1, r1, theta1, alt1, az1, alt_prop1 = starpos(stars1, inspection_radius)
    x2, y2, r2, theta2, alt2, az2, alt_prop2 = starpos(stars2, inspection_radius)
    x3, y3, r3, theta3, alt3, az3, alt_prop3 = starpos(stars3, inspection_radius)
    x4, y4, r4, theta4, alt4, az4, alt_prop4 = starpos(stars4, inspection_radius)
    
    # 3. COMPARE THE EXPECTED AND PREDICTED VALUES FOR THE STAR POSITIONS FOR EACH QUADRANT
    chisq = [] # place to put chisq values for each quadrant
    rs = [r1, r2, r3, r4]
    alts = [alt1, alt2, alt3, alt4]
    for i in range(4):
        popt_cos, pcov_cos = opt.curve_fit(cosfit, rs[i], alts[i], [90, 0.0008, 0], maxfev=50_000) # create a fit to the data
        chisq.append(chisquare(alts[i], cosfit(np.array(rs[i]), *popt_cos))) # determine the goodness of fit for each quadrant
    optimal_quadrant_ctr = q[np.argmin(chisq)]
    
    # 4. DEFINE A NEW QUADRANT
    distx = (inspection_area.x2 - inspection_area.x1)/4 # pixel distance from the centre to edge of quadrant
    disty = (inspection_area.y2 - inspection_area.y1)/4 # pixel distance from the centre to edge of quadrant
    x1_new = optimal_quadrant_ctr[0] - distx
    x2_new = optimal_quadrant_ctr[0] + distx
    y1_new = optimal_quadrant_ctr[1] - disty
    y2_new = optimal_quadrant_ctr[1] + disty
    optimal_quadrant = area(x1_new, x2_new, y1_new, y2_new)
    
    return optimal_quadrant

# function to find the zenith
def zenith_finder(initial_image, visualise=True, img=None, save=False, name=None):
    """
    find the pixel coordinates of the zenith using the optimal quadrant algorithm
    
    params
    ------
    initial_image : class~area containing x and y coordinates which define the image dimensions
    
    output
    ------
    zenith_position : (x, y) coordinates of the zenith position in pixels
    optimal quadrant visualisation (optional)    
    """
    # find the zenith position using the optimal quadrant algorithm (figure out how to loop this when you're less tired)
    q1 = optimal_quadrant(initial_image)
    q2 = optimal_quadrant(q1)
    q3 = optimal_quadrant(q2)
    q4 = optimal_quadrant(q3)
    q5 = optimal_quadrant(q4)
    q6 = optimal_quadrant(q5)
    q7 = optimal_quadrant(q6)
    q8 = optimal_quadrant(q7)
    q9 = optimal_quadrant(q8)
    q10 = optimal_quadrant(q9)
    q11 = optimal_quadrant(q10)
    q12 = optimal_quadrant(q11)
    q13 = optimal_quadrant(q12)
    q14 = optimal_quadrant(q13)
    q15 = optimal_quadrant(q14)
    q16 = optimal_quadrant(q15)
    q17 = optimal_quadrant(q16)
    q18 = optimal_quadrant(q17)
    q19 = optimal_quadrant(q18)
    q20 = optimal_quadrant(q19)
    quads = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
    zenith_position = [quads[-1].center[0], quads[-1].center[1]] # the center of the final quadrant (now smaller than a pixel)
    
    # plot the visualiser if requested
    if visualise == True:
        # plt.rcParams["figure.figsize"] = [20,20]
        plot_img(img)
        plt.plot(initial_image.center[0], initial_image.center[1])

        for quad in quads:
            plt.plot(quad.center[0], quad.center[1], 'rx')
            plt.gca().add_patch(patches.Rectangle((quad.x1, quad.y1), quad.x2-quad.x1, quad.y2-quad.y1, linewidth=1, edgecolor='none', facecolor='green', alpha=0.2))
        plt.plot(quads[-1].center[0], quads[-1].center[1], 'bx')
        plt.gca().add_patch(patches.Rectangle((quads[-1].x1, quads[-1].y1), quads[-1].x2-quads[-1].x1, quads[-1].y2-quads[-1].y1, linewidth=1, edgecolor='none', facecolor='green', alpha=0.2))
        if save == True:
            plt.savefig(f'{name}.pdf', bbox_inches='tight')
        plt.show()
    
    return zenith_position