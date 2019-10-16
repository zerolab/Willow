from willow.optimizers.optimizer_base import OptimizerBase


class Jpegoptim(OptimizerBase):
    # TODO: take in consideration the quality/progressive args passed to save_as_jpeg
    binary = "jpegoptim"
    args = [
        '-m85',               # set maximum quality to 85%
        '--strip-all',        # strip out all text information like comments and EXIF data
        '--all-progressive',  # make the resulting image progressive
    ]

    def applies_to(self, image, **kwargs):
        return super().applies_to(image, mimetype='image/jpeg')


willow_optimizer_classes = [Jpegoptim]
