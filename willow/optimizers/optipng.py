from willow.optimizers.optimizer_base import OptimizerBase


class Optipng(OptimizerBase):
    binary = 'optipng'
    args = [
        '-i0',     # this will result in a non-interlaced, progressive scanned image
        '-o2',     # this set the optimization level to two (multiple IDAT compression trials)
        '-quiet',  # required parameter for this package
    ]

    def applies_to(self, image):
        return super().applies_to(image, mimetype='image/png')


willow_optimizer_classes = [Optipng]
