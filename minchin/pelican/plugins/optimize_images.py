# -*- coding: utf-8 -*-

"""
Optimized images (jpg and png)
Assumes that jpegtran and optipng are installed on path.
http://jpegclub.org/jpegtran/
http://optipng.sourceforge.net/
Copyright (c) 2012 Irfan Ahmad (http://i.com.pk)
Copyright (c) 2017, 2022 Wm. Minchin
"""

import logging
import os
from subprocess import call

from pelican import signals

logger = logging.getLogger(__name__)

# Display command output on DEBUG and TRACE
SHOW_OUTPUT = logger.getEffectiveLevel() <= logging.DEBUG

# A list of file types with their respective commands
COMMANDS = {
    # '.ext': ('command {flags} {filename', 'silent_flag', 'verbose_flag')
    ".jpg": (
        'jpegtran {flags} -copy none -optimize -outfile "{filename}" "{filename}"',
        "",
        "-v",
    ),
    ".png": ('optipng {flags} "{filename}"', "--quiet", ""),
}


# Module Metadata
__title__ = "minchin.pelican.plugins.optimize_images"
__version__ = "1.2.1-dev"
__description__ = "This Pelican plugin optimizes images (jpg and png)."
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__url__ = "https://github.com/MinchinWeb/minchin.pelican.plugins.optimize_images"
__license__ = "GNU Affero General Public License v3"


LOG_PREFIX = "[Optimize Images]"


def optimize_images(pelican):
    """
    Optimized jpg and png images

    :param pelican: The Pelican instance
    """
    if dev_mode_active(pelican):
        pass
    else:
        for dirpath, _, filenames in os.walk(pelican.settings["OUTPUT_PATH"]):
            for name in filenames:
                if os.path.splitext(name)[1] in COMMANDS.keys():
                    optimize(dirpath, name)


def optimize(dirpath, filename):
    """
    Check if the name is a type of file that should be optimized.
    And optimizes it if required.

    :param dirpath: Path of the file to be optimized
    :param name: A file name to be optimized
    """
    filepath = os.path.join(dirpath, filename)
    logger.info("%s optimizing %s", LOG_PREFIX, filepath)

    ext = os.path.splitext(filename)[1]
    command, silent, verbose = COMMANDS[ext]
    flags = verbose if SHOW_OUTPUT else silent
    command = command.format(filename=filepath, flags=flags)
    call(command, shell=True)


def dev_mode_active(pelican):
    """
    Check if Development Mode is active.

    In this mode, no images are actually optimized. Useful for speeding up
    interations when working on your blog locally.
    """
    if (
        "OPTIMIZE_IMAGES_DEV_MODE" in pelican.settings.keys()
        and pelican.settings["OPTIMIZE_IMAGES_DEV_MODE"]
    ):
        logger.warning(
            "%s Development Mode is active. Optimize Images plugin has been disabled.",
            LOG_PREFIX,
        )
        return True
    else:
        pelican.settings["OPTIMIZE_IMAGES_DEV_MODE"] = False
        return False


# def check_settings(pelican):
#     pass


def register():
    signals.finalized.connect(optimize_images)
    # signals.initialized.connect(check_settings)
