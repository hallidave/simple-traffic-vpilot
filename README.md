# Model Matching Rules for Aerosoft Simple Traffic

This project generates a model matching file for vPilot that uses the liveries from [Aerosoft's Simple Traffic](https://www.aerosoft.com/en/microsoft-flight-simulator/msfs-tools/3537/aerosoft-tool-simple-traffic) product. The model matching file allows you to see the Aerosoft liveries when you are using live ATC on the VATSIM network with Microsoft Flight Simulator 2020.

To get the model matching file, download the latest version under **Releases**, unzip the files, and copy the `simple_traffic.vmr` file to a safe place. Then add the file as a Custom Rule Set in vPilot.

In vPilot, go to **Settings->Model Matching->Custom Rules->Add Custom Rule Set(s)...** and then select the `simple_traffic.vmr` file that you downloaded.

## Generating a New Model Matching File

There are two Python scripts in the `src` directory: one for scanning the Aerosoft Simple Traffic mod directory for liveries and the other for generating the `.vmr` file based on the list of the supported aircraft in `data/aircraft.json` and the scanning output in `data\liveries.json`.

The initial list of aircraft is pretty basic. Feel free to suggest new aircraft as an Issue or a Pull Request to the `data/aircraft.json` file.
