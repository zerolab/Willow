from willow.optimizers.optimizer_base import OptimizerBase


class Pngquant(OptimizerBase):
    binary = "pngquant"
    args = [
        '--force',   # required parameter for this package
        '--skip-if-larger'
    ]

    def applies_to(self, image):
        return super().applies_to(image, mimetype='image/png')


willow_optimizer_classes = [Pngquant]
