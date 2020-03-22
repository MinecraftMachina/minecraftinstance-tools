import json
from pathlib import Path

import fuzzysearch

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


def get_addon_with_id(id: int) -> InstalledAddon:
    return next(a for a in minecraft_instance.installed_addons if a.addon_id == id)


def addon_referenced(addon: InstalledAddon) -> bool:
    try:
        res = any(a for a in minecraft_instance.installed_addons if
                  any(f for f in a.installed_file.dependencies if
                      addon == get_addon_with_id(f.addon_id)))
    except RuntimeError:
        res = False
    return res


def remove_addon_with_deps(addon: InstalledAddon):
    remove_addon(addon)
    for dep_file in addon.installed_file.dependencies:
        dep_addon = get_addon_with_id(dep_file.addon_id)
        if not addon_referenced(dep_addon):
            remove_addon_with_deps(dep_addon)


def search_addons(query: str):
    filtered_addons = minecraft_instance.installed_addons
    if query != "":
        filtered_addons = [addon for addon in filtered_addons if
                           len(fuzzysearch.find_near_matches(query, addon.installed_file.file_name, max_l_dist=1)) > 0]
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
