import ast
import pprint
with open("fleet_data.txt", "r") as file:
    content = ast.literal_eval(file.read())
def total_fuel_consumed(truck: dict):
    fuel = truck['logs'][0]['fuel_level'] - truck['logs'][-1]['fuel_level']
    return fuel
def total_distance(truck: dict):
    distance = 0
    for i in range(0, len(truck['logs'])):
        distance += truck['logs'][i]['dist_covered']
    return distance
def efficiency_score(truck: dict):
    planned_consumption = (truck['plan']['dist_km'] * truck['plan']['consumption_rate']) / 100
    actual_consumption = truck['logs'][0]['fuel_level'] - truck['logs'][-1]['fuel_level']
    score = actual_consumption / planned_consumption
    return score
def report_dict(report: dict, fleet: list):
    efficiency_sum = 0
    count = len(fleet)
    for i in range(0, len(fleet)):
        info = {}
        efficiency_sum += efficiency_score(fleet[i])
        fuel = total_fuel_consumed(fleet[i])
        distance = total_distance(fleet[i])
        efficiency = efficiency_score(fleet[i])
        info.update({"total_dist": distance, "total_fuel": fuel, "efficiency": efficiency})
        report[fleet[i]['id']] = info
    report['fleet_avg_efficiency'] = efficiency_sum / count
    return report
def fuel_theft(trucks: list, fuel_level_threshold: int):
    thefts_report = []
    for i in range(0, len(trucks)):
        thefts = []
        for j in range(0, len(trucks[i]['logs']) - 1):
            consumed_fuel = trucks[i]['logs'][j]['fuel_level'] - trucks[i]['logs'][j+1]['fuel_level']
            if consumed_fuel > fuel_level_threshold:
                if trucks[i]['logs'][j+1]['dist_covered'] < 20:
                    thefts.append({"hour": j, "consumed_fuel": consumed_fuel})
        if(len(thefts) > 0):
            thefts_report.append({"id": trucks[i]['id'], "info": thefts})
    return thefts_report
def route_deviation(trucks: list, kilometer_threshold: int):
    deviations_report = []
    for i in range(0, len(trucks)):
        deviations = []
        for j in range(0, len(trucks[i]['logs']) - 3):
            if trucks[i]['logs'][j]['gps_deviation'] > kilometer_threshold and trucks[i]['logs'][j+1]['gps_deviation'] > kilometer_threshold and trucks[i]['logs'][j+2]['gps_deviation'] > kilometer_threshold:
                average_deviation = (trucks[i]['logs'][j]['gps_deviation'] + trucks[i]['logs'][j+1]['gps_deviation'] + trucks[i]['logs'][j+2]['gps_deviation']) / 3
                deviations.append({"hours": [j, j+1, j+2], "average_deviation": average_deviation})
        if(len(deviations) > 0):
            deviations_report.append({"id": trucks[i]["id"], "info": deviations})
    return deviations_report
report = {}
pprint.pprint(report_dict(report, content), indent = 4, width = 20)
fuel_level_threshold = int(input("Enter the fuel level threshold: "))
kilometer_threshold = int(input("Enter the kilometer threshold: "))
fuel_theft_suspects = fuel_theft(content, fuel_level_threshold)
route_deviation_suspects = route_deviation(content, kilometer_threshold)
pprint.pprint(fuel_theft_suspects, indent = 4, width = 20)
pprint.pprint(route_deviation_suspects, indent = 4, width = 20)