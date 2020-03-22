import json
import sys
from pathlib import Path

from structs import *

minecraft_instance: MinecraftInstance
minecraft_instance_json: dict
staged_addons: List[InstalledAddon] = []

mc_instance_file: Path
mc_instance_file_bak: Path


class IdNotFoundException(Exception):
    pass


def get_addon_with_id(id: int) -> InstalledAddon:
    try:
        return next(a for a in minecraft_instance.installed_addons if a.addon_id == id)
    except StopIteration:
        raise IdNotFoundException()


def get_addon_references(addon: InstalledAddon, ignored_addon: InstalledAddon = None):
    for a in minecraft_instance.installed_addons:
        if a == ignored_addon:
            continue
        for f in a.installed_file.dependencies:
            # skip dependencies that are not actual dependencies
            if f.type != 3:
                continue
            try:
                f_addon = get_addon_with_id(f.addon_id)
                if addon == f_addon:
                    yield a
            except IdNotFoundException:
                print(f"Addon with id {f.addon_id} referenced but not defined. Blame Twitch!")


def remove_addon(addon: InstalledAddon):
    minecraft_instance.installed_addons.remove(addon)
    addon_json = next(a for a in minecraft_instance_json["installedAddons"] if
                      addon.installed_file.file_name == a["installedFile"]["fileName"])
    minecraft_instance_json["installedAddons"].remove(addon_json)


def stage_addon_with_deps(addon: InstalledAddon):
    referenced = False
    for a in get_addon_references(addon):
        print(f"Addon referenced by {a.installed_file.file_name}")
        input("Press enter to continue...")
        referenced = True
    if referenced:
        return

    staged_addons.append(addon)

    for dep_file in addon.installed_file.dependencies:
        try:
            dep_addon = get_addon_with_id(dep_file.addon_id)
            try:
                next(get_addon_references(dep_addon, addon))
            except StopIteration:
                staged_addons.append(dep_addon)
        except IdNotFoundException:
            print(f"Addon with id {dep_file.addon_id} referenced but not defined. Blame Twitch!")


def choose_addons(query: str):
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
        stage_addon_with_deps(filtered_addons[int(choice)])
        return True
    elif choice == "":
        return False
    else:
        return choose_addons(choice)


def ask_unstage_addons():
    i = 0
    print("\nStaged for removal:")
    for addon in staged_addons:
        print(f"{i:02}. {addon.installed_file.file_name}")
        i += 1
    print("\nEnter choice number to discard, or leave empty to stop:")
    choice = input("> ")
    if choice.isdigit():
        remove_addon(staged_addons.pop(int(choice)))
        return True
    elif choice == "":
        return False
    else:
        return ask_unstage_addons()


def load_file():
    global mc_instance_file, mc_instance_file_bak, f, minecraft_instance_json, minecraft_instance

    mc_instance_file = Path(sys.argv[1])
    mc_instance_file_bak = mc_instance_file.with_suffix(mc_instance_file.suffix + ".bak")

    with mc_instance_file.open() as f:
        minecraft_instance_json = json.load(f)
        minecraft_instance = minecraft_instance_from_dict(minecraft_instance_json)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage of this script:")
        print("  remover.py /path/to/minecraftinstance.json")
        exit(1)

    load_file()

    while True:
        if not choose_addons(""):
            break

    while len(staged_addons) > 0:
        if not ask_unstage_addons():
            break

    if len(staged_addons) < 1:
        print("Nothing changed")
        exit(0)

    print("\nRemoved:")
    for addon in staged_addons:
        print(f"Removed {addon.installed_file.file_name}")

    print("\nWould you like to save the changes? (y/N)")
    if input("> ").lower() != "y":
        print("Nothing changed")
        exit(0)

    while mc_instance_file_bak.exists():
        mc_instance_file_bak = mc_instance_file_bak.with_suffix(mc_instance_file_bak.suffix + ".bak")
    mc_instance_file.rename(mc_instance_file_bak)

    with mc_instance_file.open("w", newline='\n') as f:
        json.dump(minecraft_instance_json, f, sort_keys=False, indent=2)
        print(f"Saved to: {f.name}")
