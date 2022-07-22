import numpy as np
import matplotlib.pyplot as plt

def ex_no_cat_degrad():
    """
    Function to illustrate a catalytic cycle without catalyst degradation.
    
    Args:
        none.
       
    Returns:
        (graphs): Two graphs of [a] vs time, one plot of the collected data and one with a time shift.
    """
    x1 = np.linspace(0, 100, 19)
    y1 = 1 / (x1 + 20)
    x2 = np.linspace(0, 100, 10)
    y2 = 1 / (x2 + 40)

    plt.plot(x1, y1, 'o', label = 'Exp 1')
    plt.plot(x2, y2, 'o', label = 'Exp 2')
    plt.title('Same excess, different starting point')
    plt.xlabel('Time')
    plt.ylabel('[a]')
    plt.xticks([])
    plt.yticks([])
    shift_x = x2[0], x2[0] + 20
    shift_y = y2[0], y2[0]
    plt.plot(shift_x, shift_y, 'o--', label = 'Time shift', zorder = 1, markersize = 4)
    plt.legend()
    plt.show()

    x1 = np.linspace(0, 100, 19)
    y1 = 1 / (x1 + 20)
    x2 = np.linspace(0, 100, 10)
    y2 = 1 / (x2 + 40)

    plt.plot(x1, y1, 'o', label = 'Exp 1')
    plt.plot(x2 + 20, y2, 'o', label = 'Exp 2')
    plt.xlabel('Time')
    plt.ylabel('[a]')
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()

def ex_cat_degrad():
    """
    Function to illustrate a catalytic cycle without catalyst degradation.
    
    Args:
        none.
       
    Returns:
        (graphs): Two graphs of [a] vs time, one plot of the collected data and one with a time shift.
    """    
    x1 = np.linspace(0, 100, 19)
    y1 = 1 / (x1 + 20)
    x2 = np.linspace(0, 100, 10)
    y2 = 1 / (x2 ** 1.2 + 40)

    plt.plot(x1, y1, 'o', label = 'Exp 3')
    plt.plot(x2, y2, 'o', label = 'Exp 4')
    plt.title('Same excess, different starting point')
    plt.xlabel('Time')
    plt.ylabel('[a]')
    plt.xticks([])
    plt.yticks([])
    shift_x = x2[0], x2[0] + 20
    shift_y = y2[0], y2[0]
    plt.plot(shift_x, shift_y, 'o--', label = 'Time shift', zorder = 1, markersize = 4)
    plt.legend()
    plt.show()

    x1 = np.linspace(0, 100, 19)
    y1 = 1 / (x1 + 20)
    x2 = np.linspace(0, 100, 10)
    y2 = 1 / (x2 ** 1.2 + 40)

    plt.plot(x1, y1, 'o', label = 'Exp 3')
    plt.plot(x2 + 20, y2, 'o', label = 'Exp 4')
    plt.xlabel('Time')
    plt.ylabel('[a]')
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()
    
def ex_order_in_cat():
    """
    Function to illustrate determining the order of the catalyst in the reaction.
    
    Args:
        none.
       
    Returns:
        (graphs): Three graphs of [p] vs time, with varied parameter gamma (order in catalyst).
    """
    x1 = np.linspace(1, 101, 19)
    y1 = np.log(x1)
    x2 = np.linspace(1, 101, 10)
    y2 = np.log(x2 ** 1.4)

    plt.plot(x1, y1, 'o', label = 'Exp 1')
    plt.plot(x2, y2, 'o', label = 'Exp 2')
    plt.title('$\gamma$ = 0.0')
    plt.xlabel('t[cat]$^{\gamma}$')
    plt.ylabel('[p]')
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()

    x1 = np.linspace(1, 101, 19)
    y1 = np.log10(x1)
    x2 = np.linspace(1, 101, 10)
    y2 = np.log10(x2 ** 1.15)

    plt.plot(x1, y1, 'o', label = 'Exp 1')
    plt.plot(x2, y2, 'o', label = 'Exp 2')
    plt.title('$\gamma$ = 0.5')
    plt.xlabel('t[cat]$^{\gamma}$')
    plt.ylabel('[p]')
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()

    x1 = np.linspace(1, 101, 19)
    y1 = np.log10(x1)
    x2 = np.linspace(1, 101, 10)
    y2 = np.log10(x2)

    plt.plot(x1, y1, 'o', label = 'Exp 1')
    plt.plot(x2, y2, 'o', label = 'Exp 2')
    plt.title('$\gamma$ = 1.0')
    plt.xlabel('t[cat]$^{\gamma}$')
    plt.ylabel('[p]')
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()