import unittest
import main
class TestFuelLogic(unittest.TestCase):
    def test_fuel_theft_detected(self):
        mock_data = [{
            "id": "TRUCK-TEST",
            "logs": [
                {"hour": 1, "fuel_level": 100, "dist_covered": 0},
                {"hour": 2, "fuel_level": 70, "dist_covered": 5}
            ]
        }]
        result = main.fuel_theft(mock_data, 10)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "TRUCK-TEST")
        self.assertEqual(result[0]["info"][0]["consumed_fuel"], 30)
        
    def test_no_theft_high_distance(self):
        mock_data = [{
            "id": "TRUCK-NORMAL",
            "logs": [
                {"hour": 1, "fuel_level": 100, "dist_covered": 0},
                {"hour": 2, "fuel_level": 70, "dist_covered": 50}
            ]
        }]
        result = main.fuel_theft(mock_data, 10)
        self.assertEqual(len(result), 0)
    
    def test_fuel_increase(self):
        mock_data = [{
            "id": "TRUCK-REFUEL",
            "logs": [
                {"hour": 1, "fuel_level": 50, "dist_covered": 0},
                {"hour": 2, "fuel_level": 150, "dist_covered": 0}
            ]
        }]
        result = main.fuel_theft(mock_data, 10)
        self.assertEqual(len(result), 0)
    
class TestDeviationLogic(unittest.TestCase):
    def no_deviation_case(self):
        mock_data = [{
            "id": "TRUCK-NORMAL",
            "logs": [
                {"hour": 1, "gps_deviation": 1},
                {"hour": 2, "gps_deviation": 1},
                {"hour": 3, "gps_deviation": 1},
                {"hour": 4, "gps_deviation": 0}
            ]
        }]
        result = main.route_deviation(mock_data, 10)
        self.assertEqual(len(result), 0)
    
    def deviation_case(self):
        mock_data = [{
            "id": "DEVIATED-TRUCK",
            "logs": [
                {"hour": 1, "gps_deviation": 100},
                {"hour": 2, "gps_deviation": 250},
                {"hour": 3, "gps_deviation": 150},
                {"hour": 4, "gps_deviation": 500}
            ]
        }]
        result = main.route_deviation(mock_data, 50)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "DEVIATED-TRUCK")
        self.assertAlmostEqual(result[0]["info"][0]["average_deviation"], 166.66, places = 1)

if __name__ == '__main__':
    unittest.main()
    
        