from willow.optimizers.optimizer_base import OptimizerBase


class Gifsicle(OptimizerBase):
    binary = 'gifsicle'
    args = [
       '-b', # required parameter
        '-O3' # slowest, but produces best results
    ]

    def applies_to(self, image):
        return super().applies_to(image, mimetype='image/gif')


willow_optimizer_classes = [Gifsicle]
