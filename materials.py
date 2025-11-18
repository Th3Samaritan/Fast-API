from fastapi import FastAPI

app = FastAPI()

MATERIALS = [
    {'name': 'Aluminium', 'type_of_material': 'metal', 'type_of_metal': 'non_ferrous'},
    {'name': 'Steel', 'type_of_material': 'metal', 'type_of_metal': 'ferrous'},
    {'name': 'Iron', 'type_of_material': 'metal', 'type_of_metal': 'ferrous'},
    {'name': 'Magnesium', 'type_of_material': 'metal', 'type_of_metal': 'ferrous'},
    {'name': 'Gold', 'type_of_material': 'metal', 'type_of_metal': 'non-ferrous'},
    {'name': 'Silver', 'type_of_material': 'metal', 'type_of_metal': 'non-ferrous'}
]


@app.get("/materials")
async def read_all_materials():
    return MATERIALS

@app.get("/materials/{material_name}")
async def read_material(material_name: str):
    for material in MATERIALS:
        if material.get('name').casefold() == material_name.casefold():
            return material


@app.get("/materials/")
async def get_category_by_query(category_name: str):
    materials_to_return = []
    for material in MATERIALS:
        if material.get('name').casefold() == category_name.casefold():
            materials_to_return.append(material)
        return materials_to_return

@app.get("/materials/{material_type}")
async def get_material_by_type(material_type: str, type_of_metal: str):
    materials_to_return = []
    for material in MATERIALS:
        if material.get('type_of_material').casefold() == material_type.casefold() and \
        material.get('type_of_metal').casefold() == type_of_metal.casefold():
            materials_to_return.append(material)
    return materials_to_return
