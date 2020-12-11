from modelling.distribution_electric_field import DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration

d = DistributionElectricField()
d.calc()

dt = DistributionTempInVolume()
dt.calc()


timegen = TimeGeneration(massiv_temp=dt.massiv_temp,
                         massiv_potential=d.massiv_potential)

print(timegen.get_min_value())