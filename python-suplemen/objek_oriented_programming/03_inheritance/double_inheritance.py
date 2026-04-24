class PropulsionSystem:
    def set_propulsion(self, thruster_count, max_speed):
        self.thruster_count = thruster_count
        self.max_speed = max_speed

    def propulsion_info(self):
        return f"Thruster: {self.thruster_count}, Max Speed: {self.max_speed} knots"

class SubmarineHull:
    def set_hull(self, material, max_depth):
        self.hull_material = material
        self.max_depth = max_depth

    def hull_info(self):
        return f"Hull: {self.hull_material}, Max Depth: {self.max_depth} m"


class SensorSystem:
    def set_sensors(self, sonar=True, camera=True):
        self.sonar = sonar
        self.camera = camera

    def sensor_info(self):
        return f"Sensors : {self.sonar}, Camera: {self.camera}"

class Amarine:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def identity(self):
        return f"AUV ID: {self.id}, Name: {self.name}"

class AUV(Amarine, PropulsionSystem, SubmarineHull, SensorSystem):
    def __init__(self, id, name):
        super().__init__(id, name)


auv = AUV(101, "Deepseek-chatgpt-01")
auv.set_propulsion(4, 10)
auv.set_propulsion(thruster_count=4, max_speed=6)
auv.set_hull(material="Titanium", max_depth=3000)
auv.set_sensors(sonar=True, camera=True)

auv = AUV(101, "AUV-DeepSea")

auv.set_propulsion(thruster_count=4, max_speed=6)
auv.set_hull(material="Titanium", max_depth=3000)
auv.set_sensors(sonar=True, camera=True)

print(auv.identity())
print(auv.propulsion_info())
print(auv.hull_info())
print(auv.sensor_info())
