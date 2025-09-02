# imports
import numpy as np
from matplotlib import pyplot as plt

def xy2pol(x,y,xz,yz):
    """
    convert cartesian (x-y) coordinates to polar (r-theta) coordinates
    
    params
    ------
    x : float, x-coord of star on image
    y : float, y-coord of star on image
    xz : float, x-coord of zenith on image
    yz : float, y-coord of zenith on image
    
    output
    ------
    r : float, distance from zenith to star in pixels
    theta : float, angle of star around zenith point
    """
    
    # find x and y lengths from the zenith and calculate r
    x_len = x - xz
    y_len = y - yz
    r = np.sqrt(x_len**2 + y_len**2)
    
    # find theta        
    if x_len < 0 and y_len < 0: # if x_len and y_len are negative...
        theta = np.arccos(-y_len/r)
        theta = theta*180/np.pi    
    elif x_len < 0 and y_len > 0: # if x_len is negative and y_len is positive...
        theta = np.pi/2 + np.arccos(-x_len/r)
        theta = theta*180/np.pi  
    elif x_len > 0 and y_len > 0: # if x_len and y_len are positive...
        theta = np.pi + np.arccos(y_len/r)
        theta = theta*180/np.pi   
    elif x_len > 0 and y_len < 0: # if x_len is positive and y_len is negative...
        theta = 3/2*np.pi + np.arccos(x_len/r)
        theta = theta*180/np.pi   
    # when x or y = 0
    elif x_len == 0 and y_len > 0: # if x_len = 0 and y_len is positive...
        theta = 0 
    elif x_len < 0 and y_len == 0: # if x_len is negative and y_len = 0...
        theta = 90 
    elif x_len == 0 and y_len < 0: # if x_len = 0 and y_len is negative...
        theta = 180
    elif x_len > 0 and y_len == 0: # if x_len is positive and y_len = 0...
        theta = 270
    else:
        raise Exception("xy2pol - something wrong with x_len y_len if/else loop")
        
    return r, theta

def tod(a, b, c):
    """
    convert from hh mm ss to decimals
    """
    return a + b/60 + c/3600

# star collection [name, x, y, r, theta, alt, az]
def gimmiestars(xz, yz):
    star1 = ['5 Lac', 789, 202, xy2pol(789,202,xz,yz)[0], xy2pol(789,202,xz,yz)[1], tod(5, 16, 41.2), tod(36, 57, 55.7)]
    star2 = ['HJ1796', 1047, 77, xy2pol(1047,77,xz,yz)[0], xy2pol(1047,77,xz,yz)[1], tod(9, 48, 36.7), tod(28, 56, 6.1)]
    star3 = ['21 Cep', 1065, 146, xy2pol(1065, 146,xz,yz)[0], xy2pol(1065, 146,xz,yz)[1], tod(13, 37, 25.9), tod(30, 1, 48.8)]
    star4 = ['Erakis', 1079, 220, xy2pol(1079, 220,xz,yz)[0], xy2pol(1079, 220,xz,yz)[1], tod(16, 10, 58.1), tod(30, 57, 9.4)]
    star5 = ['Alphirk', 1375, 195, xy2pol(1375, 195,xz,yz)[0], xy2pol(1375, 195,xz,yz)[1], tod(22, 45, 24.9), tod(20, 27, 39.2)]
    star6 = ['Alahakan', 1685, 387, xy2pol(1685, 387,xz,yz)[0], xy2pol(1685, 387,xz,yz)[1], tod(37, 7, 6.9), tod(18, 0, 20.1)]
    star7 = ['Kochab', 2123, 435, xy2pol(2123, 435,xz,yz)[0], xy2pol(2123, 435,xz,yz)[1], tod(44, 35, 33.1), tod(1, 25, 38.3)]
    star8 = ['Dubhe', 2819, 450, xy2pol(2819, 450,xz,yz)[0], xy2pol(2819, 450,xz,yz)[1], tod(42, 27, 41.6), tod(329, 11, 36.2)]
    star9 = ['Giausar', 2584, 365, xy2pol(2584, 365,xz,yz)[0], xy2pol(2584, 365,xz,yz)[1], tod(41, 45, 37.7), tod(340, 3, 48.9)]
    star10 = ['44 Lyn', 3038, 330, xy2pol(3038, 330,xz,yz)[0], xy2pol(3038, 330,xz,yz)[1], tod(33, 25, 39.7), tod(321, 41, 44.8)]
    star11 = ['17 UMa', 3062, 260, xy2pol(3062, 260,xz,yz)[0], xy2pol(3062, 260,xz,yz)[1], tod(29, 13, 44.8), tod(321, 43, 30.9)]
    star12 = ['Alhaud V', 3196, 370, xy2pol(3196, 370,xz,yz)[0], xy2pol(3196, 370,xz,yz)[1], tod(30, 55, 29.9), tod(315, 30, 36.5)]
    star13 = ['Merak', 2953, 550, xy2pol(2953, 550,xz,yz)[0], xy2pol(2953, 550,xz,yz)[1], tod(43, 44, 0.1), tod(322, 2, 27.3)]
    star14 = ['Altheba IV', 2740, 105, xy2pol(2740, 105,xz,yz)[0], xy2pol(2740, 105,xz,yz)[1], tod(29, 3, 32), tod(334, 18, 52.6)]
    star15 = ['Deneb', 778, 638, xy2pol(778, 638,xz,yz)[0], xy2pol(778, 638,xz,yz)[1], tod(18, 59, 11.8), tod(47, 57, 20.3)]
    star16 = ['o1 Cyg', 870, 706, xy2pol(870, 706,xz,yz)[0], xy2pol(870, 706,xz,yz)[1], tod(24, 0, 38.6), tod(48, 13, 34.5)]
    star17 = ['o2 Cyg', 883, 677, xy2pol(883, 677,xz,yz)[0], xy2pol(883, 677,xz,yz)[1], tod(23, 59, 58.3), tod(47, 6, 29.3)]
    star18 = ['Grumium', 1485, 799, xy2pol(1485, 799,xz,yz)[0], xy2pol(1485, 799,xz,yz)[1], tod(45, 31, 5.6), tod(36, 22, 31.8)]
    star19 = ['Athebyne', 1850, 765, xy2pol(1850, 765,xz,yz)[0], xy2pol(1850, 765,xz,yz)[1], tod(52, 38, 25.7), tod(21, 0, 53.3)]
    star20 = ['RR UMi', 2139, 655, xy2pol(2139, 655,xz,yz)[0], xy2pol(2139, 655,xz,yz)[1], tod(52, 41, 32), tod(3, 43, 14.7)]
    star21 = ['Thuban', 2348, 650, xy2pol(2348, 650,xz,yz)[0], xy2pol(2348, 650,xz,yz)[1], tod(54, 5, 2.1), tod(354, 17, 47.8)]
    star22 = ['Edasich', 2060, 850, xy2pol(2060, 850,xz,yz)[0], xy2pol(2060, 850,xz,yz)[1], tod(58, 37, 19.2), tod(12, 17, 17.7)]
    star23 = ['Mizar', 2554, 876, xy2pol(2554, 876,xz,yz)[0], xy2pol(2554, 876,xz,yz)[1], tod(60, 53, 54.8), tod(338, 48, 37.1)]
    star24 = ['Alioth', 2650, 803, xy2pol(2650, 803,xz,yz)[0], xy2pol(2650, 803,xz,yz)[1], tod(57, 26, 39.6), tod(333, 36, 32.9)]
    star25 = ['Phecda', 2885, 737, xy2pol(2885, 737,xz,yz)[0], xy2pol(2885, 737,xz,yz)[1], tod(51, 37, 54.6), tod(321, 51, 28.1)]
    star26 = ['Tania Australis', 3384, 737, xy2pol(3384, 737,xz,yz)[0], xy2pol(3384, 737,xz,yz)[1], tod(38, 0, 20.1), tod(301, 56, 22.9)]
    star27 = [r'$\psi$ UMa', 3200, 832, xy2pol(3200, 832,xz,yz)[0], xy2pol(3200, 832,xz,yz)[1], tod(46, 44, 46.8), tod(305, 35, 21.5)]
    star28 = ['Fawaris III', 401, 846, xy2pol(401, 846,xz,yz)[0], xy2pol(401, 846,xz,yz)[1], tod(6, 51, 48.2), tod(59, 1, 12.4)]
    star29 = ['Aljanah', 523, 871, xy2pol(523, 871,xz,yz)[0], xy2pol(523, 871,xz,yz)[1], tod(13, 33, 8.2), tod(58, 19, 16.8)]
    star30 = ['13 Lyr', 1053, 1005, xy2pol(1053, 1005,xz,yz)[0], xy2pol(1053, 1005,xz,yz)[1], tod(36, 52, 29.5), tod(54, 37, 6.2)]
    star31 = ['Eltanin', 1400, 935, xy2pol(1400, 935,xz,yz)[0], xy2pol(1400, 935,xz,yz)[1], tod(46, 26, 12.5), tod(44, 2, 16.9)]
    star32 = ['Rastaban', 1512, 955, xy2pol(1512, 955,xz,yz)[0], xy2pol(1512, 955,xz,yz)[1], tod(50, 7, 19.6), tod(41, 16, 59.3)]
    star33 = ['Alkaid', 2520, 1062, xy2pol(2520, 1062,xz,yz)[0], xy2pol(2520, 1062,xz,yz)[1], tod(67, 34, 1.6), tod(339, 23, 17.3)]
    star34 = ['13 Boo', 2424, 1082, xy2pol(2424, 1082,xz,yz)[0], xy2pol(2424, 1082,xz,yz)[1], tod(68, 42, 37.5), tod(347, 56, 7.7)]
    star35 = ['TU CVn', 2774, 1035, xy2pol(2774, 1035,xz,yz)[0], xy2pol(2774, 1035,xz,yz)[1], tod(63, 15, 31.7), tod(320, 16, 36.4)]
    star36 = ['Alula Borealis', 3385, 1143, xy2pol(3385, 1143,xz,yz)[0], xy2pol(3385, 1143,xz,yz)[1], tod(48, 2, 40.7), tod(288, 37, 53.9)]
    star37 = [r'$\alpha$ Lyn', 3623, 640, xy2pol(3623, 640,xz,yz)[0], xy2pol(3623, 640,xz,yz)[1], tod(24, 38, 46.3), tod(297, 7, 32.4)]
    star38 = ['Rasalas', 3747, 975, xy2pol(3747, 975,xz,yz)[0], xy2pol(3747, 975,xz,yz)[1], tod(28, 17, 16.4), tod(285, 44, 28.4)]
    star39 = ['Algenubi', 3795, 1000, xy2pol(3795, 1000,xz,yz)[0], xy2pol(3795, 1000,xz,yz)[1], tod(26, 1, 42), tod(284, 1, 47.7)]
    star40 = ['Alterf', 3828, 955, xy2pol(3828, 955,xz,yz)[0], xy2pol(3828, 955,xz,yz)[1], tod(22, 43, 40.2), tod(284, 33, 50.3)]
    star41 = ['Algieba', 3737, 1148, xy2pol(3737, 1148,xz,yz)[0], xy2pol(3737, 1148,xz,yz)[1], tod(31, 54, 26.7), tod(276, 28, 54.1)]
    star42 = ['Regulus', 3780, 1255, xy2pol(3780, 1255,xz,yz)[0], xy2pol(3780, 1255,xz,yz)[1], tod(26, 7, 11.9), tod(269, 35, 50.7)]
    star43 = ['Subra', 3955, 1335, xy2pol(3955, 1335,xz,yz)[0], xy2pol(3955, 1335,xz,yz)[1], tod(19, 14, 0.8), tod(270, 51, 9.9)]
    star44 = ['Zosma', 3547, 1395, xy2pol(3547, 1395,xz,yz)[0], xy2pol(3547, 1395,xz,yz)[1], tod(43, 58, 31.9), tod(271, 24, 15.6)]
    star45 = ['Chertan', 3583, 1462, xy2pol(3583, 1462,xz,yz)[0], xy2pol(3583, 1462,xz,yz)[1], tod(42, 1, 19.7), tod(264, 58, 13.7)]
    star46 = ['Denebola', 3453, 1538, xy2pol(3453, 1538,xz,yz)[0], xy2pol(3453, 1538,xz,yz)[1], tod(49, 11, 23.1), tod(258, 34, 3.2)]
    star47 = ['Cor Caroli', 2882, 1281, xy2pol(2882, 1281,xz,yz)[0], xy2pol(2882, 1281,xz,yz)[1], tod(67, 23, 34.3), tod(301, 19, 20.2)]
    star48 = ['AW CVn', 2623, 1490, xy2pol(2623, 1490,xz,yz)[0], xy2pol(2623, 1490,xz,yz)[1], tod(79, 13, 19.3), tod(304, 20, 6.9)]
    star49 = ['Xuange', 2468, 1240, xy2pol(2468, 1240,xz,yz)[0], xy2pol(2468, 1240,xz,yz)[1], tod(72, 18, 52.6), tod(349, 16, 55.1)]
    star50 = ['Seginus', 2370, 1423, xy2pol(2370, 1423,xz,yz)[0], xy2pol(2370, 1423,xz,yz)[1], tod(80, 27, 13.4), tod(356, 32, 35.7)]
    star51 = ['Nekkar', 2197, 1380, xy2pol(2197, 1380,xz,yz)[0], xy2pol(2197, 1380,xz,yz)[1], tod(77, 8, 24.8), tod(23, 37, 46.5)]
    star52 = ['v2 Boo', 2032, 1375, xy2pol(2032, 1375,xz,yz)[0], xy2pol(2032, 1375,xz,yz)[1], tod(73, 13, 38.3), tod(39, 55, 5.2)]
    star53 = [r'$\sigma$ Her', 1875, 1180, xy2pol(1875, 1180,xz,yz)[0], xy2pol(1875, 1180,xz,yz)[1], tod(62, 24, 41.3), tod(52, 14, 40.1)]
    star54 = [r'$\eta$ Her', 1720, 1319, xy2pol(1720, 1319,xz,yz)[0], xy2pol(1720, 1319,xz,yz)[1], tod(61, 44, 58.9), tod(60, 26, 10.2)]
    star55 = [r'$\pi$ Her', 1436, 1410, xy2pol(1436, 1410,xz,yz)[0], xy2pol(1436, 1410,xz,yz)[1], tod(55, 40, 50.5), tod(65, 50, 47.1)]
    star56 = ['RBR 48', 1495, 1306, xy2pol(1495, 1306,xz,yz)[0], xy2pol(1495, 1306,xz,yz)[1], tod(56, 26, 35.3), tod(58, 36, 0.1)]
    star57 = ['Vega', 1050, 1187, xy2pol(1050, 1187,xz,yz)[0], xy2pol(1050, 1187,xz,yz)[1], tod(39, 39, 41.9), tod(61, 41, 1.1)]
    star58 = [r'$\delta$2 Lyr', 946, 1189, xy2pol(946, 1189,xz,yz)[0], xy2pol(946, 1189,xz,yz)[1], tod(35, 55, 46.2), tod(63, 17, 55)]
    star59 = [r'$\eta$ Cyg', 660, 1112, xy2pol(660, 1112,xz,yz)[0], xy2pol(660, 1112,xz,yz)[1], tod(23, 25, 51.8), tod(61, 26, 0.1)]
    star60 = ['Albireo', 660, 1315, xy2pol(660, 1315,xz,yz)[0], xy2pol(660, 1315,xz,yz)[1], tod(26, 7, 31.4), tod(70, 51, 1.1)]
    star61 = ['Sualocin', 288, 1305, xy2pol(288, 1305,xz,yz)[0], xy2pol(288, 1305,xz,yz)[1], tod(6, 42, 52.1), tod(75, 21, 2.4)]
    star62 = [r'$\gamma$ Sge', 435, 1438, xy2pol(435, 1438,xz,yz)[0], xy2pol(435, 1438,xz,yz)[1], tod(16, 56, 36.9), tod(76, 33, 11.3)]
    star63 = ['13 Sge', 408, 1488, xy2pol(408, 1488,xz,yz)[0], xy2pol(408, 1488,xz,yz)[1], tod(15, 49, 7.2), tod(78, 16, 22.9)]
    star64 = ['Anser', 626, 1410, xy2pol(626, 1410,xz,yz)[0], xy2pol(626, 1410,xz,yz)[1], tod(25, 22, 9.9), tod(74, 26, 43.8)]
    star65 = [r'$\mu$ Her', 1188, 1615, xy2pol(1188, 1615,xz,yz)[0], xy2pol(1188, 1615,xz,yz)[1], tod(48, 6, 58.3), tod(79, 24, 27.5)]
    star66 = ['Tarazed', 398, 1735, xy2pol(398, 1735,xz,yz)[0], xy2pol(398, 1735,xz,yz)[1], tod(15, 44, 17.6), tod(86, 14, 26.9)]
    star67 = ['Altair', 365, 1766, xy2pol(365, 1766,xz,yz)[0], xy2pol(365, 1766,xz,yz)[1], tod(13, 57, 6.2), tod(87, 18, 34)]
    star68 = ['Rutilicus', 1600, 1607, xy2pol(1600, 1607,xz,yz)[0], xy2pol(1600, 1607,xz,yz)[1], tod(62, 39, 21.6), tod(76, 3, 24.9)]
    star69 = ['Thiba', 2130, 1593, xy2pol(2130, 1593,xz,yz)[0], xy2pol(2130, 1593,xz,yz)[1], tod(80, 12, 30.3), tod(59, 47, 41.2)]
    star70 = ['Nusakan', 2053, 1717, xy2pol(2053, 1717,xz,yz)[0], xy2pol(2053, 1717,xz,yz)[1], tod(78, 26, 5.2), tod(85, 5, 23.8)]
    star71 = ['Alphecca', 2008, 1787, xy2pol(2008, 1787,xz,yz)[0], xy2pol(2008, 1787,xz,yz)[1], tod(76, 37, 56.9), tod(95, 14, 52.6)]
    star72 = [r'$\gamma$ CrB', 1955, 1798, xy2pol(1955, 1798,xz,yz)[0], xy2pol(1955, 1798,xz,yz)[1], tod(74, 47, 4), tod(95, 17, 5)]
    star73 = [r'$\delta$ CrB', 1913, 1803, xy2pol(1913, 1803,xz,yz)[0], xy2pol(1913, 1803,xz,yz)[1], tod(73, 14, 11.8), tod(94, 47, 48.8)]
    star74 = [r'$\epsilon$ CrB', 1859, 1778, xy2pol(1859, 1778,xz,yz)[0], xy2pol(1859, 1778,xz,yz)[1], tod(71, 39, 27.4), tod(90, 55, 33.7)]
    star75 = ['Aulad Alnathlat', 2205, 1775, xy2pol(2205, 1775,xz,yz)[0], xy2pol(2205, 1775,xz,yz)[1], tod(83, 13, 51.4), tod(103, 51, 18.5)]
    star76 = ['Izar', 2332, 1763, xy2pol(2332, 1763,xz,yz)[0], xy2pol(2332, 1763,xz,yz)[1], tod(87, 12, 11.2), tod(126, 51, 12.1)]
    star77 = [r'$\rho$ Boo', 2405, 1655, xy2pol(2405, 1655,xz,yz)[0], xy2pol(2405, 1655,xz,yz)[1], tod(88, 16, 8.3), tod(337, 4, 43.3)]
    star78 = ['Denebola', 3482, 1756, xy2pol(3482, 1756,xz,yz)[0], xy2pol(3482, 1756,xz,yz)[1], tod(49, 11, 10.3), tod(258, 34, 13.4)]
    star79 = [r'$\rho$ Leo', 3793, 1790, xy2pol(3793, 1790,xz,yz)[0], xy2pol(3793, 1790,xz,yz)[1], tod(30, 14, 42), tod(263, 48, 21.6)]
    star80 = ['24 Com A', 3195, 1788, xy2pol(3195, 1788,xz,yz)[0], xy2pol(3195, 1788,xz,yz)[1], tod(60, 45, 13.7), tod(255, 45, 27.9)]
    star81 = ['Arcturus', 2553, 1965, xy2pol(2553, 1965,xz,yz)[0], xy2pol(2553, 1965,xz,yz)[1], tod(79, 13, 52), tod(207, 54, 49.9)]
    star82 = ['Gudja', 1909, 2034, xy2pol(1909, 2034,xz,yz)[0], xy2pol(1909, 2034,xz,yz)[1], tod(70, 26, 16.9), tod(118, 54, 52.6)]
    star83 = ['Kornephoros', 1629, 1910, xy2pol(1629, 1910,xz,yz)[0], xy2pol(1629, 1910,xz,yz)[1], tod(63, 25, 13.7), tod(99, 20, 14.4)]
    star84 = ['Rasalgethi', 1304, 2057, xy2pol(1304, 2057,xz,yz)[0], xy2pol(1304, 2057,xz,yz)[1], tod(50, 25, 47.1), tod(102, 35, 7.5)]
    star85 = ['Rasalhague', 1160, 2070, xy2pol(1160, 2070,xz,yz)[0], xy2pol(1160, 2070,xz,yz)[1], tod(45, 38, 2.5), tod(101, 50, 49.1)]
    star86 = ['72 Oph', 1160, 2070, xy2pol(1160, 2070,xz,yz)[0], xy2pol(1160, 2070,xz,yz)[1], tod(37, 13, 24.4), tod(100, 14, 12.9)]
    star87 = ['Alava', 805, 2392, xy2pol(805, 2392,xz,yz)[0], xy2pol(805, 2392,xz,yz)[1], tod(27, 15, 52.7), tod(110, 15, 33.5)]
    star88 = [r'$\kappa$ Oph', 1404, 2225, xy2pol(1404, 2225,xz,yz)[0], xy2pol(1404, 2225,xz,yz)[1], tod(51, 21, 7.4), tod(112, 48, 41.4)]
    star89 = ['Unukalhai', 1934, 2366, xy2pol(1934, 2366,xz,yz)[0], xy2pol(1934, 2366,xz,yz)[1], tod(62, 17, 49), tod(140, 22, 18.6)]
    star90 = ['Minelova', 3153, 2265, xy2pol(3153, 2265,xz,yz)[0], xy2pol(3153, 2265,xz,yz)[1], tod(55, 20, 56.5), tod(227, 25, 2.6)]
    star91 = ['FW Vir', 3268, 2265, xy2pol(3268, 2265,xz,yz)[0], xy2pol(3268, 2265,xz,yz)[1], tod(51, 20, 9.1), tod(231, 4, 29)]
    star92 = ['Porrima', 3253, 2364, xy2pol(3253, 2364,xz,yz)[0], xy2pol(3253, 2364,xz,yz)[1], tod(49, 23, 56.6), tod(226, 41, 9.1)]
    star93 = ['Zavijava', 3550, 2122, xy2pol(3550, 2122,xz,yz)[0], xy2pol(3550, 2122,xz,yz)[1], tod(42, 30, 2.6), tod(242, 49, 8.6)]
    star94 = ['u Leo', 3630, 2146, xy2pol(3630, 2146,xz,yz)[0], xy2pol(3630, 2146,xz,yz)[1], tod(38, 12, 2.4), tod(242, 59, 18.5)]
    star95 = ['e Leo', 3670, 2183, xy2pol(3670, 2183,xz,yz)[0], xy2pol(3670, 2183,xz,yz)[1], tod(35, 32, 40.2), tod(242, 9, 51.4)]
    star96 = ['p2 Leo', 3800, 2060, xy2pol(3800, 2060,xz,yz)[0], xy2pol(3800, 2060,xz,yz)[1], tod(30, 12, 9.6), tod(247, 47, 22)]
    star97 = ['v Hya', 3825, 2391, xy2pol(3825, 2391,xz,yz)[0], xy2pol(3825, 2391,xz,yz)[1], tod(19, 38, 38.7), tod(237, 40, 50)]
    star98 = [r'$\delta$ Crt', 3695, 2380, xy2pol(3695, 2380,xz,yz)[0], xy2pol(3695, 2380,xz,yz)[1], tod(25, 57, 2), tod(233, 43, 8.8)]
    star99 = [r'$\gamma$ Crt', 3706, 2464, xy2pol(3706, 2464,xz,yz)[0], xy2pol(3706, 2464,xz,yz)[1], tod(24, 53, 43.5), tod(230, 22, 47.2)]
    star100 = [r'$\xi$ Vir', 3274, 2535, xy2pol(3274, 2535,xz,yz)[0], xy2pol(3274, 2535,xz,yz)[1], tod(44, 0, 27.2), tod(221, 14, 39.1)]
    star101 = ['Gienah', 3395, 2717, xy2pol(3395, 2717,xz,yz)[0], xy2pol(3395, 2717,xz,yz)[1], tod(32, 56, 8.3), tod(219, 59, 29.7)]
    star102 = ['Minkar', 3398, 2825, xy2pol(3398, 2825,xz,yz)[0], xy2pol(3398, 2825,xz,yz)[1], tod(28, 2, 49), tod(217, 47, 4.6)]
    star103 = ['Kraz', 3255, 2905, xy2pol(3255, 2905,xz,yz)[0], xy2pol(3255, 2905,xz,yz)[1], tod(30, 26, 23.1), tod(211, 56, 11.7)]
    star104 = ['Spica', 2960, 2718, xy2pol(2960, 2718,xz,yz)[0], xy2pol(2960, 2718,xz,yz)[1], tod(46, 45, 32.2), tod(204, 56, 10.8)]

    stars = [star1, star2, star3, star4, star5, star6, star7, star8, star9, star10, star11, star12, star13, star14, star15, star16, star17, star18, star19, star20, star21, star22, star23, star24, star25, star26, star27, star28, star29, star30, star31, star32, star33, star34, star35, star36, star37, star38, star39, star40, star41, star42, star43, star44, star45, star46, star47, star48, star49, star50, star51, star52, star53, star54, star55, star56, star57, star58, star59, star60, star61, star62, star63, star64, star65, star66, star67, star68, star69, star70, star71, star72, star73, star74, star75, star76, star77, star78, star79, star80, star81, star82, star83, star84, star85, star86, star87, star88, star89, star90, star91, star92, star93, star94, star95, star96, star97, star98, star99, star100, star101, star102, star103, star104]
    
    return stars
