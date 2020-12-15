from modelling.distribution_electric_field import DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_vacancies import DrawVacancies

d = DistributionElectricField()
dt = DistributionTempInVolume()
timegen = TimeGeneration()
draw_vac = DrawVacancies()

for a in range(0,30):
    d.calc()

    dt.calc()

    timegen.calc(massiv_temp=dt.massiv_temp, massiv_potential=d.massiv_potential)
    coord_o_vac = timegen.get_min_value()

    d.massive_for_check_vacancies = timegen.massive_for_check_vacancies
    dt.massive_for_check_vacancies = timegen.massive_for_check_vacancies

    draw_vac.add_vacancies(coord_o_vac)
draw_vac.draw()