import task4
import numpy as np
import matplotlib.pyplot as plt
def driver():
    clean_sin = task4.generate_sin_wave(2, (-2, 8), 1000)
    dirty_sin = clean_sin + np.random.randn(1000)*0.05
    cleaned_sin = task4.mean_filter(dirty_sin, k=1)
    x = np.linspace(-2, 8, num=1000)
    fig = plt.figure()
    plt.plot(x, clean_sin)
    plt.title('clean_sin')
    plt.savefig('clean_sin.png')

    fig = plt.figure()
    plt.plot(x, dirty_sin)
    plt.title('dirty_sin')
    plt.savefig('dirty_sin.png')

    fig = plt.figure()
    plt.plot(x, cleaned_sin)
    plt.title('cleaned_sin')
    plt.savefig('cleaned_sin.png')

driver()
