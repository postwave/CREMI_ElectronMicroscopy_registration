def deconv(size, stride, padding, Filter):
    '''compute deconv size: deconv(size, stride, padding, Filter)'''
    return (size - 1) * stride - 2 * padding + Filter

def conv(size, stride, padding, Filter):
    '''compute conv size: conv(size, stride, padding, Filter)'''
    return (size - Filter + 2 * padding)/stride + 1