from dino_runner.utils.constants import ICE, ICE_TYPE, ICE_SOUND
from dino_runner.components.power_ups.power_up import PowerUp


class Ice(PowerUp):

    def __init__(self):
        self.image = ICE
        self.type = ICE_TYPE
        self.sound = ICE_SOUND
        super().__init__(self.image, self.type)
        