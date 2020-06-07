model_path = './latest_model.h5'

HIDDEN_CNN_LAYERS = [
    {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
]

REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
