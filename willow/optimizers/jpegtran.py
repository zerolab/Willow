from willow.optimizers.optimizer_base import OptimizerBase


class Jpegtran(OptimizerBase):
    # TODO: take in consideration the quality/progressive args passed to save_as_jpeg
    binary = "jpegtran"
    args = [
        '-copy none',   # do not copy any markers from source
        '-optimize',    # slower, but smaller size
        '-perfect',     # fails when there are non-transformable edge blocks
        '-progressive'  # make the resulting image progressive
    ]

    def applies_to(self, image):
        return super().applies_to(image, mimetype='image/jpeg')


willow_optimizer_classes = [Jpegtran]
