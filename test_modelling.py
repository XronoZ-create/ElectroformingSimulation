from modelling.distribution_electric_field import DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration

d = DistributionElectricField()
dt = DistributionTempInVolume()
timegen = TimeGeneration()

for a in range(0,10):
    d.calc()

    dt.calc()

    timegen.calc(massiv_temp=dt.massiv_temp, massiv_potential=d.massiv_potential)
    timegen.get_min_value()

    d.massive_for_check_vacancies = timegen.massive_for_check_vacancies
    dt.massive_for_check_vacancies = timegen.massive_for_check_vacancies
