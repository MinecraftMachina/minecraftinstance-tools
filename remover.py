import json
from pathlib import Path

from structs import *

minecraft_instance: MinecraftInstance
minecraft_instance_json: dict
removed_addons: List[InstalledAddon] = []

mc_instance_file = Path("minecraftinstance.json")
mc_instance_file_bak = mc_instance_file.with_suffix(mc_instance_file.suffix + ".bak")

with mc_instance_file.open() as f:
    minecraft_instance_json = json.load(f)
    minecraft_instance = minecraft_instance_from_dict(minecraft_instance_json)


def remove_addon(addon: InstalledAddon):
    minecraft_instance.installed_addons.remove(addon)
    addon_json = next(a for a in minecraft_instance_json["installedAddons"] if
                      addon.installed_file.file_name == a["installedFile"]["fileName"])
    minecraft_instance_json["installedAddons"].remove(addon_json)
    removed_addons.append(addon)


class IdNotFoundException(Exception):
    pass


def get_addon_with_id(id: int) -> InstalledAddon:
    try:
        return next(a for a in minecraft_instance.installed_addons if a.addon_id == id)
    except StopIteration:
        raise IdNotFoundException()


def get_addon_references(addon: InstalledAddon):
    for a in minecraft_instance.installed_addons:
        if a == addon:
            continue
        for f in a.installed_file.dependencies:
            # skip dependencies that are not actual dependencies
            if f.type != 3:
                continue
            f_addon = get_addon_with_id(f.addon_id)
            if addon == f_addon:
                yield a


def remove_addon_with_deps(addon: InstalledAddon):
    referenced = False
    for a in get_addon_references(addon):
        print(f"Addon referenced by {a.installed_file.file_name}")
        referenced = True
    if referenced:
        return

    remove_addon(addon)

    for dep_file in addon.installed_file.dependencies:
        dep_addon = get_addon_with_id(dep_file.addon_id)
        try:
            next(get_addon_references(dep_addon))
        except StopIteration:
            remove_addon_with_deps(dep_addon)


def search_addons(query: str):
    filtered_addons = minecraft_instance.installed_addons
    if query != "":
        filtered_addons = [addon for addon in filtered_addons if
                           query.lower() in addon.installed_file.file_name.lower()]
    i = 0
    print("\nSearch results:")
    for addon in filtered_addons:
        print(f"{i:02}. {addon.installed_file.file_name}")
        i += 1
    print("\nEnter choice number, new search, or leave empty to stop:")
    choice = input("> ")
    if choice.isdigit():
        remove_addon_with_deps(filtered_addons[int(choice)])
        return True
    elif choice == "":
        return False
    else:
        return search_addons(choice)


if __name__ == '__main__':
    while True:
        if not search_addons(""):
            break

    print("\nRemoval results:")
    for addon in removed_addons:
        print(f"Removed {addon.installed_file.file_name}")

    print("\nWould you like to save the changes? (y/N)")
    if input("> ").lower() == "y":
        while mc_instance_file_bak.exists():
            mc_instance_file_bak = mc_instance_file_bak.with_suffix(mc_instance_file_bak.suffix + ".bak")
        mc_instance_file.rename(mc_instance_file_bak)

        with mc_instance_file.open("w", newline='\n') as f:
            json.dump(minecraft_instance_json, f, sort_keys=False, indent=2)
            print(f"Saved to: {f.name}")
    else:
        print("Nothing changed")
