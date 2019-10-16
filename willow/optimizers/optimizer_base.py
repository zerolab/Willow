import subprocess

from mimetypes import guess_type


class OptimizerBase:
    # TODO allow passing a dict with binary/args for custom initialization/settings
    binary = ''
    args = []

    class Meta:
        abstract = True

    def applies_to(self, image, **kwargs):
        mime = guess_type(image.filename)
        return mime == kwargs.get('mimetype')

    @classmethod
    def check_binary(cls):
        args = [cls.binary] + cls.args
        try:
            return subprocess.check_output(args, stderr=subprocess.STDOUT)
        except (FileNotFoundError, subprocess.CalledProcessError):
            return False

    def process(self, image):
        args = [self.binary] + self.args + [image.name, image.filename]

        try:
            subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            pass

