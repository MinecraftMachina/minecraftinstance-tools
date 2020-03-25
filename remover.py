import json
import sys
from pathlib import Path

from structs import *


class Remover(object):
    minecraft_instance: MinecraftInstance
    minecraft_instance_json: dict
    staged_addons: List[InstalledAddon] = []

    mc_instance_file: Path
    mc_instance_file_bak: Path

    class IdNotFoundException(Exception):
        pass

    def get_addon_with_id(self, id: int) -> InstalledAddon:
        try:
            return next(a for a in self.minecraft_instance.installed_addons if a.addon_id == id)
        except StopIteration:
            raise Remover.IdNotFoundException()

    def get_addon_references(self, addon: InstalledAddon, ignored_addon: InstalledAddon = None):
        for a in self.minecraft_instance.installed_addons:
            if a == ignored_addon:
                continue
            for f in a.installed_file.dependencies:
                # skip dependencies that are not actual dependencies
                if f.type != 3:
                    continue
                try:
                    f_addon = self.get_addon_with_id(f.addon_id)
                    if addon == f_addon:
                        yield a
                except Remover.IdNotFoundException:
                    print(f"Addon with id {f.addon_id} referenced but not defined. Blame Twitch!")

    def remove_addon(self, addon: InstalledAddon):
        self.minecraft_instance.installed_addons.remove(addon)
        addon_json = next(a for a in self.minecraft_instance_json["installedAddons"] if
                          addon.installed_file.file_name == a["installedFile"]["fileName"])
        self.minecraft_instance_json["installedAddons"].remove(addon_json)

    def stage_addon_with_deps(self, addon: InstalledAddon):
        referenced = False
        for a in self.get_addon_references(addon):
            print(f"Addon referenced by {a.installed_file.file_name}")
            referenced = True
        print("Remove those dependencies first")
        input("Press enter to continue...")
        if referenced:
            return

        self.staged_addons.append(addon)

        for dep_file in addon.installed_file.dependencies:
            try:
                dep_addon = self.get_addon_with_id(dep_file.addon_id)
                try:
                    next(self.get_addon_references(dep_addon, addon))
                except StopIteration:
                    self.staged_addons.append(dep_addon)
            except Remover.IdNotFoundException:
                print(f"Addon with id {dep_file.addon_id} referenced but not defined. Blame Twitch!")

    def choose_addons(self, query: str):
        filtered_addons = self.minecraft_instance.installed_addons
        if query != "":
            filtered_addons = [addon for addon in filtered_addons if
                               query.lower() in addon.installed_file.file_name.lower()]
        i = 0
        print("\nSearch results:")
        for addon in filtered_addons:
            print(f"{i:>3}. {addon.installed_file.file_name}")
            i += 1
        print("\nEnter choice number, new search, or leave empty to stop:")
        choice = input("> ")
        if choice.isdigit():
            self.stage_addon_with_deps(filtered_addons[int(choice)])
            return True
        elif choice == "":
            return False
        else:
            return self.choose_addons(choice)

    def ask_unstage_addons(self):
        i = 0
        print("\nStaged for removal:")
        for addon in self.staged_addons:
            print(f"{i:>3}. {addon.installed_file.file_name}")
            i += 1
        print("\nEnter choice number to discard, or leave empty to finish:")
        choice = input("> ")
        if choice.isdigit():
            self.remove_addon(self.staged_addons.pop(int(choice)))
            return True
        elif choice == "":
            return False
        else:
            return self.ask_unstage_addons()

    def load_file(self):
        self.mc_instance_file = Path(sys.argv[1])
        self.mc_instance_file_bak = self.mc_instance_file.with_suffix(self.mc_instance_file.suffix + ".bak")

        with self.mc_instance_file.open() as f:
            self.minecraft_instance_json = json.load(f)
            self.minecraft_instance = minecraft_instance_from_dict(self.minecraft_instance_json)

    def go(self):
        self.load_file()

        while True:
            if not self.choose_addons(""):
                break

        while len(self.staged_addons) > 0:
            if not self.ask_unstage_addons():
                break

        if len(self.staged_addons) < 1:
            print("Nothing changed")
            exit(0)

        print("\nRemoved addons:")
        for addon in self.staged_addons:
            self.remove_addon(addon)
            print(f"Removed {addon.installed_file.file_name}")

        print("\nWould you like to save the changes? (y/N)")
        if input("> ").lower() != "y":
            print("Nothing changed")
            exit(0)

        while self.mc_instance_file_bak.exists():
            self.mc_instance_file_bak = self.mc_instance_file_bak.with_suffix(self.mc_instance_file_bak.suffix + ".bak")
        self.mc_instance_file.rename(self.mc_instance_file_bak)

        with self.mc_instance_file.open("w", newline='\n') as f:
            json.dump(self.minecraft_instance_json, f, sort_keys=False, indent=2)
            print(f"Saved to: {f.name}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage of this script:")
        print("  remover.py /path/to/minecraftinstance.json")
        exit(1)

    remover = Remover()
    remover.go()
