import itertools
import numpy as np

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def print_counter_most_common(counter, n, name='Item', padding=30, stats=True):
    print(f'{name:<padding}Frequency')
    for item, count in counter.most_common(n):
            print(f'{item:<padding}{count}')

    if stats:
        vals = counter.values()
        lo = np.percentile(vals, 25)
        med = np.median(vals)
        up = np.percentile(vals, 75)
        print(f'\nLower Quartile: {lo}')
        print(f'Median:           {med}')
        print(f'Upper Quartile:   {up}')
        print(f'Upper Quartile:   {up}')

def flatten_lists(l):
    '''flatten_lists
    Unpacks nested lists into one list of elements.
    '''
    return list(itertools.chain(*l))
