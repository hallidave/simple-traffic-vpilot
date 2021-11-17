# Model Matching Rules for Aerosoft Simple Traffic

If you want to use the liveries for Aerosoft's Simple Traffic product with VATSIM, just download the `simple_traffic.vmr` file, put it in a safe place, and then add the file as a Custom Rule Set in vPilot.

In vPilot, go to **Settings->Model Matching->Custom Rules->Add Custom Rule Set(s)...** and then select the `simple_traffic.vmr` file that you downloaded.

## Generating a New Model Matching File

There are two Python scripts in the `src` directory: one for scanning the Aerosoft Simple Traffic mod directory for liveries and the other for generating the `.vmr` file based on the list of the supported aircraft in `data/aircraft.json` and the scanning output in `data\liveries.json`.

The initial list of aircraft is pretty basic. Feel free to suggest new aircraft as an Issue or a Pull Request to the `data/aircraft.json` file.
