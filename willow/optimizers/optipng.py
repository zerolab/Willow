from willow.optimizers.optimizer_base import OptimizerBase


class Optipng(OptimizerBase):
    binary = 'optipng'
    args = [
        '-i0',     # results in a non-interlaced, progressive scanned image
        '-o2',     # sets the optimization level to two (multiple IDAT compression trials)
        '-quiet',  # required parameter for the package
    ]

    def applies_to(self, image, **kwargs):
        return super().applies_to(image, mimetype='image/png')


willow_optimizer_classes = [Optipng]
