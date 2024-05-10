# Fast SQV for Klipper

:warning: Use at your own risk :warning:

This is a set of postprocessing script for only OrcaSlicer to accelerate the gyroid infill speed using the [Klipper](https://www.klipper3d.org/)'s Square Corner Velocity (SQV) feature.

The post-processing script will read the .gcode file to put the necessary macro command to modify the value of SQV for infills and perimeters keeping everything else as the default SQV value that the user has set in the `printer.cfg`. Since that the infills and internal perimeters do not affect the quality of the print, thus the reason why I would want to add the features of adjusting each SQV value for different feature of type to print faster. However, increasing the SQV value too high will remove details on the surface and rounded the corner of the print.

# How to use

## Klipper setup (credit to RomRider)

This is mandatory, whatever the slicer you use:

1. Add the `save_variable` section to your `printer.cfg` if you don't already have it. For eg.:
    ```ini
    [save_variables]
    filename: ~/klipper_config/saved_variables.cfg
    ```
2. Copy the content of [`fast_infill.cfg`](klipper/fast_infill.cfg) into your `printer.cfg`.
3. Once you have added the configuration to your klipper configuration, restart Klipper.
4. When the machine is back online, run the command `SET_INFILL_SQV SQV=<VALUE>`. This will define the SQV value you want to use during the infill. I suggest a value of `20` if your printer is capable of going very fast (eg. Voron, RatRig VCore-3, ...).

Extra Step: 
* Run other command `SET_INTERNAL_PERIMETER_SQV SQV=<VALUE>` and other commands to define the SQV value you want to use.

You can update the SQV value for infill while it's printing by using the same command above. It will be applied during the next infill run. If you don't want to modify the infill SQV, just set the value to the same value as your default SQV.

NOTE:
* :warning: Ensure that the printer is perfectly tuned to handle high printing speed otherwise layer shift and other artifacts may occur during the printing process.
* The `fast_infill.cfg` files can be copied to the same folder as your `printer.cfg` and just add these sections there:
    ```ini
    [include ./fast_infill.cfg]
    ```


## OrcaSlicer

1. Copy the `fast_infill.py` from the repository's folder in a folder on your computer where OrcaSlicer runs. Put it in a folder without any space.
1. Install Python (if you are using Windows, don't install python from the Microsoft Store, it won't work)
1. Reference the post processing script into your superslicer configuration. Eg. for Windows:
    ![superslicer_config](docs/orcaslicer_config.PNG)
1. Run your slicing as usual and export or upload the file to your printer. If everything works as ecpected, you'll see a black terminal window poping up (that is the script running).

# How to validates that it works well

If you open the gcode file after postprocessing, you should find references to `_USE_INFILL_SQV`, `_USE_NORMAL_SQV`, and other macro commands.

# Credits
Thanks to RomRider who make the klipper-FastGyroidInfill post-processing script which this script is heavily based on. All of the original code is thanks to this guy's work and dedication, and I added several more lines to the script.
