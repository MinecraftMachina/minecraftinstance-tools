# Generated with https://app.quicktype.io/
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = minecraft_instance_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, Optional, TypeVar, Callable, Type, cast
from uuid import UUID


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


@dataclass
class BaseModLoader:
    id: int
    game_version_id: int
    minecraft_game_version_id: int
    forge_version: str
    name: str
    type: int
    download_url: str
    filename: str
    install_method: int
    latest: bool
    recommended: bool
    approved: bool
    date_modified: str
    maven_version_string: str
    version_json: str
    libraries_install_location: str
    minecraft_version: str
    mod_loader_game_version_id: int
    mod_loader_game_version_type_id: int
    mod_loader_game_version_status: int
    mod_loader_game_version_type_status: int
    mc_game_version_id: int
    mc_game_version_type_id: int
    mc_game_version_status: int
    mc_game_version_type_status: int

    @staticmethod
    def from_dict(obj: Any) -> 'BaseModLoader':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        game_version_id = from_int(obj.get("gameVersionId"))
        minecraft_game_version_id = from_int(obj.get("minecraftGameVersionId"))
        forge_version = from_str(obj.get("forgeVersion"))
        name = from_str(obj.get("name"))
        type = from_int(obj.get("type"))
        download_url = from_str(obj.get("downloadUrl"))
        filename = from_str(obj.get("filename"))
        install_method = from_int(obj.get("installMethod"))
        latest = from_bool(obj.get("latest"))
        recommended = from_bool(obj.get("recommended"))
        approved = from_bool(obj.get("approved"))
        date_modified = from_str(obj.get("dateModified"))
        maven_version_string = from_str(obj.get("mavenVersionString"))
        version_json = from_str(obj.get("versionJson"))
        libraries_install_location = from_str(obj.get("librariesInstallLocation"))
        minecraft_version = from_str(obj.get("minecraftVersion"))
        mod_loader_game_version_id = from_int(obj.get("modLoaderGameVersionId"))
        mod_loader_game_version_type_id = from_int(obj.get("modLoaderGameVersionTypeId"))
        mod_loader_game_version_status = from_int(obj.get("modLoaderGameVersionStatus"))
        mod_loader_game_version_type_status = from_int(obj.get("modLoaderGameVersionTypeStatus"))
        mc_game_version_id = from_int(obj.get("mcGameVersionId"))
        mc_game_version_type_id = from_int(obj.get("mcGameVersionTypeId"))
        mc_game_version_status = from_int(obj.get("mcGameVersionStatus"))
        mc_game_version_type_status = from_int(obj.get("mcGameVersionTypeStatus"))
        return BaseModLoader(id, game_version_id, minecraft_game_version_id, forge_version, name, type, download_url, filename, install_method, latest, recommended, approved, date_modified, maven_version_string, version_json, libraries_install_location, minecraft_version, mod_loader_game_version_id, mod_loader_game_version_type_id, mod_loader_game_version_status, mod_loader_game_version_type_status, mc_game_version_id, mc_game_version_type_id, mc_game_version_status, mc_game_version_type_status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["gameVersionId"] = from_int(self.game_version_id)
        result["minecraftGameVersionId"] = from_int(self.minecraft_game_version_id)
        result["forgeVersion"] = from_str(self.forge_version)
        result["name"] = from_str(self.name)
        result["type"] = from_int(self.type)
        result["downloadUrl"] = from_str(self.download_url)
        result["filename"] = from_str(self.filename)
        result["installMethod"] = from_int(self.install_method)
        result["latest"] = from_bool(self.latest)
        result["recommended"] = from_bool(self.recommended)
        result["approved"] = from_bool(self.approved)
        result["dateModified"] = from_str(self.date_modified)
        result["mavenVersionString"] = from_str(self.maven_version_string)
        result["versionJson"] = from_str(self.version_json)
        result["librariesInstallLocation"] = from_str(self.libraries_install_location)
        result["minecraftVersion"] = from_str(self.minecraft_version)
        result["modLoaderGameVersionId"] = from_int(self.mod_loader_game_version_id)
        result["modLoaderGameVersionTypeId"] = from_int(self.mod_loader_game_version_type_id)
        result["modLoaderGameVersionStatus"] = from_int(self.mod_loader_game_version_status)
        result["modLoaderGameVersionTypeStatus"] = from_int(self.mod_loader_game_version_type_status)
        result["mcGameVersionId"] = from_int(self.mc_game_version_id)
        result["mcGameVersionTypeId"] = from_int(self.mc_game_version_type_id)
        result["mcGameVersionStatus"] = from_int(self.mc_game_version_status)
        result["mcGameVersionTypeStatus"] = from_int(self.mc_game_version_type_status)
        return result


@dataclass
class Dependency:
    id: int
    addon_id: int
    type: int
    file_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Dependency':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        addon_id = from_int(obj.get("addonId"))
        type = from_int(obj.get("type"))
        file_id = from_int(obj.get("fileId"))
        return Dependency(id, addon_id, type, file_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["addonId"] = from_int(self.addon_id)
        result["type"] = from_int(self.type)
        result["fileId"] = from_int(self.file_id)
        return result


@dataclass
class Module:
    foldername: str
    fingerprint: int
    type: int

    @staticmethod
    def from_dict(obj: Any) -> 'Module':
        assert isinstance(obj, dict)
        foldername = from_str(obj.get("foldername"))
        fingerprint = from_int(obj.get("fingerprint"))
        type = from_int(obj.get("type"))
        return Module(foldername, fingerprint, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["foldername"] = from_str(self.foldername)
        result["fingerprint"] = from_int(self.fingerprint)
        result["type"] = from_int(self.type)
        return result


@dataclass
class InstalledFile:
    id: int
    display_name: str
    file_name: str
    file_date: str
    file_length: int
    release_type: int
    file_status: int
    download_url: str
    is_alternate: bool
    alternate_file_id: int
    dependencies: List[Dependency]
    is_available: bool
    modules: List[Module]
    package_fingerprint: int
    game_version: List[str]
    has_install_script: bool
    is_compatible_with_client: bool
    category_section_package_type: int
    restrict_project_file_access: int
    project_status: int
    project_id: int
    game_version_date_released: str
    game_id: int
    is_server_pack: bool
    file_name_on_disk: str

    @staticmethod
    def from_dict(obj: Any) -> 'InstalledFile':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        display_name = from_str(obj.get("displayName"))
        file_name = from_str(obj.get("fileName"))
        file_date = from_str(obj.get("fileDate"))
        file_length = from_int(obj.get("fileLength"))
        release_type = from_int(obj.get("releaseType"))
        file_status = from_int(obj.get("fileStatus"))
        download_url = from_str(obj.get("downloadUrl"))
        is_alternate = from_bool(obj.get("isAlternate"))
        alternate_file_id = from_int(obj.get("alternateFileId"))
        dependencies = from_list(Dependency.from_dict, obj.get("dependencies"))
        is_available = from_bool(obj.get("isAvailable"))
        modules = from_list(Module.from_dict, obj.get("modules"))
        package_fingerprint = from_int(obj.get("packageFingerprint"))
        game_version = from_list(from_str, obj.get("gameVersion"))
        has_install_script = from_bool(obj.get("hasInstallScript"))
        is_compatible_with_client = from_bool(obj.get("isCompatibleWithClient"))
        category_section_package_type = from_int(obj.get("categorySectionPackageType"))
        restrict_project_file_access = from_int(obj.get("restrictProjectFileAccess"))
        project_status = from_int(obj.get("projectStatus"))
        project_id = from_int(obj.get("projectId"))
        game_version_date_released = from_str(obj.get("gameVersionDateReleased"))
        game_id = from_int(obj.get("gameId"))
        is_server_pack = from_bool(obj.get("isServerPack"))
        file_name_on_disk = from_str(obj.get("FileNameOnDisk"))
        return InstalledFile(id, display_name, file_name, file_date, file_length, release_type, file_status, download_url, is_alternate, alternate_file_id, dependencies, is_available, modules, package_fingerprint, game_version, has_install_script, is_compatible_with_client, category_section_package_type, restrict_project_file_access, project_status, project_id, game_version_date_released, game_id, is_server_pack, file_name_on_disk)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["displayName"] = from_str(self.display_name)
        result["fileName"] = from_str(self.file_name)
        result["fileDate"] = from_str(self.file_date)
        result["fileLength"] = from_int(self.file_length)
        result["releaseType"] = from_int(self.release_type)
        result["fileStatus"] = from_int(self.file_status)
        result["downloadUrl"] = from_str(self.download_url)
        result["isAlternate"] = from_bool(self.is_alternate)
        result["alternateFileId"] = from_int(self.alternate_file_id)
        result["dependencies"] = from_list(lambda x: to_class(Dependency, x), self.dependencies)
        result["isAvailable"] = from_bool(self.is_available)
        result["modules"] = from_list(lambda x: to_class(Module, x), self.modules)
        result["packageFingerprint"] = from_int(self.package_fingerprint)
        result["gameVersion"] = from_list(from_str, self.game_version)
        result["hasInstallScript"] = from_bool(self.has_install_script)
        result["isCompatibleWithClient"] = from_bool(self.is_compatible_with_client)
        result["categorySectionPackageType"] = from_int(self.category_section_package_type)
        result["restrictProjectFileAccess"] = from_int(self.restrict_project_file_access)
        result["projectStatus"] = from_int(self.project_status)
        result["projectId"] = from_int(self.project_id)
        result["gameVersionDateReleased"] = from_str(self.game_version_date_released)
        result["gameId"] = from_int(self.game_id)
        result["isServerPack"] = from_bool(self.is_server_pack)
        result["FileNameOnDisk"] = from_str(self.file_name_on_disk)
        return result


@dataclass
class InstalledAddon:
    addon_id: int
    game_instance_id: UUID
    installed_file: InstalledFile
    date_installed: str
    date_updated: str
    date_last_update_attempted: str
    status: int
    preference_auto_install_updates: bool
    preference_alternate_file: bool
    preference_is_ignored: bool
    is_modified: bool
    is_working_copy: bool
    is_fuzzy_match: bool
    preference_release_type: None
    manifest_name: None
    installed_targets: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InstalledAddon':
        assert isinstance(obj, dict)
        addon_id = from_int(obj.get("addonID"))
        game_instance_id = UUID(obj.get("gameInstanceID"))
        installed_file = InstalledFile.from_dict(obj.get("installedFile"))
        date_installed = from_str(obj.get("dateInstalled"))
        date_updated = from_str(obj.get("dateUpdated"))
        date_last_update_attempted = from_str(obj.get("dateLastUpdateAttempted"))
        status = from_int(obj.get("status"))
        preference_auto_install_updates = from_bool(obj.get("preferenceAutoInstallUpdates"))
        preference_alternate_file = from_bool(obj.get("preferenceAlternateFile"))
        preference_is_ignored = from_bool(obj.get("preferenceIsIgnored"))
        is_modified = from_bool(obj.get("isModified"))
        is_working_copy = from_bool(obj.get("isWorkingCopy"))
        is_fuzzy_match = from_bool(obj.get("isFuzzyMatch"))
        preference_release_type = from_none(obj.get("preferenceReleaseType"))
        manifest_name = from_none(obj.get("manifestName"))
        installed_targets = from_union([from_none, lambda x: from_list(lambda x: x, x)], obj.get("installedTargets"))
        return InstalledAddon(addon_id, game_instance_id, installed_file, date_installed, date_updated, date_last_update_attempted, status, preference_auto_install_updates, preference_alternate_file, preference_is_ignored, is_modified, is_working_copy, is_fuzzy_match, preference_release_type, manifest_name, installed_targets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["addonID"] = from_int(self.addon_id)
        result["gameInstanceID"] = str(self.game_instance_id)
        result["installedFile"] = to_class(InstalledFile, self.installed_file)
        result["dateInstalled"] = from_str(self.date_installed)
        result["dateUpdated"] = from_str(self.date_updated)
        result["dateLastUpdateAttempted"] = from_str(self.date_last_update_attempted)
        result["status"] = from_int(self.status)
        result["preferenceAutoInstallUpdates"] = from_bool(self.preference_auto_install_updates)
        result["preferenceAlternateFile"] = from_bool(self.preference_alternate_file)
        result["preferenceIsIgnored"] = from_bool(self.preference_is_ignored)
        result["isModified"] = from_bool(self.is_modified)
        result["isWorkingCopy"] = from_bool(self.is_working_copy)
        result["isFuzzyMatch"] = from_bool(self.is_fuzzy_match)
        result["preferenceReleaseType"] = from_none(self.preference_release_type)
        result["manifestName"] = from_none(self.manifest_name)
        result["installedTargets"] = from_union([from_none, lambda x: from_list(lambda x: x, x)], self.installed_targets)
        return result


@dataclass
class SyncProfile:
    preference_enabled: bool
    preference_auto_sync: bool
    preference_auto_delete: bool
    preference_backup_saved_variables: bool
    game_instance_guid: UUID
    sync_profile_id: int
    saved_variables_profile: None
    last_sync_date: str

    @staticmethod
    def from_dict(obj: Any) -> 'SyncProfile':
        assert isinstance(obj, dict)
        preference_enabled = from_bool(obj.get("PreferenceEnabled"))
        preference_auto_sync = from_bool(obj.get("PreferenceAutoSync"))
        preference_auto_delete = from_bool(obj.get("PreferenceAutoDelete"))
        preference_backup_saved_variables = from_bool(obj.get("PreferenceBackupSavedVariables"))
        game_instance_guid = UUID(obj.get("GameInstanceGuid"))
        sync_profile_id = from_int(obj.get("SyncProfileID"))
        saved_variables_profile = from_none(obj.get("SavedVariablesProfile"))
        last_sync_date = from_str(obj.get("LastSyncDate"))
        return SyncProfile(preference_enabled, preference_auto_sync, preference_auto_delete, preference_backup_saved_variables, game_instance_guid, sync_profile_id, saved_variables_profile, last_sync_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PreferenceEnabled"] = from_bool(self.preference_enabled)
        result["PreferenceAutoSync"] = from_bool(self.preference_auto_sync)
        result["PreferenceAutoDelete"] = from_bool(self.preference_auto_delete)
        result["PreferenceBackupSavedVariables"] = from_bool(self.preference_backup_saved_variables)
        result["GameInstanceGuid"] = str(self.game_instance_guid)
        result["SyncProfileID"] = from_int(self.sync_profile_id)
        result["SavedVariablesProfile"] = from_none(self.saved_variables_profile)
        result["LastSyncDate"] = from_str(self.last_sync_date)
        return result


@dataclass
class MinecraftInstance:
    base_mod_loader: BaseModLoader
    is_unlocked: bool
    java_args_override: None
    java_dir_override: None
    last_played: str
    manifest: None
    file_date: str
    installed_modpack: None
    project_id: int
    file_id: int
    custom_author: str
    modpack_overrides: None
    is_memory_override: bool
    allocated_memory: int
    guid: UUID
    game_type_id: int
    install_path: str
    name: str
    cached_scans: List[Any]
    is_valid: bool
    last_previous_match_update: str
    is_enabled: bool
    is_pinned: bool
    game_version: str
    preference_alternate_file: bool
    preference_auto_install_updates: bool
    preference_quick_delete_libraries: bool
    preference_delete_saved_variables: bool
    preference_process_file_commands: bool
    preference_release_type: int
    sync_profile: SyncProfile
    preference_show_add_on_info: bool
    install_date: str
    installed_addons: List[InstalledAddon]
    is_migrated: bool
    preference_upload_profile: bool

    @staticmethod
    def from_dict(obj: Any) -> 'MinecraftInstance':
        assert isinstance(obj, dict)
        base_mod_loader = BaseModLoader.from_dict(obj.get("baseModLoader"))
        is_unlocked = from_bool(obj.get("isUnlocked"))
        java_args_override = from_none(obj.get("javaArgsOverride"))
        java_dir_override = from_none(obj.get("javaDirOverride"))
        last_played = from_str(obj.get("lastPlayed"))
        manifest = from_none(obj.get("manifest"))
        file_date = from_str(obj.get("fileDate"))
        installed_modpack = from_none(obj.get("installedModpack"))
        project_id = from_int(obj.get("projectID"))
        file_id = from_int(obj.get("fileID"))
        custom_author = from_str(obj.get("customAuthor"))
        modpack_overrides = from_none(obj.get("modpackOverrides"))
        is_memory_override = from_bool(obj.get("isMemoryOverride"))
        allocated_memory = from_int(obj.get("allocatedMemory"))
        guid = UUID(obj.get("guid"))
        game_type_id = from_int(obj.get("gameTypeID"))
        install_path = from_str(obj.get("installPath"))
        name = from_str(obj.get("name"))
        cached_scans = from_list(lambda x: x, obj.get("cachedScans"))
        is_valid = from_bool(obj.get("isValid"))
        last_previous_match_update = from_str(obj.get("lastPreviousMatchUpdate"))
        is_enabled = from_bool(obj.get("isEnabled"))
        is_pinned = from_bool(obj.get("isPinned"))
        game_version = from_str(obj.get("gameVersion"))
        preference_alternate_file = from_bool(obj.get("preferenceAlternateFile"))
        preference_auto_install_updates = from_bool(obj.get("preferenceAutoInstallUpdates"))
        preference_quick_delete_libraries = from_bool(obj.get("preferenceQuickDeleteLibraries"))
        preference_delete_saved_variables = from_bool(obj.get("preferenceDeleteSavedVariables"))
        preference_process_file_commands = from_bool(obj.get("preferenceProcessFileCommands"))
        preference_release_type = from_int(obj.get("preferenceReleaseType"))
        sync_profile = SyncProfile.from_dict(obj.get("syncProfile"))
        preference_show_add_on_info = from_bool(obj.get("preferenceShowAddOnInfo"))
        install_date = from_str(obj.get("installDate"))
        installed_addons = from_list(InstalledAddon.from_dict, obj.get("installedAddons"))
        is_migrated = from_bool(obj.get("isMigrated"))
        preference_upload_profile = from_bool(obj.get("preferenceUploadProfile"))
        return MinecraftInstance(base_mod_loader, is_unlocked, java_args_override, java_dir_override, last_played, manifest, file_date, installed_modpack, project_id, file_id, custom_author, modpack_overrides, is_memory_override, allocated_memory, guid, game_type_id, install_path, name, cached_scans, is_valid, last_previous_match_update, is_enabled, is_pinned, game_version, preference_alternate_file, preference_auto_install_updates, preference_quick_delete_libraries, preference_delete_saved_variables, preference_process_file_commands, preference_release_type, sync_profile, preference_show_add_on_info, install_date, installed_addons, is_migrated, preference_upload_profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["baseModLoader"] = to_class(BaseModLoader, self.base_mod_loader)
        result["isUnlocked"] = from_bool(self.is_unlocked)
        result["javaArgsOverride"] = from_none(self.java_args_override)
        result["javaDirOverride"] = from_none(self.java_dir_override)
        result["lastPlayed"] = from_str(self.last_played)
        result["manifest"] = from_none(self.manifest)
        result["fileDate"] = from_str(self.file_date)
        result["installedModpack"] = from_none(self.installed_modpack)
        result["projectID"] = from_int(self.project_id)
        result["fileID"] = from_int(self.file_id)
        result["customAuthor"] = from_str(self.custom_author)
        result["modpackOverrides"] = from_none(self.modpack_overrides)
        result["isMemoryOverride"] = from_bool(self.is_memory_override)
        result["allocatedMemory"] = from_int(self.allocated_memory)
        result["guid"] = str(self.guid)
        result["gameTypeID"] = from_int(self.game_type_id)
        result["installPath"] = from_str(self.install_path)
        result["name"] = from_str(self.name)
        result["cachedScans"] = from_list(lambda x: x, self.cached_scans)
        result["isValid"] = from_bool(self.is_valid)
        result["lastPreviousMatchUpdate"] = from_str(self.last_previous_match_update)
        result["isEnabled"] = from_bool(self.is_enabled)
        result["isPinned"] = from_bool(self.is_pinned)
        result["gameVersion"] = from_str(self.game_version)
        result["preferenceAlternateFile"] = from_bool(self.preference_alternate_file)
        result["preferenceAutoInstallUpdates"] = from_bool(self.preference_auto_install_updates)
        result["preferenceQuickDeleteLibraries"] = from_bool(self.preference_quick_delete_libraries)
        result["preferenceDeleteSavedVariables"] = from_bool(self.preference_delete_saved_variables)
        result["preferenceProcessFileCommands"] = from_bool(self.preference_process_file_commands)
        result["preferenceReleaseType"] = from_int(self.preference_release_type)
        result["syncProfile"] = to_class(SyncProfile, self.sync_profile)
        result["preferenceShowAddOnInfo"] = from_bool(self.preference_show_add_on_info)
        result["installDate"] = from_str(self.install_date)
        result["installedAddons"] = from_list(lambda x: to_class(InstalledAddon, x), self.installed_addons)
        result["isMigrated"] = from_bool(self.is_migrated)
        result["preferenceUploadProfile"] = from_bool(self.preference_upload_profile)
        return result


def minecraft_instance_from_dict(s: Any) -> MinecraftInstance:
    return MinecraftInstance.from_dict(s)


def minecraft_instance_to_dict(x: MinecraftInstance) -> Any:
    return to_class(MinecraftInstance, x)
