import os.path
import json
import xml.etree.ElementTree as ET

src_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(src_dir, "..", "data")
aircraft_file = os.path.join(data_dir, "aircraft.json")
liveries_file = os.path.join(data_dir, "liveries.json")
output_file = os.path.join(src_dir, "..", "simple_traffic.vmr")


def merge_airlines(model_liveries):
    liveries_by_airline = {}
    for livery in model_liveries:
        icao_airline = livery["icao_airline"]
        model_name = livery["title"]
        if icao_airline in liveries_by_airline:
            liveries_by_airline[icao_airline] = (
                liveries_by_airline[icao_airline] + "//" + model_name
            )
        else:
            liveries_by_airline[icao_airline] = model_name

    merged_liveries = []
    for key, value in liveries_by_airline.items():
        merged_liveries.append({"icao_airline": key, "title": value})

    return merged_liveries


def generate_rules():
    with open(aircraft_file) as af, open(liveries_file) as lf:
        aircraft = json.load(af)
        liveries = json.load(lf)
    rules = []
    for model, model_info in aircraft.items():
        for wtc_code, ac_types in model_info.items():
            for type_code in ac_types:
                model_liveries = merge_airlines(liveries[model][wtc_code])
                for livery in model_liveries:
                    callsign_prefix = livery["icao_airline"]
                    model_name = livery["title"]
                    rules.append((callsign_prefix, type_code, model_name))
    return rules


def write_rules(rules):
    rule_set = ET.Element("ModelMatchRuleSet")

    for callsign_prefix, type_code, model_name in rules:
        rule = ET.Element("ModelMatchRule")
        if callsign_prefix:
            rule.set("CallsignPrefix", callsign_prefix)
        rule.set("TypeCode", type_code)
        rule.set("ModelName", model_name)
        rule_set.append(rule)

    ET.indent(rule_set)
    rule_set.tail = "\n"

    tree = ET.ElementTree(rule_set)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)


rules = generate_rules()
write_rules(rules)
