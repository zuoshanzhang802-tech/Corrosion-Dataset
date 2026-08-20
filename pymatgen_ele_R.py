import warnings

from pymatgen.core import Element
import pandas as pd
# 忽略电负性警告
warnings.filterwarnings("ignore", category=UserWarning)


from pymatgen.core import Element

# 获取所有元素的实例
elements = [Element(el) for el in Element]

# 获取第一个元素的所有属性
first_el = elements[0]
all_attributes = [attr for attr in dir(first_el) if not attr.startswith('__')]

# 打印所有属性

name_list = []
for attr in all_attributes:
    name_list.append(attr)

import pandas as pd
import numpy as np
from pymatgen.core import Element
import warnings

# 忽略电负性警告
warnings.filterwarnings("ignore", category=UserWarning)

# 获取所有元素的属性
elements = [str(el.symbol) for el in Element]
print(len(elements))



properties = [
    'name', 'X', 'Z', 'atomic_mass', 'atomic_radius',
    'average_cationic_radius',
    'electron_affinity', 'group', 'ionization_energy',
    'is_actinoid', 'is_alkali', 'is_alkaline', 'is_chalcogen', 'is_halogen', 'is_lanthanoid', 'is_metal', 'is_metalloid', 'is_noble_gas',
    'is_post_transition_metal', 'is_quadrupolar', 'is_radioactive', 'is_rare_earth', 'is_transition_metal', 'max_oxidation_state',
    'min_oxidation_state', 'row', "mendeleev_no",
            "electrical_resistivity",
    "molar_volume",
    "thermal_conductivity",
    "boiling_point",
    "melting_point",
            "liquid_range",
            "density_of_solid",
            "atomic_radius_calculated"
        ]# 删除了'valence', 因为Cr有不确定的'valence'
print('列表长度等于', len(properties))
values = []
# 遍历元素列表
for element_symbol in elements:
    # 创建元素的实例
    element = Element(element_symbol)
    # 遍历属性列表并打印每个属性的值
    for attr in properties:
        # 使用 getattr 函数安全地获取属性值
        value = getattr(element, attr, None)
        values.append(value)
print(len(values))
values_np = np.array(values, dtype=object)
values_np_reshape = values_np.reshape(118, -1)
print(values_np_reshape.shape)

# 将属性数据转换为DataFrame
df_properties = pd.DataFrame(values_np_reshape, columns=properties)
print(df_properties)
df_properties.to_excel('df_properties.xlsx', index=False)
#X-鲍林电负性
#atomic_radius-原子半径
#block-区，不是数字
#atomic_mass
#group-族
#electron_affinity-电子亲合能







'''
['A', 'X', 'Z', 'atomic_mass', 'atomic_orbitals_eV', 'atomic_radius', 
'average_anionic_radius', 'average_cationic_radius', 'average_ionic_radius', 'block', 'common_oxidation_states', 
'data', 'electron_affinity', 'electronic_structure', 
'full_electronic_structure', 'ground_state_term_symbol', 'group', 'icsd_oxidation_states', 'ionic_radii', 'ionization_energy', 
'is_actinoid', 'is_alkali', 'is_alkaline', 'is_chalcogen', 'is_halogen', 'is_lanthanoid', 'is_metal', 'is_metalloid', 'is_noble_gas', 
'is_post_transition_metal', 'is_quadrupolar', 'is_radioactive', 'is_rare_earth', 'is_transition_metal', 'is_valid_symbol', 'iupac_ordering', 
'long_name', 'max_oxidation_state', 'min_oxidation_state', 'n_electrons', 'name', 'nmr_quadrupole_moment', 'number', 'oxidation_states', 
'print_periodic_table', 'row', 'symbol', 'term_symbols', 'valence', 'value',
            "mendeleev_no",
            "electrical_resistivity",
            "velocity_of_sound",
            "reflectivity",
            "refractive_index",
            "poissons_ratio",
            "molar_volume",
            "thermal_conductivity",
            "boiling_point",
            "melting_point",
            "critical_temperature",
            "superconduction_temperature",
            "liquid_range",
            "bulk_modulus",
            "youngs_modulus",
            "brinell_hardness",
            "rigidity_modulus",
            "mineral_hardness",
            "vickers_hardness",
            "density_of_solid",
            "atomic_radius_calculated",
            "van_der_waals_radius",
            "atomic_orbitals",
            "coefficient_of_linear_thermal_expansion",
            "ground_state_term_symbol",
            "valence",
            "ground_level",
            "ionization_energies",
            "metallic_radius",
        ]
'''

al = Element('Al')
print(al.atomic_mass)