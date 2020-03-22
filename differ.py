import json
import sys
from pathlib import Path

from structs import *


class Differ(object):
    mc_instance_old: MinecraftInstance
    mc_instance_old_json: dict
    mc_instance_old_file: Path

    mc_instance_new: MinecraftInstance
    mc_instance_new_json: dict
    mc_instance_new_file: Path

    mc_instance_bak_file: Path

    def load_file(self):
        self.mc_instance_old_file = Path(sys.argv[1])
        self.mc_instance_new_file = Path(sys.argv[2])
        self.mc_instance_bak_file = self.mc_instance_old_file.with_suffix(self.mc_instance_old_file.suffix + ".bak")

        with self.mc_instance_old_file.open() as f:
            self.mc_instance_old_json = json.load(f)
            self.mc_instance_old = minecraft_instance_from_dict(self.mc_instance_old_json)
        with self.mc_instance_new_file.open() as f:
            self.mc_instance_new_json = json.load(f)
            self.mc_instance_new = minecraft_instance_from_dict(self.mc_instance_new_json)

    from dataclasses import dataclass

    @dataclass
    class AddonDiff:
        old_addon: Optional[InstalledAddon]
        new_addon: InstalledAddon

    def get_diff_addons(self) -> List[AddonDiff]:
        for addon_new in self.mc_instance_new.installed_addons:
            diff = self.get_diff_addon(addon_new)
            if diff is not None:
                yield diff

    def get_diff_addon(self, addon_new: InstalledAddon) -> Optional[AddonDiff]:
        for addon_old in self.mc_instance_old.installed_addons:
            if addon_old.addon_id == addon_new.addon_id:
                if addon_old.installed_file.id == addon_new.installed_file.id:
                    return None
                else:
                    return self.AddonDiff(addon_old, addon_new)
        return self.AddonDiff(None, addon_new)

    @staticmethod
    def get_addon_with_id_json(instance_json, id):
        return next(a for a in instance_json["installedAddons"] if a["addonID"] == id)

    def get_old_addon_with_id_json(self, id):
        return self.get_addon_with_id_json(self.mc_instance_old_json, id)

    def get_new_addon_with_id_json(self, id):
        return self.get_addon_with_id_json(self.mc_instance_new_json, id)

    def go(self):
        self.load_file()

        diff_addons = list(self.get_diff_addons())
        if len(diff_addons) < 1:
            print("Nothing changed")
            exit(0)

        print("\nDiff:")
        for diff in diff_addons:
            if diff.old_addon is None:
                print(diff.new_addon.installed_file.file_name)
            else:
                print(f"{diff.old_addon.installed_file.file_name} -> {diff.new_addon.installed_file.file_name}")

        print("\nWould you like to save the changes? (y/N)")
        if input("> ").lower() != "y":
            print("Nothing changed")
            exit(0)

        for diff in diff_addons:
            if diff.old_addon is not None:
                i = self.mc_instance_old_json["installedAddons"].index(
                    self.get_old_addon_with_id_json(diff.new_addon.addon_id))
            else:
                self.mc_instance_old_json["installedAddons"].append(None)
                i = len(self.mc_instance_old_json["installedAddons"]) - 1

            new_addon_json = self.get_new_addon_with_id_json(diff.new_addon.addon_id)
            self.mc_instance_old_json["installedAddons"][i] = new_addon_json

        while self.mc_instance_bak_file.exists():
            self.mc_instance_bak_file = self.mc_instance_bak_file.with_suffix(self.mc_instance_bak_file.suffix + ".bak")
        self.mc_instance_old_file.rename(self.mc_instance_bak_file)

        with self.mc_instance_old_file.open("w", newline='\n') as f:
            json.dump(self.mc_instance_old_json, f, sort_keys=False, indent=2)
            print(f"Saved to: {f.name}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage of this script:")
        print("  differ.py /path/to/old/minecraftinstance.json /path/to/new/minecraftinstance.json")
        exit(1)

    Differ().go()
