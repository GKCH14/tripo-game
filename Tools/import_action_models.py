import unreal

ASSETS = [
    (r"C:\Users\takum\Downloads\anime+girl+statue+3d+model\tripo_convert_45b1325e-b840-4d8d-badc-b909798f735f.obj", "/Game/Action/Player"),
    (r"C:\Users\takum\Downloads\anime+girl+statue+3d+model\anime_girl_statue_3d_model_basecolor.JPEG", "/Game/Action/Player"),
    (r"C:\Users\takum\Downloads\fantasy+knight+3d+model\tripo_convert_33744a7c-3e31-4e99-8cea-eac33d1e4f96.obj", "/Game/Action/Enemy"),
    (r"C:\Users\takum\Downloads\fantasy+knight+3d+model\fantasy_knight_3d_model_basecolor.JPEG", "/Game/Action/Enemy"),
]

tools = unreal.AssetToolsHelpers.get_asset_tools()
tasks = []
for filename, destination in ASSETS:
    task = unreal.AssetImportTask()
    task.filename = filename
    task.destination_path = destination
    task.automated = True
    task.replace_existing = True
    task.save = True
    tasks.append(task)

tools.import_asset_tasks(tasks)
for task in tasks:
    unreal.log("Imported: {}".format(task.imported_object_paths))
unreal.EditorAssetLibrary.save_directory("/Game/Action", only_if_is_dirty=False, recursive=True)
