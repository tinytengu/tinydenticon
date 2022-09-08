from .utils import scale_matrix_1d, hsl_to_rgb, sha512hash


class Identicon:
    def __init__(
        self,
        data: bytes,
        hash_rounds: int = 1,
        image_side: int = 500,
        saturation: float = 0.7,
        lightness: float = 0.5,
        background: tuple = (240, 240, 240),
    ):
        self.data = data
        self.hash_rounds = hash_rounds
        self.image_side = image_side
        self.saturation = saturation
        self.lightness = lightness
        self.background = background

    def hexdigest(self) -> str:
        """Hexdigest of passed data."""

        return sha512hash(self.data, self.hash_rounds).hexdigest()

    def get_matrix(self) -> list:
        """Binary matrix where 1 is foreground and 0 is background."""
        digest = self.hexdigest()

        half_matrix = [int(int(c, 16) % 2 == 0) for c in digest[:15]]
        matrix = []

        for i in range(5):
            matrix.extend(
                (
                    half_matrix[i + 10],
                    half_matrix[i + 5],
                    half_matrix[i],
                    half_matrix[i + 5],
                    half_matrix[i + 10],
                )
            )

        return scale_matrix_1d(matrix, matrix_size=5, multiplier=self.image_side // 5)

    def get_pixels(self) -> list:
        """Flattened pixel matrix with assigned foreground and background colors."""
        rgb = hsl_to_rgb(
            int(self.hexdigest()[-7:], 16) / 0xFFFFFFF, self.saturation, self.lightness
        )
        return [rgb if i == 1 else self.background for i in self.get_matrix()]
