from .mount_model import MountModel
from .mount_factory import mount_factory

from .rethink_mount import RethinkMount
from .rethink_minimal_mount import RethinkMinimalMount
from .aisono_mount import AisonoMount  # aisono_mount for ultrasound scanning(by JadeCong)
from .null_mount import NullMount


MOUNT_MAPPING = {
    "RethinkMount": RethinkMount,
    "RethinkMinimalMount": RethinkMinimalMount,
    "AisonoMount": AisonoMount,  # aisono_mount for ultrasound scanning(by JadeCong)
    None: NullMount,
}

ALL_MOUNTS = MOUNT_MAPPING.keys()
