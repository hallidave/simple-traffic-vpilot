import os
import configparser
import json

start_dir = "D:\\Aerosoft One Library\\Add-ons\\msfs-f52a-AS15423\\gameDirectory~Community"

src_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(src_dir, "..", "data")
liveries_file = os.path.join(data_dir, "liveries.json")

def parse_liveries(liveries, config):
    if "GENERAL" in config:
        general = config["GENERAL"]
        icao_generic = general.getboolean("icao_generic")
        if icao_generic:
            icao_model = general.get("icao_model").strip('"').lower()
            icao_WTC = general.get("icao_WTC").strip('"').upper()
            models = []
            for section_name in config.sections():
                if section_name.startswith("FLTSIM."):
                    section = config[section_name]
                    title = section.get("title").strip('"')
                    icao_airline = section.get("icao_airline").strip('"')
                    models.append({"title": title, "icao_airline": icao_airline})
            if models:
                liveries.setdefault(icao_model, {})
                liveries[icao_model].setdefault(icao_WTC, []).extend(models)
    return liveries
            

def scan(start_dir):
    liveries = {}
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file == "aircraft.cfg":
                config = configparser.ConfigParser(inline_comment_prefixes=(";"))
                config.read(root + os.sep + file)
                liveries = parse_liveries(liveries, config)
                if liveries:
                    with open(liveries_file, "w") as f:
                        json.dump(liveries, f, sort_keys=True, indent=2)

scan(start_dir)
